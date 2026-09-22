from __future__ import annotations

import math
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import Optional
from typing import Sequence
from typing import Union
import warnings

import numpy as np

from optuna._hypervolume import WFG
from optuna._hypervolume.hssp import _solve_hssp
from optuna.distributions import BaseDistribution
from optuna.distributions import CategoricalChoiceType
from optuna.exceptions import ExperimentalWarning
from optuna.logging import get_logger
from optuna.samplers._base import _CONSTRAINTS_KEY
from optuna.samplers._base import _process_constraints_after_trial
from optuna.samplers._base import BaseSampler
from optuna.samplers._lazy_random_state import LazyRandomState
from optuna.samplers._random import RandomSampler
from optuna.samplers._tpe.parzen_estimator import _ParzenEstimator
from optuna.samplers._tpe.parzen_estimator import _ParzenEstimatorParameters
from optuna.search_space import IntersectionSearchSpace
from optuna.search_space.group_decomposed import _GroupDecomposedSearchSpace
from optuna.search_space.group_decomposed import _SearchSpaceGroup
from optuna.study import Study
from optuna.study._study_direction import StudyDirection
from optuna.trial import FrozenTrial
from optuna.trial import TrialState


EPS = 1e-12
_logger = get_logger(__name__)


def default_gamma(x: int) -> int:
    return min(int(np.ceil(0.1 * x)), 25)


def hyperopt_default_gamma(x: int) -> int:
    return min(int(np.ceil(0.25 * np.sqrt(x))), 25)


def default_weights(x: int) -> np.ndarray:
    if x == 0:
        return np.asarray([])
    elif x < 25:
        return np.ones(x)
    else:
        ramp = np.linspace(1.0 / x, 1.0, num=x - 25)
        flat = np.ones(25)
        return np.concatenate([ramp, flat], axis=0)


class TPESampler(BaseSampler):
    """Sampler using TPE (Tree-structured Parzen Estimator) algorithm.

    This sampler is based on *independent sampling*.
    See also :class:`~optuna.samplers.BaseSampler` for more details of 'independent sampling'.

    On each trial, for each parameter, TPE fits one Gaussian Mixture Model (GMM) ``l(x)`` to
    the set of parameter values associated with the best objective values, and another GMM
    ``g(x)`` to the remaining parameter values. It chooses the parameter value ``x`` that
    maximizes the ratio ``l(x)/g(x)``.

    For further information about TPE algorithm, please refer to the following papers:

    - `Algorithms for Hyper-Parameter Optimization
      <https://papers.nips.cc/paper/4443-algorithms-for-hyper-parameter-optimization.pdf>`_
    - `Making a Science of Model Search: Hyperparameter Optimization in Hundreds of
      Dimensions for Vision Architectures <http://proceedings.mlr.press/v28/bergstra13.pdf>`_
    - `Tree-Structured Parzen Estimator: Understanding Its Algorithm Components and Their Roles for
      Better Empirical Performance <https://arxiv.org/abs/2304.11127>`_

    For multi-objective TPE (MOTPE), please refer to the following papers:
    - `Multiobjective Tree-Structured Parzen Estimator for Computationally Expensive Optimization
      Problems <https://dl.acm.org/doi/10.1145/3377930.3389817>`_
    - `Multiobjective Tree-Structured Parzen Estimator <https://doi.org/10.1613/jair.1.13188>`_

    Example:
        An example of a single-objective optimization is as follows:

        .. testcode::

            import optuna
            from optuna.samplers import TPESampler


            def objective(trial):
                x = trial.suggest_float("x", -10, 10)
                return x**2


            study = optuna.create_study(sampler=TPESampler())
            study.optimize(objective, n_trials=10)

    .. note::
        For `v2.9.0 <https://github.com/optuna/optuna/releases/tag/v2.9.0>`_ or later,
        MOTPESampler is deprecated and TPESampler should be used instead.
        The following code shows how you run TPESampler on a multi-objective task:

        .. testcod
# ... [truncated] ...
erence_point = np.maximum(1.1 * worst_point, 0.9 * worst_point)
        reference_point[reference_point == 0] = EPS
        selected_indices = _solve_hssp(rank_i_lvals, rank_i_indices, subset_size, reference_point)
        indices_below[last_idx:] = selected_indices

    below_trials = []
    above_trials = []
    for index in range(len(trials)):
        if index in indices_below:
            below_trials.append(trials[index])
        else:
            above_trials.append(trials[index])
    return below_trials, above_trials


def _get_pruned_trial_score(trial: FrozenTrial, study: Study) -> tuple[float, float]:
    if len(trial.intermediate_values) > 0:
        step, intermediate_value = max(trial.intermediate_values.items())
        if math.isnan(intermediate_value):
            return -step, float("inf")
        elif study.direction == StudyDirection.MINIMIZE:
            return -step, intermediate_value
        else:
            return -step, -intermediate_value
    else:
        return 1, 0.0


def _split_pruned_trials(
    trials: Sequence[FrozenTrial],
    study: Study,
    n_below: int,
) -> tuple[list[FrozenTrial], list[FrozenTrial]]:
    n_below = min(n_below, len(trials))
    sorted_trials = sorted(trials, key=lambda trial: _get_pruned_trial_score(trial, study))
    return sorted_trials[:n_below], sorted_trials[n_below:]


def _get_infeasible_trial_score(trial: FrozenTrial) -> float:
    constraint = trial.system_attrs.get(_CONSTRAINTS_KEY)
    if constraint is None:
        warnings.warn(
            f"Trial {trial.number} does not have constraint values."
            " It will be treated as a lower priority than other trials."
        )
        return float("inf")
    else:
        # Violation values of infeasible dimensions are summed up.
        return sum(v for v in constraint if v > 0)


def _split_infeasible_trials(
    trials: Sequence[FrozenTrial], n_below: int
) -> tuple[list[FrozenTrial], list[FrozenTrial]]:
    n_below = min(n_below, len(trials))
    sorted_trials = sorted(trials, key=_get_infeasible_trial_score)
    return sorted_trials[:n_below], sorted_trials[n_below:]


def _calculate_weights_below_for_multi_objective(
    study: Study,
    below_trials: list[FrozenTrial],
    constraints_func: Callable[[FrozenTrial], Sequence[float]] | None,
) -> np.ndarray:
    loss_vals = []
    feasible_mask = np.ones(len(below_trials), dtype=bool)
    for i, trial in enumerate(below_trials):
        # Hypervolume contributions are calculated only using feasible trials.
        if constraints_func is not None:
            if any(constraint > 0 for constraint in constraints_func(trial)):
                feasible_mask[i] = False
                continue
        values = []
        for value, direction in zip(trial.values, study.directions):
            if direction == StudyDirection.MINIMIZE:
                values.append(value)
            else:
                values.append(-value)
        loss_vals.append(values)
    lvals = np.asarray(loss_vals, dtype=float)

    # Calculate weights based on hypervolume contributions.
    n_below = len(lvals)
    weights_below: np.ndarray
    if n_below == 0:
        weights_below = np.asarray([])
    elif n_below == 1:
        weights_below = np.asarray([1.0])
    else:
        worst_point = np.max(lvals, axis=0)
        reference_point = np.maximum(1.1 * worst_point, 0.9 * worst_point)
        reference_point[reference_point == 0] = EPS
        hv = WFG().compute(lvals, reference_point)
        indices_mat = ~np.eye(n_below).astype(bool)
        contributions = np.asarray(
            [hv - WFG().compute(lvals[indices_mat[i]], reference_point) for i in range(n_below)]
        )
        contributions += EPS
        weights_below = np.clip(contributions / np.max(contributions), 0, 1)

    # For now, EPS weight is assigned to infeasible trials.
    weights_below_all = np.full(len(below_trials), EPS)
    weights_below_all[feasible_mask] = weights_below
    return weights_below_all


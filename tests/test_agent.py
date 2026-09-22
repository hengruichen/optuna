import json
import os
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from optuna_agent.agent import Agent, AgentConfig
from optuna_agent.agent_config import AgentConfigError
from optuna_agent.config import ConfigError, ConfigValidationError
from optuna_agent.utils import get_project_root


@pytest.fixture
def mock_config():
    """Create a mock configuration for testing."""
    return MagicMock()


@pytest.fixture
def mock_agent_config():
    """Create a mock agent configuration for testing."""
    return MagicMock()


@pytest.fixture
def mock_agent(mock_config, mock_agent_config):
    """Create a mock Agent instance for testing."""
    return Agent(mock_config, mock_agent_config)


@pytest.fixture
def mock_agent_with_config():
    """Create a mock Agent instance with a valid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock_agent_with_invalid_config():
    """Create a mock Agent instance with an invalid configuration."""
    config = MagicMock()
    agent_config = MagicMock()
    agent = Agent(config, agent_config)
    return agent, config, agent_config


@pytest.fixture
def mock
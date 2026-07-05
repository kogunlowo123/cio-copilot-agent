"""Test configuration for CIO Copilot Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "cio-copilot-agent", "category": "Executive"}

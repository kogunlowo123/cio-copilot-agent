"""CIO Copilot Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_assess_it_portfolio():
    """Test Assess health of IT application and infrastructure portfolio."""
    tools = AgentTools()
    result = await tools.assess_it_portfolio(scope="test", assessment_criteria="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_transformation():
    """Test Track digital transformation initiative progress."""
    tools = AgentTools()
    result = await tools.track_transformation(program_id="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_evaluate_vendor():
    """Test Evaluate IT vendor performance and contract value."""
    tools = AgentTools()
    result = await tools.evaluate_vendor(vendor_id="test", evaluation_criteria="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_assess_tech_risk():
    """Test Assess technology risks (tech debt, end-of-life, security)."""
    tools = AgentTools()
    result = await tools.assess_tech_risk(scope="test", risk_categories="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.cio_copilot_agent_agent import CioCopilotAgentAgent
    agent = CioCopilotAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0

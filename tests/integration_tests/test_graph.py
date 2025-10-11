import pytest
from langsmith import unit

from planner_agent import graph
from planner_agent.context import Context


@pytest.mark.asyncio
@unit
async def test_planner_agent_simple_passthrough() -> None:
    res = await graph.ainvoke(
        {"messages": [("user", "Who is the founder of LangChain?")]},  # type: ignore
        context=Context(system_prompt="You are a helpful AI assistant."),
    )

    assert "harrison" in str(res["messages"][-1].content).lower()

"""This module provides example tools for web scraping and search functionality.

It includes a basic Tavily search function (as an example)

These tools are intended as free examples to get started. For production use,
consider implementing more robust and specialized tools tailored to your needs.
"""

import logging
import json
from typing import Any, Callable, List, Optional, cast

from langchain_tavily import TavilySearch
from langgraph.runtime import get_runtime

from planner_agent.context import Context
from planner_agent.mcp import get_mcp_tools

logger = logging.getLogger(__name__)


async def web_search(query: str) -> dict[str, Any] | None:
    """Search for general web results.

    This function performs a search using the Tavily search engine, which is designed
    to provide comprehensive, accurate, and trusted results. It's particularly useful
    for answering questions about current events.
    """
    runtime = get_runtime(Context)
    wrapped = TavilySearch(max_results=runtime.context.max_search_results)
    return cast(dict[str, Any], await wrapped.ainvoke({"query": query}))


async def get_tools() -> List[Callable[..., Any]]:
    """Get all available tools based on configuration."""
    tools = []
    runtime = get_runtime(Context)

    if runtime.context.enable_web_search:
        tools.append(web_search)

    mcp_server_configs = json.loads(runtime.context.mcp_server_configs)
    mcp_tools = await get_mcp_tools(server_configs=mcp_server_configs)
    tools.extend(mcp_tools)

    logger.info(f"Loaded {len(tools)} tools")

    return tools

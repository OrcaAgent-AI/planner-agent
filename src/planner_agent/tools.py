"""Web scraping and search functionality tools."""

import logging
from typing import Callable, cast

from langchain_tavily import TavilySearch
from langgraph.graph.state import RunnableConfig
from langgraph.runtime import get_runtime
from orcakit_sdk.mcp_adapter import get_mcp_tools

from planner_agent.context import Context, get_context

logger = logging.getLogger(__name__)


async def web_search(query: str, config: RunnableConfig) -> dict[str, object] | None:
    """Search for general web results using Tavily search engine."""
    ctx = get_context(get_runtime(Context))
    max_search_results = (
        config.get("configurable", {}).get("max_search_results", None)
        or ctx.max_search_results
    )
    include_domains = config.get("configurable", {}).get("include_domains", None)

    kwargs = {"max_results": max_search_results}
    if include_domains:
        kwargs["include_domains"] = include_domains

    wrapped = TavilySearch(**kwargs)
    return cast(dict[str, object], await wrapped.ainvoke({"query": query}))


async def get_tools(config: RunnableConfig) -> list[Callable[..., object]]:
    """Get all available tools based on configuration."""
    tools: list[Callable[..., object]] = []
    ctx = get_context(get_runtime(Context))

    enable_web_search = (
        config.get("configurable", {}).get("enable_web_search", None)
        or ctx.enable_web_search
    )
    if enable_web_search:
        tools.append(web_search)

    mcp_server_configs = (
        config.get("configurable", {}).get("mcp_server_configs", None)
        or ctx.mcp_server_configs
    )
    mcp_tools = await get_mcp_tools(mcp_server_configs)
    tools.extend(mcp_tools)

    logger.info("Loaded %d tools", len(tools))

    return tools

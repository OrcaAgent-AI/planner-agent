"""Define the configurable parameters for the agent."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Annotated

from langgraph.runtime import Runtime
from orcakit_sdk.context import EnvAwareConfig

from planner_agent.mcp_server_configs import MCP_SERVERS

from . import prompts


def get_context(runtime: Runtime[Context] | None) -> Context:
    """Get context from runtime, returning default Context if runtime or context is None.

    Handles the case where runtime.context is a dict (e.g., when passed via with_config)
    by converting it to a Context object.

    Args:
        runtime: The runtime object containing context, or None.

    Returns:
        Context: The context from runtime, or a new default Context instance.
    """
    if runtime is None or runtime.context is None:
        return Context()

    ctx = runtime.context
    # Handle case where context is a dict (from with_config configurable)
    if isinstance(ctx, dict):
        # Filter only known Context fields to avoid unexpected kwargs
        context_fields = {
            "system_prompt",
            "plan_model",
            "replan_model",
            "execute_model",
            "max_search_results",
            "enable_web_search",
            "mcp_server_configs",
        }
        filtered = {
            k: v for k, v in ctx.items() if k in context_fields and v is not None
        }
        return Context(**filtered)

    return ctx


@dataclass(kw_only=True)
class Context(EnvAwareConfig):
    """The context for the agent."""

    system_prompt: str = field(
        default=prompts.SYSTEM_PROMPT,
        metadata={
            "description": "The system prompt to use for the agent's interactions. "
            "This prompt sets the context and behavior for the agent."
        },
    )

    plan_model: Annotated[str, {"__template_metadata__": {"kind": "llm"}}] = field(
        default="compatible_openai/DeepSeek-V3-0324",
        metadata={
            "description": "The name of the language model to use for planning phase. "
            "Should be in the form: provider/model-name."
        },
    )

    replan_model: Annotated[str, {"__template_metadata__": {"kind": "llm"}}] = field(
        default="compatible_openai/DeepSeek-V3-0324",
        metadata={
            "description": "The name of the language model to use for replanning/reflection phase. "
            "Should be in the form: provider/model-name."
        },
    )

    execute_model: Annotated[str, {"__template_metadata__": {"kind": "llm"}}] = field(
        default="compatible_openai/DeepSeek-V3-0324",
        metadata={
            "description": "The name of the language model to use for execution phase. "
            "Should be in the form: provider/model-name."
        },
    )

    max_search_results: int = field(
        default=10,
        metadata={
            "description": "The maximum number of search results to return for each search query."
        },
    )

    enable_web_search: bool = field(
        default=True,
        metadata={
            "description": "Whether to enable web search functionality. "
            "When False, web search tools will be disabled."
        },
    )

    mcp_server_configs: str = field(
        default=json.dumps(MCP_SERVERS, indent=2),
        metadata={
            "description": "JSON string containing MCP server configurations. "
            "This defines which MCP servers are available and their connection settings."
        },
    )

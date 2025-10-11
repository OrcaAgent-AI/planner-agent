"""Define the state structures for the agent."""

from __future__ import annotations

import operator
from dataclasses import dataclass, field
from typing import Any, List, Sequence, Tuple

from langchain_core.messages import AnyMessage
from langgraph.graph import add_messages
from typing_extensions import Annotated


@dataclass
class InputState:
    """Defines the input state for the agent, representing a narrower interface to the outside world.

    This class is used to define the initial state and structure of incoming data.
    """

    messages: Annotated[Sequence[AnyMessage], add_messages] = field(
        default_factory=list
    )
    """
    Messages tracking the primary execution state of the agent.

    Typically accumulates a pattern of:
    1. HumanMessage - user input
    2. AIMessage with .tool_calls - agent picking tool(s) to use to collect information
    3. ToolMessage(s) - the responses (or errors) from the executed tools
    4. AIMessage without .tool_calls - agent responding in unstructured format to the user
    5. HumanMessage - user responds with the next conversational turn

    Steps 2-5 may repeat as needed.

    The `add_messages` annotation ensures that new messages are merged with existing ones,
    updating by ID to maintain an "append-only" state unless a message with the same ID is provided.
    """


@dataclass
class State(InputState):
    """Represents the complete state of the agent, extending InputState with additional attributes.

    This class can be used to store any information needed throughout the agent's lifecycle.
    """

    input: str = field(default="")
    """
    String representing the user's input question or request.
    
    This contains the original user input that initiated the planning and execution process.
    It serves as the primary objective for the agent to accomplish.
    """

    initial_plan: List[str] = field(default_factory=list)
    """
    List of strings representing the initial planning steps.
    
    This contains the original plan created at the beginning of the execution.
    """

    plan: List[str] = field(default_factory=list)
    """
    List of strings representing the current planning steps.
    
    This contains the current plan which may be updated during execution.
    """

    past_steps: Annotated[List[Tuple[str, Any]], operator.add] = field(default_factory=list)
    """
    List of tuples representing completed steps.
    
    Each tuple contains information about a step that has been completed.
    The first element is typically the step description and the second element
    contains additional metadata or results.
    The operator.add annotation ensures that new steps are added to existing ones.
    """

    response: str = field(default="")
    """
    String representing the final response to be returned.
    
    This contains the final answer or result of the agent's execution.
    """

    # Additional attributes can be added here as needed.
    # Common examples include:
    # retrieved_documents: List[Document] = field(default_factory=list)
    # extracted_entities: Dict[str, Any] = field(default_factory=dict)
    # api_connections: Dict[str, Any] = field(default_factory=dict)

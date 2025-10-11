"""Tools and schemas for the planner agent."""

from typing import List, Union

from pydantic import BaseModel, Field


class Plan(BaseModel):
    """Execution plan."""
    steps: List[str] = Field(
        description="List of execution steps in order"
    )


class Response(BaseModel):
    """User response."""
    response: str


class Act(BaseModel):
    """Execution action."""
    action: Union[Response, Plan] = Field(
        description="Action to execute. Use Response to reply to user. Use Plan if tools are needed to get the answer."
    )
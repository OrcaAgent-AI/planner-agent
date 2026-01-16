"""Tools and schemas for the planner agent."""

from pydantic import BaseModel, Field


class Plan(BaseModel):
    """Execution plan."""

    steps: list[str] = Field(description="List of execution steps in order")


class Response(BaseModel):
    """User response."""

    response: str


class Act(BaseModel):
    """Execution action."""

    action: Response | Plan = Field(
        description="Action to execute. Use Response to reply to user. Use Plan if tools are needed to get the answer."
    )

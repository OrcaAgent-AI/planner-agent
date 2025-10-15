"""Custom model integrations for ReAct agent."""

import os

from langchain_openai import ChatOpenAI


def create_compatible_openai_client(model_name: str | None = None) -> ChatOpenAI:
    """Create and return a DeepSeek ChatOpenAI client instance."""
    from pydantic import SecretStr

    api_key = os.getenv("OPENAI_API_KEY")
    model = model_name or os.getenv("OPENAI_MODEL_NAME") or "gpt-3.5-turbo"

    return ChatOpenAI(
        api_key=SecretStr(api_key) if api_key else None,
        base_url=os.getenv("OPENAI_BASE_URL"),
        model=model,
        streaming=True,
        temperature=0.0,  # Add temperature parameter to control response creativity
        timeout=120,  # Use timeout instead of request_timeout
    )

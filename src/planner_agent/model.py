"""Custom model integrations for ReAct agent."""

import os

from langchain_openai import ChatOpenAI


def create_compatible_openai_client(model_name: str | None = None) -> ChatOpenAI:
    """Create and return a DeepSeek ChatOpenAI client instance."""
    return ChatOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),
        model_name=model_name or os.getenv("OPENAI_MODEL_NAME"),
        streaming=True,
        temperature=0.0,  # Add temperature parameter to control response creativity
        request_timeout=120,
    )
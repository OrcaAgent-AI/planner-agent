#!/usr/bin/env python3
"""Main entry point for running the Planner Agent HTTP server.

This module provides a command-line interface to start the Planner Agent
as an HTTP service with OpenAI-compatible and LangGraph endpoints.

Usage:
    # Start HTTP server with default settings
    python -m main

    # Specify host and port
    python -m main --host 0.0.0.0 --port 8888

    # Enable dev mode (hot reload on file changes)
    python -m main --dev

    # Enable debug logging
    python -m main --debug

Endpoints:
    - /langgraph/health  - Health check
    - /langgraph/call    - LangGraph chat endpoint
    - /langgraph/stream  - LangGraph streaming endpoint
    - /openai/chat/completions - OpenAI-compatible chat completions
    - /openai/models     - List available models
    - /docs              - API documentation (Swagger UI)
"""

# Load environment variables BEFORE any other imports
# This ensures Langfuse and other SDKs pick up the env vars during initialization
from dotenv import load_dotenv

load_dotenv()

import argparse  # noqa: E402
import logging  # noqa: E402

from orcakit_sdk.runner.agent import Agent  # noqa: E402

from planner_agent.graph import graph  # noqa: E402

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    """Parse command line arguments.

    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Start the Planner Agent HTTP server.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Start with default settings (0.0.0.0:8888)
    python -m main

    # Specify host and port
    python -m main --host 127.0.0.1 --port 9000

    # Enable dev mode (hot reload on file changes)
    python -m main --dev

    # Enable debug logging
    python -m main --debug

Endpoints:
    LangGraph:
        POST /langgraph/call         - Chat endpoint
        POST /langgraph/stream       - Streaming chat endpoint
        GET  /langgraph/health       - Health check

    OpenAI-compatible:
        POST /openai/chat/completions - Chat completions
        GET  /openai/models           - List models

    Documentation:
        GET  /docs                    - Swagger UI
        GET  /openapi.json            - OpenAPI schema
        """,
    )

    parser.add_argument(
        "--host",
        type=str,
        default="0.0.0.0",
        help="Host address to bind the server (default: 0.0.0.0)",
    )

    parser.add_argument(
        "--port",
        "-p",
        type=int,
        default=8888,
        help="Port number to bind the server (default: 8888)",
    )

    parser.add_argument(
        "--dev",
        action="store_true",
        help="Enable dev mode with hot reload (file changes auto-reload)",
    )

    parser.add_argument(
        "--reload",
        action="store_true",
        help="Enable auto-reload for development (alias for --dev)",
    )

    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging",
    )

    return parser.parse_args()


def configure_debug_mode() -> None:
    """Configure debug mode settings.

    Enables verbose logging for various components including:
    - LangChain/LangGraph internals
    - HTTP requests and responses
    - Tool execution details
    """
    # Set all loggers to DEBUG
    logging.getLogger().setLevel(logging.DEBUG)
    logging.getLogger("planner_agent").setLevel(logging.DEBUG)
    logging.getLogger("langchain").setLevel(logging.DEBUG)
    logging.getLogger("langgraph").setLevel(logging.DEBUG)
    logging.getLogger("httpx").setLevel(logging.DEBUG)
    logging.getLogger("uvicorn").setLevel(logging.DEBUG)

    # Enable LangChain debug mode
    try:
        from langchain.globals import set_debug, set_verbose

        set_debug(True)
        set_verbose(True)
    except ImportError:
        pass

    logger.debug("Debug mode enabled")


def main() -> None:
    """Run the Planner Agent HTTP server."""
    args = parse_args()

    # Configure logging level
    log_level = "debug" if args.debug else "info"
    if args.debug:
        configure_debug_mode()

    # Dev mode: --dev or --reload enables hot reload
    dev_mode = args.dev or args.reload

    if dev_mode:
        logger.info(
            f"Starting Planner Agent HTTP server in DEV mode on {args.host}:{args.port}"
        )
        logger.info("Hot reload enabled - file changes will trigger automatic reload")
    else:
        logger.info(f"Starting Planner Agent HTTP server on {args.host}:{args.port}")

    logger.info("API Documentation available at /docs")

    # Create Agent from the compiled graph and run HTTP server
    agent = Agent(graph=graph, name="Planner Agent")
    agent.run(
        host=args.host,
        port=args.port,
        dev=dev_mode,
        log_level=log_level,
    )


if __name__ == "__main__":
    main()

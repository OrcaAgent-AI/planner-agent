# OrcaAgent React Template

[🇨🇳 中文](README_CN.md) | 🇺🇸 English

[![CI](https://github.com/langchain-ai/react-agent/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/langchain-ai/react-agent/actions/workflows/unit-tests.yml)
[![Integration Tests](https://github.com/langchain-ai/react-agent/actions/workflows/integration-tests.yml/badge.svg)](https://github.com/langchain-ai/react-agent/actions/workflows/integration-tests.yml)
[![Open in - LangGraph Studio](https://img.shields.io/badge/Open_in-LangGraph_Studio-00324d.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4NS4zMzMiIGhlaWdodD0iODUuMzMzIiB2ZXJzaW9uPSIxLjAiIHZpZXdCb3g9IjAgMCA2NCA2NCI+PHBhdGggZD0iTTEzIDcuOGMtNi4zIDMuMS03LjEgNi4zLTYuOCAyNS43LjQgMjQuNi4zIDI0LjUgMjUuOSAyNC41QzU3LjUgNTggNTggNTcuNSA1OCAzMi4zIDU4IDcuMyA1Ni43IDYgMzIgNmMtMTIuOCAwLTE2LjEuMy0xOSAxLjhtMzcuNiAxNi42YzIuOCAyLjggMy40IDQuMiAzLjQgNy42cy0uNiA0LjgtMy40IDcuNkw0Ny4yIDQzSDE2LjhsLTMuNC0zLjRjLTQuOC00LjgtNC44LTEwLjQgMC0xNS4ybDMuNC0zLjRoMzAuNHoiLz48cGF0aCBkPSJNMTguOSAyNS42Yy0xLjEgMS4zLTEgMS43LjQgMi41LjkuNiAxLjcgMS44IDEuNyAyLjcgMCAxIC43IDIuOCAxLjYgNC4xIDEuNCAxLjkgMS40IDIuNS4zIDMuMi0xIC42LS42LjkgMS40LjkgMS41IDAgMi43LS41IDIuNy0xIDAtLjYgMS4xLS44IDIuNi0uNGwyLjYuNy0xLjgtMi45Yy01LjktOS4zLTkuNC0xMi4zLTExLjUtOS44TTM5IDI2YzAgMS4xLS45IDIuNS0yIDMuMi0yLjQgMS41LTIuNiAzLjQtLjUgNC4yLjguMyAyIDEuNyAyLjUgMy4xLjYgMS41IDEuNCAyLjMgMiAyIDEuNS0uOSAxLjItMy41LS40LTMuNS0yLjEgMC0yLjgtMi44LS44LTMuMyAxLjYtLjQgMS42LS41IDAtLjYtMS4xLS4xLTEuNS0uNi0xLjItMS42LjctMS43IDMuMy0yLjEgMy41LS41LjEuNS4yIDEuNi4zIDIuMiAwIC43LjkgMS40IDEuOSAxLjYgMi4xLjQgMi4zLTIuMy4yLTMuMi0uOC0uMy0yLTEuNy0yLjUtMy4xLTEuMS0zLTMtMy4zLTMtLjUiLz48L3N2Zz4=)](https://langgraph-studio.vercel.app/templates/open?githubUrl=https://github.com/langchain-ai/react-agent)

## 📖 Project Overview

**OrcaAgent** is an Agent development framework based on LangGraph, deeply integrating the rich ecosystem resources of LangChain/LangGraph. Built on industry best practices with necessary encapsulation, it provides rich Agent scenario templates and scaffolding tools.

### 🌟 Core Features

- **Ready to Use**: Pre-built standardized components for quick business scenario deployment
- **Ecosystem Compatibility**: Seamless reuse of LangChain toolchain and LangGraph workflow engine

## 🎯 React Template Features

This project is a React pattern-based Agent template provided by OrcaAgent, specifically optimized for tool calling and Q&A scenarios:

### ✨ Key Advantages

1. **Intelligent Tool Filtering**
   - Tool filtering before React execution
   - Suitable for Agents with numerous tools
   - Effectively reduces token usage and improves answer accuracy

2. **Tool-Only Mode**
   - Completely relies on tool calls to answer questions
   - Limits LLM response scope to avoid free-form answers
   - Ensures answer quality - doesn't answer unknown questions

3. **Model Compatibility**
   - Compatible with OpenAI protocol LLMs
   - Supports user-deployed models (prefixed with `compatible_openai/`)
   - Flexible model configuration options

## 🚀 Quick Start

### Environment Setup

1. **Create environment configuration file**
```bash
cp .env.example .env
```

2. **Configure API Keys**

Define necessary API keys in the `.env` file. By default, uses [Tavily](https://tavily.com/) search tool, which requires creating an API key [here](https://app.tavily.com/sign-in).

### Model Configuration

Default model configuration:
```yaml
model: anthropic/claude-3-5-sonnet-20240620
```

#### Anthropic Configuration
1. Get [Anthropic API key](https://console.anthropic.com/)
2. Add to `.env` file:
```
ANTHROPIC_API_KEY=your-api-key
```

#### OpenAI Configuration
1. Get [OpenAI API key](https://platform.openai.com/signup)
2. Add to `.env` file:
```
OPENAI_API_KEY=your-api-key
```

#### OpenAI Compatible Protocol Configuration
1. Edit `.env` file:
```
OPENAI_API_KEY=your-api-key
OPENAI_BASE_URL=your-base-url
OPENAI_MODEL_NAME=your-model-name
```

## 🛠️ Usage

### CLI Quick Start

#### 1. Download CLI
```bash
pip install orcaagent-cli
```

#### 2. Use CLI to Download Existing Templates

Download template [TEMPLATE] to path [PATH]:
```bash
orcaagent new [PATH] [TEMPLATE]
```
You can also use `orcaagent new` command for interactive template selection

#### 3. Configure .env
- Create `.env` in the downloaded template directory
- Get required API_KEYs and fill in `.env`, for example:
  - TAVILY_API_KEY
  - LANGSMITH_API_KEY
  - LLM API KEY

#### 4. Debug and Development
Enter the downloaded template directory:
```bash
cd [PATH]
```
Install necessary dependencies:
```bash
pip install -e .
```
Start debugging:
```bash
orcaagent dev
```

### CLI Features

#### Browse CLI Functions
```bash
orcaagent --help
```

#### Browse Existing Templates
```bash
orcaagent template
```

#### Create Project Using Existing Templates
1. `orcaagent new [PATH] [TEMPLATE]`
2. You can also use `orcaagent new` command for interactive template selection

#### Debug and Development
Start lightweight local server for debugging:
```bash
orcaagent dev
```

#### Start Complete OrcaAgent Service with Local Docker
*Requires Docker installed and running locally*
```bash
orcaagent up
```

#### Generate Dockerfile
```bash
orcaagent dockerfile [SAVE_PATH]
```
Example: `orcaagent dockerfile Dockerfile`

#### Generate Dockerfile and docker-compose.yml
```bash
orcaagent dockerfile --config [CONFIG] --add-docker-compose ./Dockerfile
```
Example: `orcaagent dockerfile --config orcaagent.json --add-docker-compose ./Dockerfile`

#### Package and Build Image
```bash
orcaagent build --tag [TAG TEXT]
```
Example: `orcaagent build --tag my-agent`

## 🔧 Custom Configuration

### 1. Add MCP Server

Add or remove MCP Servers in `src/react_agent/mcp_server_configs.py`:

```python
MCP_SERVERS = {
        "math": {
            "command": "python",
            # Make sure to update to the full absolute path to your math_server.py file
            "args": ["/path/to/math_server.py"],
            "transport": "stdio",
        },
        "weather": {
            # Make sure you start your weather server on port 8000
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http",
        }
    }
```

### 2. Add New Tools

Extend Agent functionality in `src/react_agent/tools.py`:

```python
from langchain.tools import tool

@tool
def custom_tool(query: str) -> str:
    """Custom tool description"""
    # Tool implementation logic
    return result
```

### 3. Choose Different Models

Select compatible chat models through runtime context:
```python
# Example: Use OpenAI GPT-4
model = "openai/gpt-4-turbo-preview"

# Example: Use self-deployed model compatible with OpenAI protocol
model = "compatible_openai/DeepSeek-V3-0324"
```

### 4. Custom Prompts

Update system prompts in `src/react_agent/prompts.py`:

```python
SYSTEM_PROMPT = """
You are a professional AI assistant specialized in handling...
"""
```

### 5. Modify Reasoning Flow

Adjust Agent's reasoning process in `src/react_agent/graph.py`:
- Modify ReAct loop
- Add additional decision steps
- Customize nodes and edges

## 📁 Project Structure

```
react-agent/
├── src/
│   ├── common/           # Common utilities and configurations
│   └── react_agent/      # React Agent core code
│       ├── graph.py      # Graph structure definition
│       ├── tools.py      # Tool definitions
│       ├── prompts.py    # Prompt templates
│       └── main.py       # Main entry point
├── static/               # Static resources
├── tests/                # Test files
│   ├── unit_tests/       # Unit tests
│   └── integration_tests/ # Integration tests
├── .env.example          # Environment configuration example
└── README.md
```

## 🧪 Development and Debugging

### Local Development

When iterating on graph structure, you can:
- Edit past states and rerun the application from past states
- Use hot reload to automatically apply local changes
- Add breakpoints before Agent calls tools
- Update default system messages to adopt specific roles
- Add additional nodes and edges

### Create New Thread

Use the `+` button in the top right corner to create a brand new thread, clearing previous history.

## 📚 Related Resources

- [LangGraph Documentation](https://github.com/langchain-ai/langgraph)

## 🤝 Contributing

We welcome community contributions! Please follow these steps:

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support and Feedback

For questions or suggestions, please:
- Submit an [Issue](https://github.com/OrcaAgent-AI/react-agent/issues)
- Send email to: jubaoliang@gmail.com
- Join our community discussion group
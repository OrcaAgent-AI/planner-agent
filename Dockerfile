# Use the official LangGraph API image as base
FROM langchain/langgraph-api:3.11

# =====================================
# Configure Package Mirrors (China)
# =====================================

# Configure pip to use Tencent Cloud mirror
RUN pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple && \
    pip config set global.trusted-host mirrors.cloud.tencent.com

# Configure uv to use Tencent Cloud mirror
ENV UV_INDEX_URL=https://mirrors.cloud.tencent.com/pypi/simple
ENV UV_TRUSTED_HOST=mirrors.cloud.tencent.com

# Alternative: Use Tsinghua University mirror (uncomment if needed)
# RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
#     pip config set global.trusted-host pypi.tuna.tsinghua.edu.cn
# ENV UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple
# ENV UV_TRUSTED_HOST=pypi.tuna.tsinghua.edu.cn

# =====================================
# Install Local Dependencies
# =====================================

# Add the local planner-agent package to the container
ADD . /deps/planner-agent

# Install all local dependencies found in /deps directory
RUN for dep in /deps/*; do \
    echo "Installing $dep"; \
    if [ -d "$dep" ]; then \
        echo "Installing $dep"; \
        (cd "$dep" && PYTHONDONTWRITEBYTECODE=1 uv pip install --system --no-cache-dir -c /api/constraints.txt -e .); \
    fi; \
done

# =====================================
# Environment Configuration
# =====================================

# Set LangGraph HTTP application path
ENV LANGGRAPH_HTTP='{"app": "/deps/planner-agent/src/planner_agent/app.py:app"}'

# Set LangServe graphs configuration
ENV LANGSERVE_GRAPHS='{"agent": "/deps/planner-agent/src/planner_agent/graph.py:graph"}'

# =====================================
# Ensure Core Dependencies
# =====================================

# Ensure user dependencies didn't inadvertently overwrite langgraph-api components
RUN mkdir -p /api/langgraph_api /api/langgraph_runtime /api/langgraph_license && \
    touch /api/langgraph_api/__init__.py /api/langgraph_runtime/__init__.py /api/langgraph_license/__init__.py

# Reinstall langgraph-api to ensure it's not overwritten
RUN PYTHONDONTWRITEBYTECODE=1 uv pip install --system --no-cache-dir --no-deps -e /api

# =====================================
# Cleanup Build Dependencies
# =====================================

# Remove pip, setuptools, and wheel from system
RUN pip uninstall -y pip setuptools wheel && \
    rm -rf /usr/local/lib/python*/site-packages/pip* \
           /usr/local/lib/python*/site-packages/setuptools* \
           /usr/local/lib/python*/site-packages/wheel* && \
    find /usr/local/bin -name "pip*" -delete || true && \
    rm -rf /usr/lib/python*/site-packages/pip* \
           /usr/lib/python*/site-packages/setuptools* \
           /usr/lib/python*/site-packages/wheel* && \
    find /usr/bin -name "pip*" -delete || true && \
    uv pip uninstall --system pip setuptools wheel && \
    rm /usr/bin/uv /usr/bin/uvx

# =====================================
# Set Working Directory
# =====================================

WORKDIR /deps/planner-agent
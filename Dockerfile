## Stage 1: Build Stage with Dependencies
FROM python:3.12-slim AS builder

## https://github.com/users/nnthanh101/packages/container/package/runbooks
LABEL org.opencontainers.image.source https://github.com/nnthanh101/runbooks

## Update base image and install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git curl \
    && rm -rf /var/lib/apt/lists/*
## Install UV as package manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

## Set working directory
WORKDIR /app

## Install the project without the the source code (only dependencies)
## Cache dependencies for faster builds
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev --compile-bytecode

## Copy source code & Install the project's source packages
ADD .python-version pyproject.toml uv.lock src/ /app/

RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install --compile-bytecode .

## Run tests during the build phase
# COPY tests/ /tests/
# RUN pytest -v /tests

## Stage 2 - Production Stage: Use alpine for the final image to reduce the total size
FROM python:3.12-alpine AS prod

## Copy the installed environment from builder (built artifacts and dependencies)
COPY --from=builder --chown=app:app /app /app

## Set working directory
WORKDIR /app

## Configure PATH for executables, packages are in the /app/.venv folder
ENV PATH="/app/.venv/bin:$PATH"

## Run command
CMD ["python", "main.py"]

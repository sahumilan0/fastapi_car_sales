# Use Python 3.10 slim base image for smaller size and cross-platform compatibility
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false

# Add Poetry to PATH
ENV PATH="$POETRY_HOME/bin:$PATH"

# Install system dependencies and Poetry
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        build-essential \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create false \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY pyproject.toml poetry.lock ./

# Install project dependencies
RUN poetry install --no-dev --no-root

# Create and set permissions for SQLite database directory
RUN mkdir -p /data && \
    chown -R nobody:nogroup /data && \
    chmod 777 /data

# Copy the application code
COPY app/ ./app/
RUN chown -R nobody:nogroup /app

# Set non-root user for security
USER nobody

# Create SQLite database directory at runtime
RUN mkdir -p /data/db

# Create volume for persistent SQLite database
VOLUME ["/data"]

# Expose the port the app runs on
EXPOSE 8000

# Add healthcheck
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/ || exit 1

# Command to run the application
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

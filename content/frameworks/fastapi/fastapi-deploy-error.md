---
title: "[Solution] FastAPI Deploy Error -- How to Fix"
description: "Fix FastAPI deployment errors. Resolve production server, container, and hosting configuration issues."
frameworks: ["fastapi"]
error-types: ["deployment-error"]
severities: ["error"]
weight: 5
comments: true
---

A FastAPI deploy error occurs when the application fails to deploy to production due to server configuration, environment issues, or container problems.

## Why It Happens

Deployment errors stem from missing environment variables, incorrect ASGI server configuration, Docker build failures, or missing dependencies.

## Common Error Messages

```
uvicorn.error: Invalid proxy header
```

```
docker.errors.BuildError: Failed to build image
```

```
ModuleNotFoundError: No module named 'uvicorn'
```

```
gunicorn.error: Worker timeout exceeded
```

## How to Fix It

### 1. Configure Uvicorn for Production

Set up Uvicorn with proper settings.

```bash
uvicorn main:app \
    --host 0.0.0.0 \
    --port 8000 \
    --workers 4 \
    --limit-concurrency 1000 \
    --timeout-keep-alive 30 \
    --access-log \
    --log-level info
```

### 2. Use Gunicorn with Uvicorn Workers

Set up Gunicorn for production.

```bash
gunicorn main:app \
    -w 4 \
    -k uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -
```

### 3. Create Dockerfile

Set up Docker for deployment.

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
```

### 4. Configure Environment Variables

Set up all required env vars.

```python
import os
from fastapi import FastAPI

app = FastAPI(
    title=os.getenv('APP_TITLE', 'My API'),
    debug=os.getenv('DEBUG', 'false').lower() == 'true',
    docs_url=None if os.getenv('ENV') == 'production' else '/docs'
)
```

## Common Scenarios

**Scenario 1: Worker timeout in production.**
Increase timeout and check for slow endpoints.

**Scenario 2: Docker build fails.**
Check requirements.txt and Python version.

**Scenario 3: Module not found in container.**
Ensure all dependencies are in requirements.txt.

## Prevent It

1. **Use multi-stage Docker builds.**
Keep image size small.

2. **Set health check endpoints.**
Add `/health` endpoint.

3. **Use environment variables.**
Never hardcode production values.


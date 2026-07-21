---
title: "[Solution] FastAPI Gunicorn Uvicorn Worker Error"
description: "Fix FastAPI gunicorn uvicorn worker errors when running production ASGI servers with incorrect configurations."
frameworks: ["fastapi"]
error-types: ["deployment-error"]
severities: ["error"]
---

When deploying FastAPI with Gunicorn using Uvicorn workers, configuration mismatches cause startup failures.

## Common Causes

- Using the default sync worker class instead of `uvicorn.workers.UvicornWorker`
- Not specifying enough workers for concurrent request handling
- Mismatched `--workers` and `--threads` flags with async application
- Forgetting to install `uvicorn[standard]` for WebSocket support
- Environment variables not passed through to worker processes

## How to Fix

### Use the Uvicorn Worker Class

```bash
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Create a Gunicorn Config File

```python
# gunicorn_conf.py
bind = "0.0.0.0:8000"
workers = 4
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 120
keepalive = 5
accesslog = "-"
errorlog = "-"
```

### Use Docker for Process Management

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
```

## Examples

```bash
# Wrong -- sync worker does not support async
gunicorn main:app -w 4

# Correct -- use UvicornWorker
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

Install the required packages:

```bash
pip install gunicorn uvicorn[standard]
```

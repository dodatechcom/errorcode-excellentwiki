---
title: "[Solution] FastAPI Celery Integration Error"
description: "Fix FastAPI Celery integration errors when tasks fail to execute or results are not returned properly."
frameworks: ["fastapi"]
error-types: ["integration-error"]
severities: ["error"]
---

Integrating Celery with FastAPI requires proper broker configuration, task serialization settings, and result backend setup.

## Common Causes

- Celery broker URL does not match Redis or RabbitMQ configuration
- Task serialization format mismatch between worker and client
- Result backend not configured, so `task.get()` returns None
- FastAPI startup event does not initialize Celery properly
- Task functions import heavy modules that cause worker startup failures

## How to Fix

### Configure Celery with FastAPI

```python
from celery import Celery
from fastapi import FastAPI

celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1",
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    result_expires=3600,
)

app = FastAPI()

@celery_app.task
def process_data(data: dict) -> dict:
    return {"processed": True, **data}

@app.post("/submit")
def submit_task(data: dict):
    task = process_data.delay(data)
    return {"task_id": task.id}

@app.get("/status/{task_id}")
def get_status(task_id: str):
    result = celery_app.AsyncResult(task_id)
    return {"status": result.status, "result": result.result}
```

### Use Task Routes for Queue Management

```python
celery_app.conf.task_routes = {
    "worker.process_heavy": {"queue": "heavy"},
    "worker.send_email": {"queue": "emails"},
}
```

## Examples

```python
from celery import Celery

# Bug -- pickle serialization is insecure
celery = Celery("worker", broker="redis://localhost:6379/0")
celery.conf.update(
    task_serializer="pickle",
    accept_content=["pickle"],
)

# Fix -- use JSON serialization
celery = Celery("worker", broker="redis://localhost:6379/0")
celery.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
)
```

Start the Celery worker with: `celery -A worker.celery_app worker --loglevel=info`.

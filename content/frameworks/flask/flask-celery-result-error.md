---
title: "[Solution] Flask Celery Result Error"
description: "Fix Flask Celery result errors when task results are not stored or returned correctly."
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
---

Celery result errors occur when task results are not properly stored in the backend or when the result backend is not configured.

## Common Causes

- Result backend not configured
- Redis or database backend not running
- Task result expires before client retrieves it
- Result serialization format mismatch
- Backend connection pool exhausted

## How to Fix

### Configure Result Backend

```python
from celery import Celery

celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1",
)

celery.conf.update(
    result_expires=3600,
    result_serializer="json",
    accept_content=["json"],
)
```

### Store and Retrieve Results

```python
from celery.result import AsyncResult

@celery.task
def compute(x, y):
    return x + y

# In Flask route
@app.route("/compute/<int:x>/<int:y>")
def compute_route(x, y):
    task = compute.delay(x, y)
    return {"task_id": task.id}

@app.route("/result/<task_id>")
def get_result(task_id):
    result = AsyncResult(task_id)
    return {
        "task_id": task_id,
        "status": result.status,
        "result": result.result,
    }
```

### Handle Result Failures

```python
@app.route("/result/<task_id>")
def get_result(task_id):
    result = AsyncResult(task_id)
    if result.ready():
        if result.successful():
            return {"status": "success", "result": result.result}
        else:
            return {"status": "failed", "error": str(result.result)}
    return {"status": "pending"}
```

## Examples

```python
from celery import Celery

# Bug -- no result backend
celery = Celery("tasks", broker="redis://localhost:6379/0")
# result.get() will hang forever

# Fix -- add result backend
celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1",
)
```

---
title: "[Solution] Flask Celery Task Error"
description: "Fix Flask Celery task errors when asynchronous tasks fail, hang, or produce incorrect results."
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
---

Celery task errors occur when tasks fail silently, have incorrect serialization, or are not properly configured with the Flask application.

## Common Causes

- Task function raises unhandled exception
- Task not registered with Celery
- Broker connection lost during task execution
- Task result backend not configured
- Flask application context not available in task

## How to Fix

### Define Tasks Properly

```python
from celery import Celery

celery = Celery(app.name, broker=app.config["CELERY_BROKER_URL"])
celery.conf.update(app.config)

@celery.task(bind=True)
def send_email(self, user_id, subject, body):
    try:
        user = User.query.get(user_id)
        # Send email
        return {"status": "sent"}
    except Exception as exc:
        self.retry(exc=exc, countdown=60)
```

### Handle Task Failures

```python
@celery.task
def process_data(data):
    try:
        result = transform(data)
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "error": str(e)}
```

### Monitor Task Status

```python
@app.route("/task/<task_id>")
def task_status(task_id):
    result = celery.AsyncResult(task_id)
    return {
        "task_id": task_id,
        "status": result.status,
        "result": result.result,
    }
```

## Examples

```python
from celery import Celery

celery = Celery("tasks", broker="redis://localhost:6379/0")

# Bug -- no error handling
@celery.task
def broken_task(data):
    return transform(data)  # May raise exception

# Fix -- add error handling
@celery.task
def working_task(data):
    try:
        return transform(data)
    except Exception as e:
        return {"error": str(e)}
```

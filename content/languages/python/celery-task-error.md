---
title: "[Solution] Celery Task Execution Failed Fix"
description: "Fix Celery task execution failed errors. Handle task exceptions, configure error handling, and implement retry logic."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Celery Task Execution Failed Fix

A Celery `task execution failed` error occurs when a worker cannot complete a task due to an unhandled exception, serialization issue, or worker configuration problem.

## What This Error Means

Common messages:

- `celery.exceptions.TaskRevokedError`
- `Task [task_name] raised unexpected: <Exception>`
- `WorkerLostError: Worker exited prematurely: signal 15 (SIGTERM)`

The Celery worker received a task but failed to execute it successfully. The task may have raised an exception, the worker may have been killed, or the result could not be serialized.

## Common Causes

```python
# Cause 1: Unhandled exception in task
from celery import Celery

app = Celery("tasks", broker="redis://localhost:6379/0")

@app.task
def process_data(data):
    result = data["key"]  # KeyError if "key" missing

process_data.delay({"wrong": "key"})  # Task fails

# Cause 2: Task result exceeds backend size limit
@app.task
def huge_result():
    return "x" * 10_000_000  # Too large for Redis backend

# Cause 3: Task serialization error
@app.task
def non_serializable():
    return lambda x: x  # Lambda cannot be pickled

# Cause 4: Worker killed or OOM
@app.task
def memory_hog():
    return [0] * 100_000_000  # Worker killed by OOM
```

## How to Fix

### Fix 1: Add task-level error handling

```python
from celery import Celery
from celery.exceptions import MaxRetriesExceededError

app = Celery("tasks", broker="redis://localhost:6379/0")

@app.task(bind=True, max_retries=3)
def process_data(self, data):
    try:
        return data["key"]
    except KeyError as exc:
        self.retry(exc=exc, countdown=60)
```

### Fix 2: Configure task acknowledgment and reject on failure

```python
app.conf.update(
    task_acks_late=True,
    task_reject_on_worker_lost=True,
    task_track_started=True,
)
```

### Fix 3: Set result backend expiration

```python
app.conf.update(
    result_expires=3600,
    result_backend_transport_options={"max_size": 1048576},
)
```

### Fix 4: Use serializer that handles more types

```python
app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
)
```

### Fix 5: Monitor failed tasks

```python
from celery.signals import task_failure

@task_failure.connect
def handle_task_failure(sender, task_id, exception, traceback, **kwargs):
    print(f"Task {sender.name}[{task_id}] failed: {exception}")
    # Send alert, log to monitoring system, etc.
```

## Related Errors

- {{< relref "celery-timeout-error" >}} — Celery task timeout after specified seconds.
- {{< relref "memoryerror" >}} — Python out-of-memory error.

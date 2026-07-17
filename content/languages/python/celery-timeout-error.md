---
title: "[Solution] Celery Task Timeout After 300s Fix"
description: "Fix Celery task timeout when tasks exceed time limit. Optimize slow tasks, configure timeouts, and use asynchronous patterns."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Celery Task Timeout Fix

A Celery task timeout error occurs when a task runs longer than the configured `task_time_limit` or `task_soft_time_limit`, causing the worker to terminate or raise a `SoftTimeLimitExceeded` exception.

## What This Error Means

Common messages:

- `celery.exceptions.SoftTimeLimitExceeded`
- `Task [task_name] timed out (300s)`
- `WorkerLostError: Worker exited prematurely: signal 9 (SIGKILL)`

The task exceeded the configured time limit. The soft limit raises an exception that the task can catch, while the hard limit kills the worker process.

## Common Causes

```python
from celery import Celery

app = Celery("tasks", broker="redis://localhost:6379/0")

# Cause 1: Slow external API call blocks the task
@app.task
def fetch_data(url):
    import requests
    return requests.get(url, timeout=300)  # If API is slow, exceeds limit

# Cause 2: Large database query without pagination
@app.task
def process_all_users():
    users = User.objects.all()  # 10M rows
    for user in users:  # Takes hours
        process(user)

# Cause 3: Infinite loop or deadlock
@app.task
def stuck_task():
    while True:
        pass  # Never completes

# Cause 4: Soft time limit too aggressive
app.conf.update(task_soft_time_limit=300)
```

## How to Fix

### Fix 1: Set appropriate time limits

```python
app.conf.update(
    task_time_limit=600,        # Hard limit: 10 minutes (kills worker)
    task_soft_time_limit=300,   # Soft limit: 5 minutes (raises exception)
)
```

### Fix 2: Catch SoftTimeLimitExceeded for cleanup

```python
from celery.exceptions import SoftTimeLimitExceeded

@app.task(bind=True)
def process_data(self, data):
    try:
        result = long_running_operation(data)
        return result
    except SoftTimeLimitExceeded:
        self.update_state(state="TIMEOUT")
        cleanup_partial_results()
        raise
```

### Fix 3: Break large tasks into smaller chunks

```python
from celery import group

@app.task
def process_chunk(chunk):
    return [process(item) for item in chunk]

def process_all_users():
    chunks = [users[i:i+1000] for i in range(0, len(users), 1000)]
    job = group(process_chunk.s(chunk) for chunk in chunks)
    result = job.apply_async()
```

### Fix 4: Use async HTTP calls instead of blocking

```python
import httpx

@app.task
def fetch_data(url):
    with httpx.Client(timeout=30) as client:
        return client.get(url).json()
```

### Fix 5: Monitor long-running tasks

```python
from celery.signals import task_prerun, task_postrun
import time

@task_prerun.connect
def task_start(sender, **kwargs):
    kwargs["kwargs"]["_start_time"] = time.time()

@task_postrun.connect
def task_end(sender, **kwargs):
    duration = time.time() - kwargs["kwargs"].get("_start_time", 0)
    if duration > 60:
        print(f"Slow task: {sender.name} took {duration:.1f}s")
```

## Related Errors

- {{< relref "celery-task-error" >}} — Celery task execution failed.
- {{< relref "timeouterror" >}} — Python TimeoutError.

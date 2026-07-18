---
title: "[Solution] Python Celery Worker Error — How to Fix"
description: "Fix Python Celery worker errors. Resolve worker crashes, task failures, and monitoring issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Celery Worker Error

A `celery.WorkerLostError` occurs when Celery workers fail to process tasks due to resource exhaustion, import errors, or configuration issues..

## Why It Happens

This happens when workers run out of memory, task code has import errors, or workers cannot serialize results. Python enforces strict type and state checking.

## Common Error Messages

- `Worker exited prematurely`
- `Task was revoked`
- `exceeded max retries`
- `connection refused`

## How to Fix It

### Fix 1: Configure worker resources

```python
celery -A app worker --concurrency=4 --max-tasks-per-child=1000 --loglevel=info
```

### Fix 2: Handle worker crashes

```python
from celery import shared_task

@shared_task(bind=True)
def safe_task(self):
    try:
        return do_work()
    except Exception as exc:
        self.retry(exc=exc, countdown=60)
```

### Fix 3: Monitor worker health

```python
# celeryconfig.py
worker_prefetch_multiplier = 1
task_acks_late = True
task_reject_on_worker_lost = True
```

### Fix 4: Handle memory leaks

```python
celery -A app worker --max-tasks-per-child=100 --max-memory-per-child=200000
```

## Common Scenarios

- **Memory leaks** — Tasks accumulate memory over time causing OOM.
- **Task timeouts** — Long-running tasks exceed configured time limits.
- **Worker restarts** — Workers crash and lose in-flight tasks.

## Prevent It

- Set max-tasks-per-child to recycle workers
- Use task_acks_late = True to prevent message loss
- Monitor workers with flower or custom health checks

## Related Errors

- - [OperationalError](/languages/python/operationalerror/) — database operation failed
- - [TimeoutError](/languages/python/timeouterror/) — operation timed out
- - [Redis ConnectionError](/languages/python/redis-connection-error/) — broker connection failed

---
title: "[Solution] Python Celery Task Queue Error — How to Fix"
description: "Fix Python Celery task queue errors. Resolve worker, broker, and task execution issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Celery Task Queue Error

A `celery.exceptions.CeleryError` or `celery.exceptions.TaskRevokedError` occurs when Celery fails to enqueue tasks, when workers crash, or when the broker connection is lost.

## Why It Happens

Celery is a distributed task queue. Errors arise when the broker (Redis/RabbitMQ) is unavailable, when tasks raise unhandled exceptions, when workers run out of memory, or when result backends are not configured.

## Common Error Messages

- `ConnectionError: Error connecting to redis://localhost:6379`
- `TaskRevokedError: Task was revoked`
- `MaxRetriesExceededError: Can't retry`
- `OperationalError: connection already closed`

## How to Fix It

### Fix 1: Configure Celery properly

```python
from celery import Celery

# Wrong — minimal configuration
# app = Celery('tasks', broker='redis://localhost')

# Correct — comprehensive configuration
app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1",
)

app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_acks_late=True,
    worker_prefetch_multiplier=1,
    task_reject_on_worker_lost=True,
    task_soft_time_limit=300,
    task_time_limit=600,
)
```

### Fix 2: Handle task errors

```python
from celery import shared_task
from celery.exceptions import MaxRetriesExceededError

# Wrong — no retry handling
# @app.task
# def process_data(data):
#     return transform(data)

# Correct — handle retries
@shared_task(
    bind=True,
    max_retries=3,
    default_retry_delay=60,
    autoretry_for=(ConnectionError, TimeoutError),
    retry_backoff=True,
    retry_backoff_max=600,
    retry_jitter=True,
)
def process_data(self, data):
    try:
        result = transform(data)
        return result
    except Exception as exc:
        self.retry(exc=exc)

@shared_task
def send_email(user_id, message):
    try:
        do_send_email(user_id, message)
    except Exception as e:
        print(f"Email failed: {e}")
        raise
```

### Fix 3: Monitor worker health

```python
# celeryconfig.py
broker_url = "redis://localhost:6379/0"
result_backend = "redis://localhost:6379/1"

# Worker configuration
worker_prefetch_multiplier = 1
task_acks_late = True
task_reject_on_worker_lost = True
task_soft_time_limit = 300
task_time_limit = 600

# Event settings for monitoring
worker_send_task_events = True
task_send_sent_event = True
```

```bash
# Start worker with monitoring
celery -A app worker --loglevel=info --concurrency=4
celery -A app flower  # web-based monitoring
```

### Fix 4: Handle result expiration

```python
from celery import Celery

app = Celery("tasks", broker="redis://localhost:6379/0", backend="redis://localhost:6379/1")

app.conf.update(
    result_expires=3600,  # results expire after 1 hour
    result_persistent=True,  # persist results to disk
    result_backend_transport_options={"master_name": "mymaster"},
)

@app.task
def compute(x, y):
    return x + y

# Check result with timeout
result = compute.delay(4, 4)
try:
    value = result.get(timeout=10)
    print(f"Result: {value}")
except celery.exceptions.TimeoutError:
    print("Task still running")
```

## Common Scenarios

- **Worker crash** — Worker process runs out of memory and terminates.
- **Broker connection lost** — Redis or RabbitMQ server restarts, disconnecting workers.
- **Task timeout** — Long-running task exceeds soft or hard time limit.

## Prevent It

- Always set `task_acks_late=True` to prevent message loss when workers crash.
- Use `autoretry_for` with exponential backoff for transient failures.
- Monitor workers with Flower or custom health checks.

## Related Errors

- [ConnectionError](/languages/python/connectionerror/) — broker connection failed
- [TaskRevokedError](/languages/python/task-revoked/) — task was cancelled
- [MaxRetriesExceededError](/languages/python/max-retries/) — retry limit exceeded

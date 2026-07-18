---
title: "[Solution] FastAPI Celery Error — How to Fix"
description: "Fix FastAPI Celery errors. Resolve worker failures, task serialization issues, and broker connection problems."
frameworks: ["fastapi"]
error-types: ["background-error"]
severities: ["error"]
weight: 5
comments: true
---

A FastAPI Celery error occurs when Celery workers fail to execute tasks, connect to the broker, or serialize arguments correctly.

## Why It Happens

Celery errors happen due to broker connection failures, incorrect serialization, missing dependencies, or worker crashes.

## Common Error Messages

```
celery.exceptions.InvalidTaskSignature: Task signature error
```

```
kombu.exceptions.OperationalError: Error connecting to broker
```

```
celery.exceptions.MaxRetriesExceededError: Max retries exceeded
```

```
billiard.exceptions.TaskRevokedError: Task revoked
```

## How to Fix It

### 1. Configure Celery Properly

Set up Celery with FastAPI.

```python
from celery import Celery

app_celery = Celery(
    'worker',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/1'
)

app_celery.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_track_started=True,
    task_time_limit=300,
    task_soft_time_limit=270
)

@app_celery.task(bind=True, max_retries=3)
def process_data(self, data_id):
    try:
        data = fetch_data(data_id)
        result = process(data)
        return result
    except Exception as exc:
        self.retry(exc=exc, countdown=60)
```

### 2. Handle Task Failures

Add error handling and retries.

```python
@app_celery.task(bind=True, max_retries=3, default_retry_delay=60)
def send_notification(self, user_id, message):
    try:
        user = get_user(user_id)
        send_email(user.email, message)
    except SMTPException as exc:
        logger.error(f'Email failed: {exc}')
        self.retry(exc=exc)
    except Exception as exc:
        logger.error(f'Notification failed: {exc}')
        raise
```

### 3. Monitor Celery Workers

Track worker status and tasks.

```python
from celery.app.control import Control

control = Control(app_celery)

# Inspect active tasks
active = control.active()

# Inspect registered tasks
registered = control.registered()

# Inspect stats
stats = control.stats()
```

### 4. Implement Task Chaining

Chain tasks for complex workflows.

```python
from celery import chain, group, chord

# Chain tasks sequentially
workflow = chain(
    fetch_data.s(data_id),
    process_data.s(),
    store_result.s()
)
result = workflow.apply_async()

# Group parallel tasks
parallel = group(process_item.s(item) for item in items)
result = parallel.apply_async()
```

## Common Scenarios

**Scenario 1: Celery worker won't start.**
Check broker connection and dependencies.

**Scenario 2: Task stuck in PENDING.**
Ensure worker is running and task is registered.

**Scenario 3: Task serialization error.**
Use JSON serialization consistently.

## Prevent It

1. **Use JSON serialization.**
Configure task_serializer='json'.

2. **Monitor worker health.**
Set up Flower dashboard.

3. **Set task time limits.**
Prevent stuck tasks.


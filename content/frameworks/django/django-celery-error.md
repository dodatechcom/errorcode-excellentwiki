---
title: "[Solution] Django Celery Task Error"
description: "Fix Django Celery task errors. Resolve Celery worker and task execution issues."
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["celery", "task", "worker", "broker", "django"]
weight: 5
---

A Django Celery error occurs when Celery tasks fail to execute. This can be caused by broker connectivity issues, task errors, or worker misconfiguration.

## Common Causes

- Celery broker (Redis/RabbitMQ) is not running
- Worker not started or crashed
- Task has syntax errors or exceptions
- Result backend not configured
- Serialization format mismatch

## How to Fix

### Check Broker Settings

```python
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
```

### Start Celery Worker

```bash
celery -A myproject worker -l info
```

### Check Task Status

```python
result = my_task.delay(arg1, arg2)
result.status  # PENDING, STARTED, SUCCESS, FAILURE
result.get(timeout=10)
```

### Monitor Celery

```bash
celery -A myproject flower
```

### Check Worker Logs

```bash
celery -A myproject worker -l debug
```

### Test Task

```python
@shared_task
def add(x, y):
    return x + y

result = add.delay(4, 4)
print(result.get())  # 8
```

## Examples

```python
# Example 1: Broker not running
# ConnectionRefusedError: Error connecting to localhost:6379
# Fix: start Redis service

# Example 2: Task exception
@app.task
def process_data(data):
    raise ValueError("Invalid data")
# Fix: handle exception in task
```

## Related Errors

- [Django Redis Error]({{< relref "/frameworks/django/django-redis-error" >}}) — Redis connection error
- [Django Signal Error]({{< relref "/frameworks/django/django-signal-error" >}}) — signal handler error

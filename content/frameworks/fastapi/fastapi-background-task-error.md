---
title: "[Solution] FastAPI Background Task Error -- How to Fix"
description: "Fix FastAPI background task errors. Resolve task execution failures and cleanup issues."
frameworks: ["fastapi"]
error-types: ["background-error"]
severities: ["error"]
weight: 5
comments: true
---

A FastAPI background task error occurs when tasks fail to execute, are lost during shutdown, or cause resource leaks.

## Why It Happens

Background task errors happen due to missing dependencies, incorrect async handling, or tasks accessing closed resources.

## Common Error Messages

```
RuntimeError: Task was destroyed but it is pending
```

```
AttributeError: 'NoneType' object has no attribute 'execute'
```

```
asyncio.CancelledError: Task was cancelled
```

```
RuntimeError: Event loop is closed
```

## How to Fix It

### 1. Add Background Tasks to Endpoints

Use FastAPI's built-in BackgroundTasks.

```python
from fastapi import BackgroundTasks

def send_email(email: str, message: str):
    # Send email logic
    pass

@app.post('/send-notification/')
async def send_notification(background_tasks: BackgroundTasks, email: str, message: str):
    background_tasks.add_task(send_email, email, message)
    return {'message': 'Notification queued'}
```

### 2. Handle Task Exceptions

Add error handling to tasks.

```python
def process_data(data: dict):
    try:
        result = heavy_computation(data)
        save_result(result)
    except Exception as e:
        logger.error(f'Background task failed: {e}')
```

### 3. Use Task Dependencies

Ensure tasks have proper dependencies.

```python
@app.post('/process/')
async def process(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    users = db.query(User).all()
    background_tasks.add_task(process_users, users)
    return {'status': 'processing'}
```

### 4. Implement Task Retry Logic

Add retry mechanism.

```python
import asyncio

async def retry_task(func, *args, max_retries=3, delay=1):
    for attempt in range(max_retries):
        try:
            await func(*args)
            return
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            await asyncio.sleep(delay * (attempt + 1))
```

## Common Scenarios

**Scenario 1: Task loses database session.**
Pass data, not session objects.

**Scenario 2: Task fails silently.**
Add logging and error handling.

**Scenario 3: Tasks pile up under load.**
Use Celery for heavy workloads.

## Prevent It

1. **Use BackgroundTasks for light work.**
Use Celery for heavy tasks.

2. **Log all task executions.**
Track success/failure rates.

3. **Set task timeouts.**
Prevent indefinite execution.


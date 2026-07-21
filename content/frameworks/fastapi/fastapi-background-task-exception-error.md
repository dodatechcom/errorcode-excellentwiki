---
title: "[Solution] FastAPI Background Task Exception Error"
description: "Fix FastAPI background task exception errors when tasks fail silently or raise unhandled errors after response."
frameworks: ["fastapi"]
error-types: ["runtime-error"]
severities: ["error"]
---

When a `BackgroundTask` raises an exception, the error is logged but not returned to the client since the response has already been sent.

## Common Causes

- Background task function raises an unhandled exception
- Database session is closed before background task completes
- External service call in background task fails without retry logic
- Background task depends on request-scoped state that no longer exists
- Multiple background tasks with dependencies execute in wrong order

## How to Fix

### Add Error Handling Inside Background Tasks

```python
from fastapi import FastAPI, BackgroundTasks
import logging

logger = logging.getLogger(__name__)

app = FastAPI()

def send_email(email: str, message: str):
    try:
        print(f"Sending email to {email}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")

@app.post("/subscribe")
def subscribe(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email, "Welcome!")
    return {"message": "Subscribed"}
```

### Use Separate Database Sessions

```python
from sqlalchemy.orm import Session

def process_data(user_id: int):
    db = SessionLocal()
    try:
        user = db.query(User).get(user_id)
        db.commit()
    except Exception as e:
        db.rollback()
        logger.error(f"Background task failed: {e}")
    finally:
        db.close()
```

## Examples

```python
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def unreliable_task(data: str):
    raise RuntimeError("Something went wrong!")

@app.post("/process")
def process(data: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(unreliable_task, data)
    return {"status": "processing"}
```

The RuntimeError will be logged but the client receives `200 OK`. Add try/except and logging inside the task function for proper error tracking.

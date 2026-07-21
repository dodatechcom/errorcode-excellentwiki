---
title: "[Solution] FastAPI Background Tasks Order Error"
description: "Fix FastAPI background tasks order errors when tasks execute in unexpected sequence or parallel."
frameworks: ["fastapi"]
error-types: ["runtime-error"]
severities: ["error"]
---

When multiple background tasks are added to a FastAPI request, they execute sequentially in the order they were added.

## Common Causes

- Tasks added in the wrong order for dependencies
- Task A writes data that Task B needs, but B runs first
- Exception in an early task prevents later tasks from executing
- Tasks added in different parts of the code run in unpredictable order
- Background tasks assume they run in parallel (they do not)

## How to Fix

### Add Tasks in Dependency Order

```python
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(message + "\n")

def send_notification(user_id: int, message: str):
    print(f"Sending to user {user_id}: {message}")

@app.post("/notify")
def notify(user_id: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, f"Notification for user {user_id}")
    background_tasks.add_task(send_notification, user_id, "Hello!")
    return {"status": "queued"}
```

### Use Task Queues for Complex Workflows

```python
from celery import Celery

celery_app = Celery("tasks", broker="redis://localhost:6379/0")

@celery_app.task
def process_data(data):
    return transform(data)

@celery_app.task
def send_result(result):
    notify_user(result)

# Chain tasks
process_data.delay(data).link(send_result.delay)
```

## Examples

```python
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def step_one():
    print("Step 1: Initialize")

def step_two():
    print("Step 2: Process")

@app.post("/run")
def run(background_tasks: BackgroundTasks):
    background_tasks.add_task(step_one)
    background_tasks.add_task(step_two)
    # step_one runs first, then step_two
```

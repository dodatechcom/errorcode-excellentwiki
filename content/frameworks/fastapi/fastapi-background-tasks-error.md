---
title: "[Solution] FastAPI Background Tasks Error"
description: "Tasks not executing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Tasks not executing.

## Common Causes

Not properly registered.

## How to Fix

Use BackgroundTasks.

## Example

```python
from fastapi import BackgroundTasks
@app.post('/send')
async def send(email: str, bg: BackgroundTasks):
    bg.add_task(send_email, email)
    return {'msg': 'Sent'}
```

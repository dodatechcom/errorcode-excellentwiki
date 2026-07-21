---
title: "[Solution] FastAPI Database Session Error"
description: "Session not closing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Session not closing.

## Common Causes

Not using DI.

## How to Fix

Use yield dependency.

## Example

```python
async def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()
```

---
title: "[Solution] FastAPI Dependency Yield Error"
description: "Yield dependency not cleaning up."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Yield dependency not cleaning up.

## Common Causes

Missing finally.

## How to Fix

Use try/finally.

## Example

```python
async def db():
    d = SessionLocal()
    try: yield d
    finally: d.close()
```

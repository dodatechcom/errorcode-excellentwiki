---
title: "[Solution] FastAPI Lifespan Startup Error"
description: "Startup event not running."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Startup event not running.

## Common Causes

Wrong implementation.

## How to Fix

Use asynccontextmanager.

## Example

```python
from contextlib import asynccontextmanager
@asynccontextmanager
async def lifespan(app):
    startup()
    yield
    shutdown()
```

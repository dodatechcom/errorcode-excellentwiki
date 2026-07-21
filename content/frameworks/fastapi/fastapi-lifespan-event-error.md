---
title: "[Solution] FastAPI Lifespan Event Error"
description: "Lifespan not firing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Lifespan not firing.

## Common Causes

Wrong signature.

## How to Fix

Use async generator.

## Example

```python
from contextlib import asynccontextmanager
@asynccontextmanager
async def lifespan(app):
    yield
app = FastAPI(lifespan=lifespan)
```

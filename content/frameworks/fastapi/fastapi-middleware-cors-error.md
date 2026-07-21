---
title: "[Solution] FastAPI Middleware CORS Error"
description: "CORS middleware not working."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

CORS middleware not working.

## Common Causes

Wrong order.

## How to Fix

Add first.

## Example

```python
app.add_middleware(CORSMiddleware, allow_origins=['*'])  # add before routes
```

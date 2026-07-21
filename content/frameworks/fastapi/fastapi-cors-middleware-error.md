---
title: "[Solution] FastAPI CORS Middleware Error"
description: "CORS not allowing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

CORS not allowing.

## Common Causes

Not configured.

## How to Fix

Add middleware.

## Example

```python
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])
```

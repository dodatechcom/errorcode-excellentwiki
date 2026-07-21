---
title: "[Solution] FastAPI GZip Middleware Error"
description: "GZip not compressing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

GZip not compressing.

## Common Causes

Not added.

## How to Fix

Add middleware.

## Example

```python
from fastapi.middleware.gzip import GZipMiddleware
app.add_middleware(GZipMiddleware, minimum_size=1000)
```

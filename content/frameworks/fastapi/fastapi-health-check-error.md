---
title: "[Solution] FastAPI Health Check Error"
description: "Health check endpoint failing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Health check endpoint failing.

## Common Causes

Not implemented.

## How to Fix

Add endpoint.

## Example

```python
@app.get('/health')
async def health(): return {'status': 'ok'}
```

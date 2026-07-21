---
title: "[Solution] FastAPI ASGI App Error"
description: "ASGI app not working."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

ASGI app not working.

## Common Causes

Wrong implementation.

## How to Fix

Implement __call__.

## Example

```python
class ASGIApp:
    async def __call__(self, scope, receive, send):
        await send({'type': 'http.response.start', 'status': 200})
```

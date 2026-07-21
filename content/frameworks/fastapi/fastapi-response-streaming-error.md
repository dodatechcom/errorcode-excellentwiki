---
title: "[Solution] FastAPI Response Streaming Error"
description: "Streaming not working."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Streaming not working.

## Common Causes

Wrong usage.

## How to Fix

Use StreamingResponse.

## Example

```python
from fastapi.responses import StreamingResponse
async def gen():
    for i in range(10): yield f'line {i}\n'.encode()
@app.get('/stream')
async def stream(): return StreamingResponse(gen())
```

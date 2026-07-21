---
title: "[Solution] FastAPI Stream Response Error"
description: "StreamingResponse not working."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

StreamingResponse not working.

## Common Causes

Wrong generator.

## How to Fix

Use async generator.

## Example

```python
from fastapi.responses import StreamingResponse
async def gen(): yield b'chunk'
@app.get('/stream')
async def stream(): return StreamingResponse(gen())
```

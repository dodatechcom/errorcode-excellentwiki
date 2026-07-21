---
title: "[Solution] FastAPI Plain Text Response Error"
description: "PlainTextResponse not working."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

PlainTextResponse not working.

## Common Causes

Wrong content.

## How to Fix

Return string.

## Example

```python
from fastapi.responses import PlainTextResponse
@app.get('/t')
async def t(): return PlainTextResponse('Hello')
```

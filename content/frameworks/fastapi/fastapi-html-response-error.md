---
title: "[Solution] FastAPI HTML Response Error"
description: "HTMLResponse not rendering."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

HTMLResponse not rendering.

## Common Causes

Wrong content.

## How to Fix

Return HTML string.

## Example

```python
from fastapi.responses import HTMLResponse
@app.get('/', response_class=HTMLResponse)
async def root(): return '<h1>Hello</h1>'
```

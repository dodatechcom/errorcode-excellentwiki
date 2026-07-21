---
title: "[Solution] FastAPI Redirect Response Error"
description: "RedirectResponse not redirecting."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

RedirectResponse not redirecting.

## Common Causes

Wrong URL.

## How to Fix

Use correct URL.

## Example

```python
from fastapi.responses import RedirectResponse
@app.get('/old')
async def old(): return RedirectResponse('/new')
```

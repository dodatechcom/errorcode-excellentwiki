---
title: "[Solution] FastAPI File Response Error"
description: "FileResponse not sending."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

FileResponse not sending.

## Common Causes

Wrong path.

## How to Fix

Use correct path.

## Example

```python
from fastapi.responses import FileResponse
@app.get('/f')
async def f(): return FileResponse('file.pdf')
```

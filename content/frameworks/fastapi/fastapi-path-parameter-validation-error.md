---
title: "[Solution] FastAPI Path Parameter Validation Error"
description: "Path param validation failing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Path param validation failing.

## Common Causes

Wrong type.

## How to Fix

Use correct type.

## Example

```python
@app.get('/u/{id}')
async def u(id: int): return {'id': id}
```

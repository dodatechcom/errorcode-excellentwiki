---
title: "[Solution] FastAPI Path Parameter Error"
description: "Path parameter failing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Path parameter failing.

## Common Causes

Wrong type annotation.

## How to Fix

Use correct types.

## Example

```python
@app.get('/items/{item_id}')
async def read(item_id: int): return {'id': item_id}
```

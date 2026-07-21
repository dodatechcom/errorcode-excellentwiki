---
title: "[Solution] FastAPI Pagination Error FastAPI"
description: "Pagination not working."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Pagination not working.

## Common Causes

Wrong params.

## How to Fix

Use Query params.

## Example

```python
@app.get('/items')
async def items(skip: int = 0, limit: int = 10):
    return items[skip:skip+limit]
```

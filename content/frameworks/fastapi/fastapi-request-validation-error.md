---
title: "[Solution] FastAPI Request Validation Error"
description: "Request validation failing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Request validation failing.

## Common Causes

Wrong data.

## How to Fix

Fix request data.

## Example

```python
@app.post('/items')
async def create(item: Item): return item
```

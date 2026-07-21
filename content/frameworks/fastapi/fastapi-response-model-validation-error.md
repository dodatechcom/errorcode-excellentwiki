---
title: "[Solution] FastAPI Response Model Validation Error"
description: "Response validation failing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Response validation failing.

## Common Causes

Data mismatch.

## How to Fix

Match model.

## Example

```python
@app.get('/u', response_model=UserOut)
async def u(): return user_data
```

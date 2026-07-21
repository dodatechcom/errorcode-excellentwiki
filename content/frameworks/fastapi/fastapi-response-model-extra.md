---
title: "[Solution] FastAPI Response Model Extra"
description: "Extra fields in response."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Extra fields in response.

## Common Causes

Model has extras.

## How to Fix

Use exclude_unset.

## Example

```python
@app.get('/u', response_model=User, response_model_exclude_unset=True)
```

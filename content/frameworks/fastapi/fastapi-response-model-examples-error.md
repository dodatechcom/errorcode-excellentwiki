---
title: "[Solution] FastAPI Response Model Examples Error"
description: "API docs examples missing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

API docs examples missing.

## Common Causes

Not in model.

## How to Fix

Add examples.

## Example

```python
@app.get('/u', response_model=User, examples=[{'name': 'John'}])
```

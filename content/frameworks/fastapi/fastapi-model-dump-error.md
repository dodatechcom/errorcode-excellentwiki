---
title: "[Solution] FastAPI Model Dump Error"
description: "model_dump not working."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

model_dump not working.

## Common Causes

Wrong method.

## How to Fix

Use model_dump.

## Example

```python
u = User(name='John')
u.model_dump()  # dict
u.model_dump_json()  # JSON string
```

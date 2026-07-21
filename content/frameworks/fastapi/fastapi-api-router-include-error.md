---
title: "[Solution] FastAPI API Router Include Error"
description: "Router include not working."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Router include not working.

## Common Causes

Wrong prefix.

## How to Fix

Set prefix.

## Example

```python
app.include_router(r, prefix='/api', tags=['api'])
```

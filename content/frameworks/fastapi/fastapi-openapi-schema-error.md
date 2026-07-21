---
title: "[Solution] FastAPI OpenAPI Schema Error"
description: "Schema not generating."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Schema not generating.

## Common Causes

Model issue.

## How to Fix

Check definitions.

## Example

```python
@app.get('/schema')
async def schema(): return app.openapi()
```

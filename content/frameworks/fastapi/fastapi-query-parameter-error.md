---
title: "[Solution] FastAPI Query Parameter Error"
description: "Query param validation failing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Query param validation failing.

## Common Causes

Wrong defaults.

## How to Fix

Define correctly.

## Example

```python
@app.get('/search')
async def search(q: str = '', limit: int = 10): return {'q': q}
```

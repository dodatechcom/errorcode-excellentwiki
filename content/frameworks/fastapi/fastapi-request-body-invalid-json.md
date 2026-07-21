---
title: "[Solution] FastAPI Request Body Invalid JSON"
description: "Invalid JSON body."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Invalid JSON body.

## Common Causes

Wrong format.

## How to Fix

Send valid JSON.

## Example

```python
@app.post('/d')
async def d(item: Item): return item
```

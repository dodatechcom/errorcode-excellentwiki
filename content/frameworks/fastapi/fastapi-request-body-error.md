---
title: "[Solution] FastAPI Request Body Error"
description: "Body not parsing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Body not parsing.

## Common Causes

Wrong Pydantic model.

## How to Fix

Match model.

## Example

```python
class Item(BaseModel):
    name: str
    price: float
@app.post('/items')
async def create(item: Item): return item
```

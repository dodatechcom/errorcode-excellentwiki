---
title: "[Solution] FastAPI Form Data Parse Error"
description: "Form data not parsing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Form data not parsing.

## Common Causes

Wrong Content-Type.

## How to Fix

Use form data.

## Example

```python
from fastapi import Form
@app.post('/f')
async def f(name: str = Form(...)):
    return {'name': name}
```

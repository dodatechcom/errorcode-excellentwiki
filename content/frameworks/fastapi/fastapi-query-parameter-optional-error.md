---
title: "[Solution] FastAPI Query Parameter Optional Error"
description: "Optional query param wrong."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Optional query param wrong.

## Common Causes

Not optional.

## How to Fix

Use Optional or None default.

## Example

```python
from typing import Optional
@app.get('/s')
async def s(q: Optional[str] = None): return {'q': q}
```

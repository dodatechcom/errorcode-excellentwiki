---
title: "[Solution] FastAPI Template Not Found"
description: "Jinja2 template missing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Jinja2 template missing.

## Common Causes

Wrong directory.

## How to Fix

Configure directory.

## Example

```python
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory='templates')
```

---
title: "[Solution] FastAPI Static Files Error"
description: "Static files 404."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Static files 404.

## Common Causes

Wrong directory.

## How to Fix

Mount correctly.

## Example

```python
from fastapi.staticfiles import StaticFiles
app.mount('/static', StaticFiles(directory='static'))
```

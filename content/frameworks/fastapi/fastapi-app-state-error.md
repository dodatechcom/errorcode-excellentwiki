---
title: "[Solution] FastAPI App State Error"
description: "App state not persisting."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

App state not persisting.

## Common Causes

Not using app.state.

## How to Fix

Use app.state.

## Example

```python
app.state.db = Database()
```

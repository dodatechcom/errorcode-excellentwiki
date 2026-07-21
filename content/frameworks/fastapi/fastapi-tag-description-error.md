---
title: "[Solution] FastAPI Tag Description Error"
description: "Tag description not showing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Tag description not showing.

## Common Causes

Not configured.

## How to Fix

Set in openapi_tags.

## Example

```python
app.openapi_tags = [{'name': 'users', 'description': 'User operations'}]
```

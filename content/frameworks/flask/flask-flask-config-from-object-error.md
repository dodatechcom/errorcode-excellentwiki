---
title: "[Solution] Flask Flask Config From Object Error"
description: "Config object not loading."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Config object not loading.

## Common Causes

Wrong class.

## How to Fix

Use uppercase.

## Example

```python
class Config:
    SECRET_KEY = 's'
app.config.from_object(Config)
```

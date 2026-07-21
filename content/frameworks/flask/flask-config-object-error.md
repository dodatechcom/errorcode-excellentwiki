---
title: "[Solution] Flask Config Object Error"
description: "Config not loading."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Config not loading.

## Common Causes

Wrong class.

## How to Fix

Use uppercase attrs.

## Example

```python
class Config:
    SECRET_KEY = 's'
app.config.from_object(Config)
```

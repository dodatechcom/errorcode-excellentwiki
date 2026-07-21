---
title: "[Solution] Flask Secret Key Not Set"
description: "Cannot sign cookies."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Cannot sign cookies.

## Common Causes

Not configured.

## How to Fix

Set secret key.

## Example

```python
app.secret_key = os.environ.get('SECRET_KEY')
```

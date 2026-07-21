---
title: "[Solution] Django Secret Key Not Set"
description: "SECRET_KEY not configured."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

SECRET_KEY not configured.

## Common Causes

Missing from settings.

## How to Fix

Set key.

## Example

```python
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
```

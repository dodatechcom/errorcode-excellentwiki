---
title: "[Solution] Django REST Auth Error"
description: "Authentication not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Authentication not working.

## Common Causes

Not configured.

## How to Fix

Configure auth.

## Example

```python
REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication']}
```

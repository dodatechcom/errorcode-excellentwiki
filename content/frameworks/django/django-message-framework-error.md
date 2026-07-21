---
title: "[Solution] Django Message Framework Error"
description: "Messages not displaying."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Messages not displaying.

## Common Causes

Middleware missing.

## How to Fix

Add middleware.

## Example

```python
MIDDLEWARE = [..., 'django.contrib.messages.middleware.MessageMiddleware', ...]
```

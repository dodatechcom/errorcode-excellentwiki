---
title: "[Solution] Django CSRF Cookie Error Django"
description: "CSRF cookie not setting."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

CSRF cookie not setting.

## Common Causes

Middleware missing.

## How to Fix

Add middleware.

## Example

```python
MIDDLEWARE = [..., 'django.middleware.csrf.CsrfViewMiddleware', ...]
```

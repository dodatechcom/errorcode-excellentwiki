---
title: "[Solution] Django Middleware Error Django"
description: "Middleware not executing."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Middleware not executing.

## Common Causes

Not in MIDDLEWARE.

## How to Fix

Add to MIDDLEWARE.

## Example

```python
MIDDLEWARE = ['myapp.middleware.MyMiddleware', ...]
```

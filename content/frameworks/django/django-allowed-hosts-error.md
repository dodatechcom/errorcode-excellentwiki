---
title: "[Solution] Django Allowed Hosts Error"
description: "DisallowedHost error."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

DisallowedHost error.

## Common Causes

ALLOWED_HOSTS empty.

## How to Fix

Add domain.

## Example

```python
ALLOWED_HOSTS = ['example.com']
```

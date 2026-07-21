---
title: "[Solution] Django Database Connection Error Django"
description: "Database connection failing."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Database connection failing.

## Common Causes

Wrong config.

## How to Fix

Check DATABASES.

## Example

```python
DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql', 'NAME': 'mydb'}}
```

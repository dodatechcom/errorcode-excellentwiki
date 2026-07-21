---
title: "[Solution] Django Static Files Finders Error"
description: "Static files not found."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Static files not found.

## Common Causes

Finders not configured.

## How to Fix

Configure finders.

## Example

```python
STATICFILES_FINDERS = ['django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder']
```

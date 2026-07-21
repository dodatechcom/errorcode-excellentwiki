---
title: "[Solution] Django Static File Storage Error"
description: "Static file storage wrong."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Static file storage wrong.

## Common Causes

Wrong storage.

## How to Fix

Configure storage.

## Example

```python
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
```

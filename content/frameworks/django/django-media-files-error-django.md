---
title: "[Solution] Django Media Files Error Django"
description: "Media files not serving."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Media files not serving.

## Common Causes

MEDIA_URL not set.

## How to Fix

Configure media.

## Example

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

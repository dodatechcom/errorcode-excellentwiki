---
title: "[Solution] Django REST Filter Error"
description: "Filter not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Filter not working.

## Common Causes

Not configured.

## How to Fix

Configure filter.

## Example

```python
REST_FRAMEWORK = {'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']}
```

---
title: "[Solution] Django REST Throttle Error"
description: "Throttle not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Throttle not working.

## Common Causes

Not configured.

## How to Fix

Configure throttle.

## Example

```python
REST_FRAMEWORK = {'DEFAULT_THROTTLE_CLASSES': ['rest_framework.throttling.AnonRateThrottle'], 'DEFAULT_THROTTLE_RATES': {'anon': '100/day'}}
```

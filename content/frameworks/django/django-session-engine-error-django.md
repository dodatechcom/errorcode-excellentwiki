---
title: "[Solution] Django Session Engine Error Django"
description: "Session not persisting."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Session not persisting.

## Common Causes

Wrong engine.

## How to Fix

Configure engine.

## Example

```python
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
```

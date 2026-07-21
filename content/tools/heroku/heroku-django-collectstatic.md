---
title: "[Solution] Heroku Django Collectstatic Error"
description: "Fix Heroku Django collectstatic errors. Resolve static file collection issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Django Collectstatic Error can prevent your application from working correctly.

## Common Causes

- Collectstatic failed
- Static files missing
- Configuration error

## How to Fix

### Run Collectstatic

```bash
heroku run python manage.py collectstatic --app my-app
```


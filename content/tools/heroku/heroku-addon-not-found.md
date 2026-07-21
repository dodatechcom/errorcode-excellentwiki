---
title: "[Solution] Heroku Addon Not Found Error"
description: "Fix Heroku addon not found errors. Resolve addon lookup issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Addon Not Found Error can prevent your application from working correctly.

## Common Causes

- Addon does not exist
- Addon in different region
- Addon name misspelled

## How to Fix

### List Addons

```bash
heroku addons --app my-app
```


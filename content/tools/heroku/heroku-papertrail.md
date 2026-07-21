---
title: "[Solution] Heroku Papertrail Error"
description: "Fix Heroku Papertrail errors. Resolve Papertrail logging issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Papertrail Error can prevent your application from working correctly.

## Common Causes

- Papertrail not connected
- Logs not syncing
- Account issue

## How to Fix

### Add Papertrail

```bash
heroku addons:create papertrail:starter --app my-app
```


---
title: "[Solution] Heroku Addon Provisioning Error"
description: "Fix Heroku addon provisioning errors. Resolve addon creation issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Addon Provisioning Error can prevent your application from working correctly.

## Common Causes

- Provisioning failed
- Plan unavailable
- Resource limit reached

## How to Fix

### Create Addon

```bash
heroku addons:create addon-name:plan --app my-app
```


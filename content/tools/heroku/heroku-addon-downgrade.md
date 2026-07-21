---
title: "[Solution] Heroku Addon Downgrade Error"
description: "Fix Heroku addon downgrade errors. Resolve plan downgrade issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Addon Downgrade Error can prevent your application from working correctly.

## Common Causes

- Downgrade failed
- Data too large for plan
- Plan not available

## How to Fix

### Downgrade

```bash
heroku addons:downgrade addon-name:new-plan --app my-app
```


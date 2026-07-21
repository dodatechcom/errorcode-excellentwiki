---
title: "[Solution] Heroku Database Not Provisioned Error"
description: "Fix Heroku database not provisioned errors. Resolve database addon issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Database Not Provisioned Error can prevent your application from working correctly.

## Common Causes

- Database addon not installed
- Addon not attached
- Plan insufficient

## How to Fix

### Add Database

```bash
heroku addons:create heroku-postgresql:essential-0 --app my-app
```


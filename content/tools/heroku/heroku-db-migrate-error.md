---
title: "[Solution] Heroku Database Migrate Error"
description: "Fix Heroku database migrate errors. Resolve migration execution issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Database Migrate Error can prevent your application from working correctly.

## Common Causes

- Migration failed
- Schema conflict
- Permission denied

## How to Fix

### Run Migrations

```bash
heroku run rake db:migrate --app my-app
```


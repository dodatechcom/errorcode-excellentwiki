---
title: "[Solution] Heroku pg pull Error"
description: "Fix Heroku pg pull errors. Resolve database pull issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku pg pull Error can prevent your application from working correctly.

## Common Causes

- Pull failed
- Database not found
- Permission denied

## How to Fix

### Pull Database

```bash
heroku pg:pull DATABASE_URL mydb --app my-app
```


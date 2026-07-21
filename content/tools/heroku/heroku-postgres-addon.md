---
title: "[Solution] Heroku Postgres Addon Error"
description: "Fix Heroku Postgres addon errors. Resolve PostgreSQL database issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Postgres Addon Error can prevent your application from working correctly.

## Common Causes

- Addon not found
- Connection refused
- Database full

## How to Fix

### Check Addon

```bash
heroku addons --app my-app
```

### Connect

```bash
heroku pg:psql --app my-app
```


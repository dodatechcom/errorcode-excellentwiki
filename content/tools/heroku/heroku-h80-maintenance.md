---
title: "[Solution] Heroku H80 Maintenance Mode Error"
description: "Fix Heroku H80 maintenance mode errors. Resolve maintenance mode issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku H80 Maintenance Mode Error can prevent your application from working correctly.

## Common Causes

- Maintenance mode enabled
- Site showing maintenance page

## How to Fix

### Disable Maintenance

```bash
heroku maintenance:off --app my-app
```


---
title: "[Solution] Heroku Logs Error"
description: "Fix Heroku logs errors. Resolve log viewing issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Logs Error can prevent your application from working correctly.

## Common Causes

- Logs not available
- Log drain not configured
- Retention expired

## How to Fix

### View Logs

```bash
heroku logs --tail --app my-app
```

### View Specific Source

```bash
heroku logs --source app --app my-app
```


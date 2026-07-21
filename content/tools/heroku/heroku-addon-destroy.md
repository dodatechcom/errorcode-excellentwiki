---
title: "[Solution] Heroku Addon Destroy Error"
description: "Fix Heroku addon destroy errors. Resolve addon deletion issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Addon Destroy Error can prevent your application from working correctly.

## Common Causes

- Addon in use
- Destroy failed
- Data will be lost

## How to Fix

### Destroy Addon

```bash
heroku addons:destroy addon-name --app my-app --confirm my-app
```


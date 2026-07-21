---
title: "[Solution] Heroku Web Dyno Error"
description: "Fix Heroku web dyno errors. Resolve web process issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Web Dyno Error can prevent your application from working correctly.

## Common Causes

- Dyno not running
- Crash loop
- Boot timeout
- Memory exceeded

## How to Fix

### Check Status

```bash
heroku ps --app my-app
```

### Restart

```bash
heroku ps:restart web --app my-app
```


---
title: "[Solution] Heroku Redis Addon Error"
description: "Fix Heroku Redis addon errors. Resolve Redis cache issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Redis Addon Error can prevent your application from working correctly.

## Common Causes

- Addon not found
- Connection refused
- Memory full

## How to Fix

### Add Redis

```bash
heroku addons:create heroku-redis:mini --app my-app
```

### Check Status

```bash
heroku redis:info --app my-app
```


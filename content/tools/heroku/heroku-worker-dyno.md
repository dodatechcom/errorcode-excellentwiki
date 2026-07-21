---
title: "[Solution] Heroku Worker Dyno Error"
description: "Fix Heroku worker dyno errors. Resolve background process issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Worker Dyno Error can prevent your application from working correctly.

## Common Causes

- Worker not running
- Crash loop
- No web dyno
- Resource limit

## How to Fix

### Check Status

```bash
heroku ps --app my-app
```

### Scale Worker

```bash
heroku ps:scale worker=1 --app my-app
```


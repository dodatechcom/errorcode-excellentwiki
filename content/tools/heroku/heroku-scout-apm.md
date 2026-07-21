---
title: "[Solution] Heroku Scout APM Error"
description: "Fix Heroku Scout APM errors. Resolve Scout monitoring issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Scout APM Error can prevent your application from working correctly.

## Common Causes

- Scout not connected
- Data not syncing
- Agent error

## How to Fix

### Add Scout

```bash
heroku addons:create scout:developer --app my-app
```


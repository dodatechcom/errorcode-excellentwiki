---
title: "[Solution] Heroku Clock Dyno Error"
description: "Fix Heroku clock dyno errors. Resolve scheduled task process issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Clock Dyno Error can prevent your application from working correctly.

## Common Causes

- Clock not running
- Scheduler misconfigured
- Task not scheduled

## How to Fix

### Check Clock

```bash
heroku ps --app my-app
```


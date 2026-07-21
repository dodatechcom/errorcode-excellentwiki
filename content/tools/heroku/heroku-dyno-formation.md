---
title: "[Solution] Heroku Dyno Formation Error"
description: "Fix Heroku dyno formation errors. Resolve dyno scaling issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Dyno Formation Error can prevent your application from working correctly.

## Common Causes

- Formation not set
- Invalid dyno type
- Scaling limit reached

## How to Fix

### Check Formation

```bash
heroku ps --app my-app
```

### Scale

```bash
heroku ps:scale web=1 --app my-app
```


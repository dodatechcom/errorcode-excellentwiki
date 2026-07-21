---
title: "[Solution] Heroku Datastore Error"
description: "Fix Heroku datastore errors. Resolve database service issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Datastore Error can prevent your application from working correctly.

## Common Causes

- Service unavailable
- Connection timeout
- Quota exceeded

## How to Fix

### Check Status

```bash
heroku pg:info --app my-app
```


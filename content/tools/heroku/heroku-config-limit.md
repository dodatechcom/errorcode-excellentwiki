---
title: "[Solution] Heroku Config Limit Error"
description: "Fix Heroku config limit errors. Resolve config var limit issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Config Limit Error can prevent your application from working correctly.

## Common Causes

- Too many config vars
- Total size exceeded

## How to Fix

### Check Limits

```bash
heroku config --app my-app
```

### Remove Unused

```bash
heroku config:unset UNUSED_VAR --app my-app
```


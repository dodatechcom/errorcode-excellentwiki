---
title: "[Solution] Heroku Config Var Error"
description: "Fix Heroku config var errors. Resolve environment variable issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Config Var Error can prevent your application from working correctly.

## Common Causes

- Config var not set
- Var name invalid
- Var value too large

## How to Fix

### Set Config Var

```bash
heroku config:set MY_VAR=value --app my-app
```

### List Vars

```bash
heroku config --app my-app
```


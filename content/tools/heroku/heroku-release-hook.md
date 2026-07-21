---
title: "[Solution] Heroku Release Hook Error"
description: "Fix Heroku release hook errors. Resolve release notification issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Release Hook Error can prevent your application from working correctly.

## Common Causes

- Hook not triggered
- Script failed
- Hook not configured

## How to Fix

### Add Release Hook

```bash
heroku addons:create deployhooks:http --app my-app
```


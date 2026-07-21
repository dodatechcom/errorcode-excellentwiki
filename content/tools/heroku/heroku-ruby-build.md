---
title: "[Solution] Heroku Ruby Build Error"
description: "Fix Heroku Ruby build errors. Resolve Ruby compilation issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Ruby Build Error can prevent your application from working correctly.

## Common Causes

- Ruby version mismatch
- Gem installation failed
- Native extension failed

## How to Fix

### Set Ruby Version

```bash
heroku config:set RUBY_VERSION=3.1 --app my-app
```


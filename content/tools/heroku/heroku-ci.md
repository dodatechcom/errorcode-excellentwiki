---
title: "[Solution] Heroku CI Error"
description: "Fix Heroku CI errors. Resolve continuous integration issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku CI Error can prevent your application from working correctly.

## Common Causes

- CI not enabled
- Test failed
- Buildpack error
- Config error

## How to Fix

### Enable CI

```bash
heroku features:enable ci --app my-app
```


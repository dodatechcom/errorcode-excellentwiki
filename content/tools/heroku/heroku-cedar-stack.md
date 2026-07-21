---
title: "[Solution] Heroku Cedar Stack Error"
description: "Fix Heroku Cedar stack errors. Resolve Cedar stack specific issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Cedar Stack Error can prevent your application from working correctly.

## Common Causes

- Cedar stack deprecated
- Features not available
- Migration required

## How to Fix

### Check Stack

```bash
heroku stack --app my-app
```

### Upgrade

```bash
heroku stack:set heroku-22 --app my-app
```


---
title: "[Solution] Heroku Stack Not Supported Error"
description: "Fix Heroku stack not supported errors. Resolve stack compatibility issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Stack Not Supported Error can prevent your application from working correctly.

## Common Causes

- Stack deprecated
- Stack not available
- App on unsupported stack

## How to Fix

### Check Stack

```bash
heroku stack
```

### Upgrade Stack

```bash
heroku stack:set heroku-22
```


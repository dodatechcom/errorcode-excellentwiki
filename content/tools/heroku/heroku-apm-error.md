---
title: "[Solution] Heroku APM Error"
description: "Fix Heroku APM errors. Resolve application performance monitoring issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku APM Error can prevent your application from working correctly.

## Common Causes

- APM not configured
- Data not collected
- Agent not installed

## How to Fix

### Install APM

```bash
heroku addons:create newrelic:developer --app my-app
```


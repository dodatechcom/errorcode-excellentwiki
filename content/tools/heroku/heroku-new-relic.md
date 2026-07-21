---
title: "[Solution] Heroku New Relic Error"
description: "Fix Heroku New Relic errors. Resolve New Relic monitoring issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku New Relic Error can prevent your application from working correctly.

## Common Causes

- New Relic not configured
- License key invalid
- Agent not running

## How to Fix

### Add New Relic

```bash
heroku addons:create newrelic:developer --app my-app
```


---
title: "[Solution] Heroku One-Off Dyno Error"
description: "Fix Heroku one-off dyno errors. Resolve ad-hoc process issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku One-Off Dyno Error can prevent your application from working correctly.

## Common Causes

- One-off dyno failed
- Command not found
- Timeout

## How to Fix

### Run Command

```bash
heroku run bash --app my-app
```


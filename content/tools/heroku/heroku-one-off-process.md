---
title: "[Solution] Heroku One-Off Process Error"
description: "Fix Heroku one-off process errors. Resolve ad-hoc process issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku One-Off Process Error can prevent your application from working correctly.

## Common Causes

- Process failed
- Command not found
- Timeout

## How to Fix

### Run Process

```bash
heroku run "node script.js" --app my-app
```


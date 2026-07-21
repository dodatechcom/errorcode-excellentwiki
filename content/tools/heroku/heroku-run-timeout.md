---
title: "[Solution] Heroku Run Timeout Error"
description: "Fix Heroku run timeout errors. Resolve command timeout issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Run Timeout Error can prevent your application from working correctly.

## Common Causes

- Command exceeds time limit
- Long-running task
- Connection lost

## How to Fix

### Increase Timeout

```bash
heroku run bash --app my-app --timeout 600
```


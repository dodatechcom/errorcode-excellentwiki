---
title: "[Solution] Heroku Review Error"
description: "Fix Heroku review errors. Resolve review app management issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Review Error can prevent your application from working correctly.

## Common Causes

- Review not found
- Review app failed
- Review expired

## How to Fix

### List Reviews

```bash
heroku review apps --pipeline my-pipeline
```


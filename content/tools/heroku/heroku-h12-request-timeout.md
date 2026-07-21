---
title: "[Solution] Heroku H12 Request Timeout Error"
description: "Fix Heroku H12 request timeout errors. Resolve 30-second timeout issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku H12 Request Timeout Error can prevent your application from working correctly.

## Common Causes

- Request takes longer than 30 seconds
- Slow database query
- External API timeout
- Blocking operation

## How to Fix

### Optimize Request

- Use background jobs for long tasks
- Add caching
- Optimize queries


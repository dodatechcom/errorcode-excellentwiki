---
title: "[Solution] Heroku SSL Required Error"
description: "Fix Heroku SSL required errors. Resolve database SSL connection issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku SSL Required Error can prevent your application from working correctly.

## Common Causes

- SSL not configured
- Connection rejected without SSL

## How to Fix

### Enable SSL

Append `?sslmode=require` to database URL.


---
title: "[Solution] Heroku HTTPS Drain Error"
description: "Fix Heroku HTTPS drain errors. Resolve HTTPS log forwarding issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku HTTPS Drain Error can prevent your application from working correctly.

## Common Causes

- HTTPS drain not configured
- URL invalid
- Certificate error

## How to Fix

### Add HTTPS Drain

```bash
heroku drains:add https://logs.example.com --app my-app
```


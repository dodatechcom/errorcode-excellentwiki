---
title: "[Solution] Heroku Syslog Drain Error"
description: "Fix Heroku syslog drain errors. Resolve syslog forwarding issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Syslog Drain Error can prevent your application from working correctly.

## Common Causes

- Syslog drain not configured
- URL invalid
- Logs not arriving

## How to Fix

### Add Syslog Drain

```bash
heroku drains:add syslog+tls://logs.example.com:514 --app my-app
```


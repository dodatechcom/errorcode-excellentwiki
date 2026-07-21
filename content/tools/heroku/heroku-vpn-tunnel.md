---
title: "[Solution] Heroku VPN Tunnel Error"
description: "Fix Heroku VPN tunnel errors. Resolve VPN tunnel issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku VPN Tunnel Error can prevent your application from working correctly.

## Common Causes

- Tunnel not established
- Configuration invalid
- Route missing

## How to Fix

### Check Tunnel

```bash
heroku peerings:info --space my-space
```


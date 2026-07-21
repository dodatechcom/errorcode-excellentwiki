---
title: "[Solution] Heroku VPN Connection Error"
description: "Fix Heroku VPN connection errors. Resolve VPN setup issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku VPN Connection Error can prevent your application from working correctly.

## Common Causes

- VPN not connected
- Tunnel down
- Configuration error

## How to Fix

### Check VPN

```bash
heroku peerings:info --space my-space
```


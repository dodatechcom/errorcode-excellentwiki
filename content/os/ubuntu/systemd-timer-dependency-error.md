---
title: "Systemd Timer Dependency Error"
description: "Timer-triggered service fails due to unmet dependencies"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Systemd Timer Dependency Error

Timer-triggered service fails due to unmet dependencies

## Common Causes

- Required service (e.g., network.target) not started
- Timer fires before system fully booted
- Missing After= or Requires= directives
- Service has Wants= for non-existent target

## How to Fix

1. Check service dependencies: `systemctl list-dependencies <service>`
2. Add After= and Requires= to service unit
3. Add Wants=network.target to timer or service
4. Verify with `systemd-analyze verify <service>`

## Examples

```bash
# Check service dependencies
systemctl list-dependencies myservice.service

# Analyze service unit
systemd-analyze verify myservice.service
```

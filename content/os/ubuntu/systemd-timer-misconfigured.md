---
title: "Systemd Timer Unit Misconfigured"
description: "Systemd timer unit file has syntax errors preventing timer from running"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Systemd Timer Unit Misconfigured

Systemd timer unit file has syntax errors preventing timer from running

## Common Causes

- Invalid OnCalendar or OnBootSec expression
- Unit directive references non-existent .service file
- Missing [Timer] section
- Timer unit not enabled

## How to Fix

1. Check timer status: `systemctl list-timers --all`
2. Verify unit file: `systemd-analyze verify mytimer.timer`
3. Check calendar expression: `systemd-analyze calendar 'daily'`
4. Enable and start: `systemctl enable --now mytimer.timer`

## Examples

```bash
# Check all timers
systemctl list-timers --all

# Verify timer unit file
sudo systemd-analyze verify mytimer.timer

# Test calendar expression
systemd-analyze calendar 'Mon *-*-* 09:00:00'
```

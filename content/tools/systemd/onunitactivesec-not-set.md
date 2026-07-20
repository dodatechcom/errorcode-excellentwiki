---
title: "[Solution] systemd OnUnitActiveSec not set"
description: "Fix systemd OnUnitActiveSec not set warnings. Resolve timer issues with missing repeat intervals."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd OnUnitActiveSec not set

## Error Description

myapp.timer: Neither OnCalendar= nor OnUnitActiveSec= is set.

The timer has no way to determine when to fire next.

## Common Causes

Common Causes:
- Timer unit file has no scheduling directive
- Only OnBootSec= is set without a recurring trigger
- Timer was misconfigured

## How to Fix

How to Fix:
```bash
# Add a scheduling directive
sudo systemctl edit myapp.timer
```

```ini
[Timer]
# For one-shot after boot:
OnBootSec=5min

# For recurring:
OnUnitActiveSec=1h

# For calendar-based:
OnCalendar=*-*-* 02:00:00
```

## Examples

```bash
# Check systemd version
systemctl --version

# Verify unit file syntax
sudo systemd-analyze verify /etc/systemd/system/myapp.service

# Analyze system boot
systemd-analyze blame

# List failed units
systemctl --failed

# View service logs
journalctl -u myapp -n 50 --no-pager
```
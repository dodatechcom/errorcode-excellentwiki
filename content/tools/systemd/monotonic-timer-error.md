---
title: "[Solution] systemd monotonic timer error"
description: "Fix systemd monotonic timer error. Resolve OnActiveSec, OnBootSec, or OnUnitActiveSec configuration issues."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd monotonic timer error

## Error Description

myapp.timer: Invalid monotonic timer value: -10s.

Monotonic timer values must be positive.

## Common Causes

Common Causes:
- Negative value specified for a monotonic timer
- Invalid time format (e.g., missing unit suffix)
- Value is 0 or negative

## How to Fix

How to Fix:
```bash
# Valid monotonic timer values are positive
sudo systemctl edit myapp.timer
```

```ini
[Timer]
OnActiveSec=10min
OnBootSec=5min
OnUnitActiveSec=1h
OnUnitInactiveSec=30min
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
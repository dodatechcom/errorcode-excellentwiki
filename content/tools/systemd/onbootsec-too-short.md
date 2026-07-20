---
title: "[Solution] systemd OnBootSec too short"
description: "Fix systemd OnBootSec too short. Resolve timer issues where the boot delay is insufficient."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd OnBootSec too short

## Error Description

myapp.timer: OnBootSec=10s is too short. Minimum is 1ms.

The OnBootSec= value is below the minimum allowed.

## Common Causes

Common Causes:
- OnBootSec= set to a value below 1ms
- Value is negative or zero
- Value format is incorrect

## How to Fix

How to Fix:
```bash
# Valid OnBootSec= formats:
# OnBootSec=30s    (30 seconds after boot)
# OnBootSec=5min   (5 minutes after boot)
# OnBootSec=1h     (1 hour after boot)

sudo systemctl edit myapp.timer
```

```ini
[Timer]
OnBootSec=5min
OnUnitActiveSec=1h
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
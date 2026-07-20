---
title: "[Solution] systemd RandomizedDelaySec conflict"
description: "Fix systemd RandomizedDelaySec conflict. Resolve timer issues with incompatible delay settings."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd RandomizedDelaySec conflict

## Error Description

myapp.timer: RandomizedDelaySec=3600 conflicts with OnUnitActiveSec=60.

Randomized delay exceeds the interval.

## Common Causes

Common Causes:
- RandomizedDelaySec= is larger than the timer interval
- Delay would cause the next trigger before the previous completes
- OnUnitActiveSec= is too short for the random delay

## How to Fix

How to Fix:
```bash
# Adjust RandomizedDelaySec to be less than the interval
sudo systemctl edit myapp.timer
```

```ini
[Timer]
OnUnitActiveSec=1h
RandomizedDelaySec=5min
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
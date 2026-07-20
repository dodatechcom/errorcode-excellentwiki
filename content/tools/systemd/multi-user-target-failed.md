---
title: "[Solution] systemd multi-user.target failed"
description: "Fix systemd multi-user.target failed. Resolve boot failures where multi-user.target cannot be reached."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd multi-user.target failed

## Error Description

multi-user.target: Failed to start. System not reaching multi-user mode.

The system failed to reach the multi-user.target during boot.

## Common Causes

Common Causes:
- A required service in multi-user.target failed
- Network configuration error
- Filesystem mount failure
- Critical service dependency not met

## How to Fix

How to Fix:
```bash
# Check which services failed
systemctl --failed

# Check multi-user.target dependencies
systemctl list-dependencies multi-user.target

# Boot into rescue mode for debugging
sudo systemctl isolate rescue.target

# Check logs
journalctl -b -p err
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
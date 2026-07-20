---
title: "[Solution] systemd --user failed"
description: "Fix systemd --user failed. Resolve user session manager failures."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd --user failed

## Error Description

Failed to start user@1000.service: User session manager not starting.

The per-user systemd instance failed to start.

## Common Causes

 Common Causes:
- XDG_RUNTIME_DIR is not set
- D-Bus session bus is not available
- User service directory does not exist
- systemd-logind is not running

## How to Fix

How to Fix:
```bash
# Check user session
systemctl --user status

# Check logind
systemctl status systemd-logind

# Ensure XDG_RUNTIME_DIR is set
echo $XDG_RUNTIME_DIR

# Create runtime directory if missing
sudo mkdir -p /run/user/1000
sudo chown 1000:1000 /run/user/1000
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
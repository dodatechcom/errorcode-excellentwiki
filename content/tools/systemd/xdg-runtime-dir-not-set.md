---
title: "[Solution] systemd XDG_RUNTIME_DIR not set"
description: "Fix systemd XDG_RUNTIME_DIR not set. Resolve user service failures when the runtime directory is missing."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd XDG_RUNTIME_DIR not set

## Error Description

XDG_RUNTIME_DIR is not set. User services cannot start.

The XDG runtime directory environment variable is missing.

## Common Causes

Common Causes:
- User session does not set XDG_RUNTIME_DIR
- Runtime directory was not created
- systemd-logind did not set up the session
- SSH session without X forwarding

## How to Fix

How to Fix:
```bash
# Check if logind is running
systemctl status systemd-logind

# Manually set XDG_RUNTIME_DIR
export XDG_RUNTIME_DIR=/run/user/$(id -u)

# Ensure lingering is enabled
sudo loginctl enable-linger $USER

# Create the directory
sudo mkdir -p /run/user/$(id -u)
sudo chown $(id -u):$(id -u) /run/user/$(id -u)
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
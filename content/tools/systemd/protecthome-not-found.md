---
title: "[Solution] systemd ProtectHome not found"
description: "Fix systemd ProtectHome not found. Resolve service failures when ProtectHome blocks access to /home."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd ProtectHome not found

## Error Description

myapp.service: Cannot access /home. Protected by ProtectHome=yes.

The service is blocked from accessing /home.

## Common Causes

Common Causes:
- ProtectHome=yes makes /home inaccessible
- Application needs to read from /home
- User files are in /home and service needs access

## How to Fix

How to Fix:
```bash
# If the service needs access to /home
sudo systemctl edit myapp
```

```ini
[Service]
ProtectHome=no
# Or use specific paths:
# BindReadOnlyPaths=/home/myapp/config /home/myapp/config
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
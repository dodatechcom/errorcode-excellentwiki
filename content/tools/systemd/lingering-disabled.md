---
title: "[Solution] systemd lingering disabled"
description: "Fix systemd lingering disabled. Resolve user service failures when lingering is not enabled."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd lingering disabled

## Error Description

User services cannot start without a login session. Lingering is disabled.

The user needs lingering enabled to run services without an active session.

## Common Causes

Common Causes:
- Lingering is not enabled for the user
- User services need to run without a login session
- loginctl has not been configured for lingering

## How to Fix

How to Fix:
```bash
# Enable lingering
sudo loginctl enable-linger myuser

# Verify
ls /var/lib/systemd/linger/
ls /var/lib/systemd/linger/myuser

# List lingering users
loginctl list-users
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
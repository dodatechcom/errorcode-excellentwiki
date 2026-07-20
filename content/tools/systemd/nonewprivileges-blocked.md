---
title: "[Solution] systemd NoNewPrivileges blocked"
description: "Fix systemd NoNewPrivileges blocked. Resolve service failures when NoNewPrivileges prevents privilege escalation."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd NoNewPrivileges blocked

## Error Description

myapp.service: setuid() failed. NoNewPrivileges=yes is set.

The service cannot gain new privileges.

## Common Causes

Common Causes:
- NoNewPrivileges=yes prevents setuid/setgid
- Application requires setuid binaries
- Sudo is not allowed within the service
- Kernel feature not supported

## How to Fix

How to Fix:
```bash
# If the service legitimately needs new privileges
sudo systemctl edit myapp
```

```ini
[Service]
NoNewPrivileges=no
# Note: This reduces security. Only use if absolutely necessary.
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
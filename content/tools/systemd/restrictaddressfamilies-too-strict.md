---
title: "[Solution] systemd RestrictAddressFamilies too strict"
description: "Fix systemd RestrictAddressFamilies too strict. Resolve networking failures when address families are restricted."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd RestrictAddressFamilies too strict

## Error Description

myapp.service: socket() failed: EAFNOSUPPORT. Address family not allowed.

The service cannot create sockets of the required address family.

## Common Causes

Common Causes:
- RestrictAddressFamilies does not include AF_INET
- Service needs AF_NETLINK for certain operations
- D-Bus requires AF_UNIX

## How to Fix

How to Fix:
```bash
# Allow required address families
sudo systemctl edit myapp
```

```ini
[Service]
RestrictAddressFamilies=AF_INET AF_INET6 AF_UNIX AF_NETLINK
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
---
title: "[Solution] systemd ListenStream invalid"
description: "Fix systemd ListenStream invalid errors. Resolve socket unit ListenStream configuration errors."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd ListenStream invalid

## Error Description

myapp.socket: Invalid ListenStream address: [::]:abc

The ListenStream= value has an invalid address or port format.

## Common Causes

Common Causes:
- Invalid port number (non-numeric or out of range)
- Malformed IPv6 address
- Missing port specification
- Using a path that doesn't start with /

## How to Fix

How to Fix:
```bash
# Valid ListenStream formats:
# ListenStream=8080           (port on all interfaces)
# ListenStream=127.0.0.1:8080 (specific IPv4)
# ListenStream=[::]:8080      (all IPv6 interfaces)
# ListenStream=/run/myapp.sock (Unix socket)

sudo systemctl edit myapp.socket
```

```ini
[Socket]
ListenStream=8080
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
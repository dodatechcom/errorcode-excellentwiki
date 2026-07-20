---
title: "[Solution] systemd PrivateTmp not writable"
description: "Fix systemd PrivateTmp not writable. Resolve service failures when /tmp is private and not writable."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd PrivateTmp not writable

## Error Description

myapp.service: Cannot write to /tmp. PrivateTmp=yes may be preventing access.

The service cannot write to its private /tmp.

## Common Causes

Common Causes:
- PrivateTmp=yes creates a private /tmp but with restricted permissions
- Application expects shared /tmp
- /tmp is full or has wrong permissions

## How to Fix

How to Fix:
```bash
# Check private /tmp permissions
ls -la /tmp/private/myapp.service

# Or disable PrivateTmp
sudo systemctl edit myapp
```

```ini
[Service]
PrivateTmp=no
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
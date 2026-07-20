---
title: "[Solution] systemd SystemCallFilter blocked"
description: "Fix systemd SystemCallFilter blocked. Resolve service failures when system calls are blocked."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd SystemCallFilter blocked

## Error Description

myapp.service: System call 'mount' blocked by SystemCallFilter.

The service tried to use a blocked system call.

## Common Causes

Common Causes:
- SystemCallFilter=~@mount blocks mount-related calls
- Application requires blocked system calls
- Filter is too restrictive for the workload

## How to Fix

How to Fix:
```bash
# Remove the restrictive filter
sudo systemctl edit myapp
```

```ini
[Service]
# Remove SystemCallFilter or use a less restrictive one
SystemCallFilter=@system-service
# Or whitelist specific calls:
# SystemCallFilter=~@mount
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
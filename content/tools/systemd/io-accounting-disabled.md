---
title: "[Solution] systemd IO accounting disabled"
description: "Fix systemd IO accounting disabled. Resolve missing disk IO statistics for services."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd IO accounting disabled

## Error Description

IO usage statistics are not available for myapp.service.

IOAccounting= is not enabled for this service.

## Common Causes

Common Causes:
- IOAccounting=no is set
- cgroup IO controller not available
- IO accounting requires cgroup v2

## How to Fix

How to Fix:
```bash
# Enable IO accounting (requires cgroup v2)
sudo systemctl edit myapp
```

```ini
[Service]
IOAccounting=yes
IOWeight=100
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
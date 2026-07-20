---
title: "[Solution] systemd CPUAccounting not enabled"
description: "Fix systemd CPUAccounting not enabled. Resolve missing CPU usage statistics for services."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd CPUAccounting not enabled

## Error Description

CPU usage statistics are not available for myapp.service.

CPUAccounting= is not enabled for this service.

## Common Causes

Common Causes:
- CPUAccounting=no is set explicitly
- cgroup CPU controller not available
- systemd compiled without CPU accounting support

## How to Fix

How to Fix:
```bash
# Enable CPU accounting
sudo systemctl edit myapp
```

```ini
[Service]
CPUAccounting=yes
CPUQuota=100%
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
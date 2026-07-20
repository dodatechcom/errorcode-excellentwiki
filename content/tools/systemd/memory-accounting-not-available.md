---
title: "[Solution] systemd memory accounting not available"
description: "Fix systemd memory accounting not available. Resolve missing memory usage statistics."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd memory accounting not available

## Error Description

Memory usage statistics are not available for myapp.service.

MemoryAccounting is not supported for this service.

## Common Causes

Common Causes:
- MemoryAccounting=no is set
- cgroup memory controller not available
- Kernel compiled without memory cgroup support

## How to Fix

How to Fix:
```bash
# Enable memory accounting
sudo systemctl edit myapp
```

```ini
[Service]
MemoryAccounting=yes
MemoryMax=2G
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
---
title: "[Solution] systemd memory limit exceeded"
description: "Fix systemd memory limit exceeded. Resolve OOM kills when service memory limits are too low."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd memory limit exceeded

## Error Description

myapp.service: Memory limit exceeded. Process killed by OOM.

The service exceeded its configured MemoryMax and was killed.

## Common Causes

Common Causes:
- MemoryMax is set too low for the application
- Memory leak in the application
- Insufficient system memory
- MemoryHigh threshold being hit continuously

## How to Fix

How to Fix:
```bash
# Check memory usage
systemctl status myapp
systemd-cgtop

# Increase memory limit
sudo systemctl edit myapp
```

```ini
[Service]
MemoryMax=4G
MemoryHigh=3G
MemorySwapMax=2G
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
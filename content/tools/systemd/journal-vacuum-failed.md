---
title: "[Solution] systemd journal vacuum failed"
description: "Fix systemd journal vacuum failed. Resolve journal cleanup failures preventing disk space recovery."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd journal vacuum failed

## Error Description

Failed to vacuum journal: Permission denied

The journal vacuum operation could not complete.

## Common Causes

Common Causes:
- Insufficient privileges (not root)
- Journal files are owned by a different user
- Filesystem is read-only
- Journal is in volatile storage with special permissions

## How to Fix

How to Fix:
```bash
# Use sudo
sudo journalctl --vacuum-size=500M

# Or vacuum by time
sudo journalctl --vacuum-time=30d

# Or vacuum by files
sudo journalctl --vacuum-files=5
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
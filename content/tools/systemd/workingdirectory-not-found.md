---
title: "[Solution] systemd WorkingDirectory not found"
description: "Fix systemd WorkingDirectory not found errors. Resolve service start failures when the working directory is missing."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd WorkingDirectory not found

## Error Description

Failed to start myapp.service: Working directory '/opt/myapp' not found.

The directory specified by WorkingDirectory= does not exist.

## Common Causes

Common Causes:
- The directory was deleted or moved
- Typo in the path
- The directory has not been created yet
- NFS or remote mount not available

## How to Fix

How to Fix:
```bash
# Check if the directory exists
ls -la /opt/myapp

# Create the directory
sudo mkdir -p /opt/myapp
sudo chown myappuser:myappuser /opt/myapp

# Verify unit file
sudo systemd-analyze verify /etc/systemd/system/myapp.service
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
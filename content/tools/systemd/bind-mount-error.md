---
title: "[Solution] systemd bind mount error"
description: "Fix systemd bind mount error. Resolve bind mount failures in systemd mount units."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd bind mount error

## Error Description

mnt-link.mount: Bind mount failed: No such file or directory

The source directory for the bind mount does not exist.

## Common Causes

Common Causes:
- Source directory for bind mount does not exist
- Target directory does not exist
- SELinux blocking the bind mount
- Source is a file but target expects a directory

## How to Fix

How to Fix:
```bash
# Check source directory
ls -la /opt/myapp/data

# Create directories if missing
sudo mkdir -p /opt/myapp/data
sudo mkdir -p /mnt/data

# Update mount unit with Options=bind
sudo systemctl edit mnt-link.mount
```

```ini
[Mount]
What=/opt/myapp/data
Where=/mnt/data
Type=none
Options=bind
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
---
title: "[Solution] systemd automount timeout"
description: "Fix systemd automount timeout. Resolve automount units that time out during mounting."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd automount timeout

## Error Description

mnt-data.automount: Mounting timed out. Killing mount process.

The automount took too long to complete the mount.

## Common Causes

Common Causes:
- Network mount is slow to respond
- Device is slow to initialize
- Timeout is too short for the mount type
- NFS or SMB server is unreachable

## How to Fix

How to Fix:
```bash
# Increase the timeout
sudo systemctl edit mnt-data.automount
```

```ini
[Automount]
Where=/mnt/data
TimeoutIdleSec=120
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
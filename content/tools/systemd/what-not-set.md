---
title: "[Solution] systemd What= not set in mount unit"
description: "Fix systemd What= not set errors. Resolve mount unit configuration errors when the device path is missing."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd What= not set in mount unit

## Error Description

mnt-data.mount: What= is not set. Mount unit requires a device.

The What= directive is required in the [Mount] section.

## Common Causes

Common Causes:
- What= directive is missing from the mount unit
- Unit file was created without specifying the device
- The device path was removed accidentally

## How to Fix

How to Fix:
```bash
# Edit the mount unit to add What=
sudo systemctl edit mnt-data.mount --force
```

```ini
[Mount]
What=/dev/sdb1
Where=/mnt/data
Type=ext4
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
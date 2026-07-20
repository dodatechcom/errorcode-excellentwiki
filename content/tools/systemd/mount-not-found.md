---
title: "[Solution] systemd mount unit not found"
description: "Fix systemd mount unit not found errors. Resolve mount failures when the mount unit is missing."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd mount unit not found

## Error Description

Failed to mount mnt-data.mount: Unit mnt-data.mount not found.

The mount unit file does not exist.

## Common Causes

Common Causes:
- Mount unit file was not created
- Unit file was deleted
- The mount was configured in /etc/fstab but not converted to a systemd mount

## How to Fix

How to Fix:
```bash
# Check if the mount is in fstab
grep /mnt/data /etc/fstab

# Create the mount unit
sudo tee /etc/systemd/system/mnt-data.mount <<'EOF'
[Unit]
Description=Data Mount
After=blockdev@dev-disk-by\x2duuid-XXXX.target

[Mount]
What=/dev/sdb1
Where=/mnt/data
Type=ext4
Options=defaults

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable mnt-data.mount
sudo systemctl start mnt-data.mount
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
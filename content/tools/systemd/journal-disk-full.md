---
title: "[Solution] systemd journal disk full"
description: "Fix systemd journal disk full. Resolve situations where the journal has consumed all available disk space."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd journal disk full

## Error Description

No space left on device. Journal cannot write new entries.

The disk is full and the journal cannot create new files.

## Common Causes

Common Causes:
- Journal size limits not configured
- Disk partition is too small for logging
- Other data consuming disk space
- Log rotation not working

## How to Fix

How to Fix:
```bash
# Emergency: vacuum journal immediately
sudo journalctl --vacuum-size=100M

# Check disk usage
df -h /var/log

# Remove old journal files
sudo find /var/log/journal -name "*.journal" -mtime +7 -delete

# Configure permanent limits
sudo tee /etc/systemd/journald.conf <<'EOF'
[Journal]
SystemMaxUse=500M
RuntimeMaxUse=200M
EOF

sudo systemctl restart systemd-journald
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
---
title: "[Solution] systemd persistent journal not enabled"
description: "Fix systemd persistent journal not enabled. Resolve log persistence issues across reboots."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd persistent journal not enabled

## Error Description

Logs are not being persisted across reboots. Journal is volatile only.

The persistent journal storage is not configured.

## Common Causes

Common Causes:
- /var/log/journal directory does not exist
- Storage=volatile is configured
- journald.conf has Storage=none
- Missing systemd-journal persistence configuration

## How to Fix

How to Fix:
```bash
# Create persistent journal directory
sudo mkdir -p /var/log/journal

# Configure persistent storage
sudo tee /etc/systemd/journald.conf <<'EOF'
[Journal]
Storage=persistent
SystemMaxUse=1G
MaxRetentionSec=90day
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
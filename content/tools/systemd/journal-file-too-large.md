---
title: "[Solution] systemd journal file too large"
description: "Fix systemd journal file too large. Resolve disk space issues caused by large journal files."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd journal file too large

## Error Description

Journal file /var/log/journal/... is too large (2.5G). Consider using SystemMaxUse.

The journal has consumed excessive disk space.

## Common Causes

Common Causes:
- SystemMaxUse or SystemMaxFileSize not configured
- No journal vacuum policy set
- High-volume logging services

## How to Fix

How to Fix:
```bash
# Check current journal size
journalctl --disk-usage

# Vacuum old entries
sudo journalctl --vacuum-size=500M

# Configure size limits
sudo tee /etc/systemd/journald.conf <<'EOF'
[Journal]
SystemMaxUse=1G
SystemMaxFileSize=100M
MaxRetentionSec=30day
MaxFileSec=7day
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
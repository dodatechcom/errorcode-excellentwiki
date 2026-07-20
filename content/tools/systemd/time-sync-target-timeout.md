---
title: "[Solution] systemd time-sync.target timeout"
description: "Fix systemd time-sync.target timeout. Resolve boot delays when time synchronization takes too long."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd time-sync.target timeout

## Error Description

time-sync.target: Job timed out. NTP synchronization not complete.

The system could not synchronize time within the allowed timeout.

## Common Causes

Common Causes:
- NTP server is unreachable
- systemd-timesyncd is not configured
- Network not available for time sync
- Firewall blocking NTP traffic

## How to Fix

How to Fix:
```bash
# Check time sync status
timedatectl status

# Configure NTP
sudo timedatectl set-ntp true

# Check timesyncd
systemctl status systemd-timesyncd

# Set NTP server
sudo tee /etc/systemd/timesyncd.conf <<'EOF'
[Time]
NTP=pool.ntp.org
FallbackNTP=0.pool.ntp.org 1.pool.ntp.org
EOF

sudo systemctl restart systemd-timesyncd
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
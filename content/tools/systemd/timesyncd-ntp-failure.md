---
title: "[Solution] systemd timesyncd NTP failure"
description: "Fix systemd timesyncd NTP failure. Resolve time synchronization failures with systemd-timesyncd."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd timesyncd NTP failure

## Error Description

systemd-timesyncd.service: NTP synchronization failed. No server found.

The timesyncd daemon could not synchronize time.

## Common Causes

Common Causes:
- NTP servers are not configured or unreachable
- Network is not available
- Firewall blocking NTP traffic (port 123)
- DNS resolution failing for NTP servers

## How to Fix

How to Fix:
```bash
# Check timesyncd status
timedatectl status

# Configure NTP servers
sudo tee /etc/systemd/timesyncd.conf <<'EOF'
[Time]
NTP=0.pool.ntp.org 1.pool.ntp.org 2.pool.ntp.org
FallbackNTP=3.pool.ntp.org 4.pool.ntp.org
RootDistanceMaxSec=5
PollIntervalMinSec=32
PollIntervalMaxSec=2048
EOF

sudo systemctl restart systemd-timesyncd
timedatectl set-ntp true
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
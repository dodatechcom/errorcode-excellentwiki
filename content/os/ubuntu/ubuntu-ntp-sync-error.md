---
title: "Ubuntu NTP Time Synchronization Error"
description: "System time cannot be synchronized via NTP"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu NTP Time Synchronization Error

System time cannot be synchronized via NTP

## Common Causes

- NTP server unreachable or blocked by firewall
- systemd-timesyncd not running
- Chrony or ntp package not installed
- Time offset too large for step correction

## How to Fix

1. Check status: `timedatectl status`
2. Check sync: `timedatectl show-timesync`
3. List servers: `chronyc sources -v` or `ntpq -p`
4. Restart: `sudo systemctl restart systemd-timesyncd`

## Examples

```bash
# Check time sync status
timedatectl status

# Check NTP servers
chronyc sources -v

# Force time sync
sudo systemctl restart systemd-timesyncd
```

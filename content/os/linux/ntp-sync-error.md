---
title: "[Solution] Linux: ntp-sync-error -- NTP synchronization failure"
description: "Fix Linux NTP synchronization errors. NTP time sync failure causing certificate issues."
os: ["linux"]
error-types: ["time-error"]
severities: ["error"]
---

# Linux: NTP Sync Error

NTP synchronization errors prevent the system clock from aligning with reference servers.

## Common Causes

- NTP server unreachable due to firewall or network
- Chrony or systemd-timesyncd not running
- Clock drift too large for initial synchronization
- NTP port 123 UDP blocked by network
- Hardware clock drifting significantly

## How to Fix

### 1. Check NTP Status

```bash
timedatectl status
chronyc tracking 2>/dev/null
systemctl status systemd-timesyncd 2>/dev/null
```

### 2. Configure Time Sync

```bash
sudo timedatectl set-ntp true
sudo systemctl restart systemd-timesyncd
```

### 3. Use Alternative NTP

```bash
sudo apt install chrony
echo "pool pool.ntp.org iburst" | sudo tee /etc/chrony/chrony.conf
sudo systemctl restart chrony
```

## Examples

```bash
$ timedatectl status
               Local time: Thu 2026-07-20 14:00:00 UTC
                 RTC time: Thu 2026-07-20 12:30:00
                Sync time: no
$ chronyc tracking
System time : 0.000012345 seconds fast of NTP time
```

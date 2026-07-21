---
title: "NetworkManager Unmanaged Device Error"
description: "Network interface not managed by NetworkManager"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# NetworkManager Unmanaged Device Error

Network interface not managed by NetworkManager

## Common Causes

- Interface listed in /etc/network/interfaces
- managed=false in NetworkManager config
- udev rule excluding interface
- systemd-networkd managing the interface

## How to Fix

1. Check: `nmcli device status`
2. Remove interface from /etc/network/interfaces
3. Set managed: `NM_CONTROLLED=yes` or remove from interfaces file
4. Check udev: `udevadm info /sys/class/net/<iface> | grep ENV{NM_}`

## Examples

```bash
# Check device status
nmcli device status

# Force manage interface
nmcli device set eth0 managed yes

# Check if in interfaces file
grep eth0 /etc/network/interfaces
```

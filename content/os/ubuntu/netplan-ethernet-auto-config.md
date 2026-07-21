---
title: "Netplan Ethernet Auto-Configuration Error"
description: "Netplan fails to auto-configure Ethernet interface"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Netplan Ethernet Auto-Configuration Error

Netplan fails to auto-configure Ethernet interface

## Common Causes

- Match section does not match any interface
- Multiple match criteria conflict
- Interface name changed by udev rules
- Driver not loaded for network interface

## How to Fix

1. Check interface names: `ip link show`
2. Simplify match section or remove it
3. Check udev rules: `udevadm info /sys/class/net/<iface>`
4. Verify driver loaded: `lspci | grep -i ethernet`

## Examples

```bash
# List network interfaces
ip link show

# Check interface driver info
udevadm info /sys/class/net/eth0 | grep DRIVER

# Check lspci for network devices
lspci | grep -i ethernet
```

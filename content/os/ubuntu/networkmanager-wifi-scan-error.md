---
title: "[Solution] Ubuntu Server: networkmanager-wifi-scan-error"
description: "Fix Ubuntu networkmanager-wifi-scan-error. WiFi scan fails or finds no results."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# NetworkManager WiFi Scan Error

NetworkManager fails to scan for wireless networks.

## Common Causes
- WiFi adapter disabled by rfkill
- Driver does not support scan
- Regulatory domain blocking frequency
- WiFi power management turning off radio

## How to Fix
1. Check rfkill status
```bash
rfkill list
```
2. Unblock WiFi
```bash
rfkill unblock wifi
```
3. Scan manually
```bash
nmcli device wifi rescan
nmcli device wifi list
```

## Examples
```bash
$ rfkill list
0: phy0: Wireless LAN
    Soft blocked: no
    Hard blocked: no

$ nmcli device wifi list
SSID              MODE   CHAN  RATE       SIGNAL  BARS
MyNetwork         Infra  6     270 Mbit/s  85      ****
```

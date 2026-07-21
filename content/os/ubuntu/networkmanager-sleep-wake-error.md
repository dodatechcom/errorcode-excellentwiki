---
title: "[Solution] Ubuntu Server: networkmanager-sleep-wake-error"
description: "Fix Ubuntu networkmanager-sleep-wake-error. NM fails to handle sleep/wake transitions."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# NetworkManager Sleep Wake Error

NetworkManager fails after system resume from sleep.

## Common Causes
- Dispatcher scripts not handling sleep events
- Power management turning off WiFi on suspend
- systemd-logind not notifying NM
- Driver crash on resume

## How to Fix
1. Check NM dispatcher
```bash
ls /etc/NetworkManager/dispatcher.d/
```
2. Disable WiFi power save on suspend
```bash
sudo nano /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
[connection]
wifi.powersave = 2
```
3. Restart NM after wake
```bash
sudo systemctl restart NetworkManager
```

## Examples
```bash
$ systemctl suspend
$ # After wake:
$ nmcli device status
DEVICE  TYPE  STATE
eth0    ethernet  unmanaged

$ sudo systemctl restart NetworkManager
```

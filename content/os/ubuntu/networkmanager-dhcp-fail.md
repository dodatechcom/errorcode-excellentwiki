---
title: "[Solution] Ubuntu Server: networkmanager-dhcp-fail"
description: "Fix Ubuntu networkmanager-dhcp-fail. NetworkManager cannot obtain IP via DHCP."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# NetworkManager DHCP Failure

NetworkManager fails to obtain IP through DHCP.

## Common Causes
- DHCP server not responding
- NM dispatcher script blocking DHCP
- NM-managed flag set to no
- Firewall dropping DHCP offers

## How to Fix
1. Check NM status
```bash
nmcli device status
nmcli general status
```
2. Force DHCP request
```bash
nmcli device disconnect eth0
nmcli device connect eth0
```
3. Set managed=yes
```bash
sudo nano /etc/NetworkManager/NetworkManager.conf
[ifupdown]
managed=true
```

## Examples
```bash
$ nmcli device status
DEVICE  TYPE  STATE      CONNECTION
eth0    ethernet  disconnected  ---

$ nmcli device connect eth0
Device eth0 successfully activated.
```

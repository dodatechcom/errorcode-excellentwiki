---
title: "[Solution] Ubuntu Server: networkmanager-vpn-error"
description: "Fix Ubuntu networkmanager-vpn-error. NetworkManager VPN connection fails to establish."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# NetworkManager VPN Error

NetworkManager fails to establish or maintain a VPN connection.

## Common Causes
- VPN plugin not installed
- VPN config file has incorrect parameters
- Authentication credentials wrong
- Firewall blocking VPN port

## How to Fix
1. Check VPN plugins
```bash
dpkg -l | grep network-manager
```
2. Install required plugin
```bash
sudo apt install network-manager-openconnect-gnome
```
3. Check VPN logs
```bash
journalctl -u NetworkManager -f
```

## Examples
```bash
$ dpkg -l | grep network-manager
ii  network-manager-gnome

$ sudo apt install network-manager-openconnect-gnome
```

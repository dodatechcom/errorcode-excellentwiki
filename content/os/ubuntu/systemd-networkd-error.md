---
title: "[Solution] Ubuntu Server: system-networkd-error"
description: "Fix Ubuntu system-networkd-error. systemd-networkd fails to configure networking."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd Networkd Error

systemd-networkd encounters errors configuring network interfaces.

## Common Causes
- .network file syntax error
- Renderer conflict with NetworkManager
- Interface not managed by networkd
- DHCP client not starting

## How to Fix
1. Check networkd status
```bash
sudo systemctl status systemd-networkd
networkctl status
```
2. Check network files
```bash
ls /etc/systemd/network/
ls /run/systemd/network/
```
3. Verify config syntax
```bash
networkctl list
networkctl status <interface>
```

## Examples
```bash
$ sudo systemctl status systemd-networkd
● systemd-networkd.service - Network Service
   Active: failed (Result: exit-code)

$ networkctl status eth0
● 2: eth0
      State: failed
```

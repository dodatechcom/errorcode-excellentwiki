---
title: "[Solution] Ubuntu Server: networkmanager-dns-error"
description: "Fix Ubuntu networkmanager-dns-error. NetworkManager DNS configuration is incorrect."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# NetworkManager DNS Error

NetworkManager does not configure DNS correctly.

## Common Causes
- DNS settings overridden by connection profile
- systemd-resolved not integrated
- /etc/resolv.conf symlink broken
- VPN pushing incorrect DNS servers

## How to Fix
1. Check DNS configuration
```bash
nmcli device show eth0 | grep DNS
cat /etc/resolv.conf
```
2. Set DNS manually
```bash
nmcli con mod "Wired connection 1" ipv4.dns "8.8.8.8 8.8.4.4"
nmcli con mod "Wired connection 1" ipv4.ignore-auto-dns yes
```
3. Restart NetworkManager
```bash
sudo systemctl restart NetworkManager
```

## Examples
```bash
$ nmcli device show eth0 | grep DNS
DNS4[1]: 192.168.1.1

$ nmcli con mod "Wired 1" ipv4.dns "8.8.8.8"
```

---
title: "[Solution] Ubuntu Server: netplan-dns-from-dhcp-error"
description: "Fix Ubuntu netplan-dns-from-dhcp-error. DNS servers from DHCP not applied correctly."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Netplan DNS From DHCP Error

DNS servers obtained via DHCP are not applied to the system.

## Common Causes
- ignore-auto-dns set to true
- systemd-resolved not handling DHCP DNS
- Multiple DHCP clients conflicting
- resolv.conf not symlinked to stub

## How to Fix
1. Check DHCP DNS settings
```bash
nmcli device show eth0 | grep DNS
cat /etc/resolv.conf
```
2. Verify netplan config
```bash
sudo nano /etc/netplan/01-config.yaml
# Ensure dhcp4: true and no ignore-auto-dns
```
3. Restart network services
```bash
sudo systemctl restart systemd-networkd
sudo systemctl restart systemd-resolved
```

## Examples
```bash
$ cat /etc/resolv.conf
nameserver 127.0.0.53

$ resolvectl status
Global
  DNS Servers: 8.8.8.8
```

---
title: "[Solution] Ubuntu Server: netplan-dns-resolution-error"
description: "Fix Ubuntu netplan-dns-resolution-error. DNS resolution fails after netplan configuration."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Netplan DNS Resolution Error

DNS resolution fails after applying netplan config.

## Common Causes
- nameservers not defined in netplan
- DNS server unreachable
- /etc/resolv.conf overwritten by netplan
- systemd-resolved not running

## How to Fix
1. Check resolv.conf
```bash
cat /etc/resolv.conf
resolvectl status
```
2. Add DNS servers in netplan
```bash
sudo nano /etc/netplan/01-config.yaml
network:
  version: 2
  ethernets:
    eth0:
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
```
3. Restart resolved
```bash
sudo systemctl restart systemd-resolved
```

## Examples
```bash
$ nslookup google.com
;; connection timed out; no servers could be reached

$ resolvectl status
Global
  Protocols: +LLMNR +mDNS -DNSOverTLS
```

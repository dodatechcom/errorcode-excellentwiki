---
title: "[Solution] Ubuntu Server: networkmanager-dns-default-route-error"
description: "Fix Ubuntu networkmanager-dns-default-route-error. NM applies DNS from wrong connection."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# NetworkManager DNS Default Route Error

NetworkManager applies DNS settings from wrong connection.

## Common Causes
- Multiple active connections with different DNS
- VPN pushing default route without DNS
- Connection autoconnect priority wrong
- never-default flag conflicting

## How to Fix
1. List active connections
```bash
nmcli connection show --active
```
2. Check DNS per connection
```bash
nmcli connection show "Wired 1" | grep ipv4.dns
```
3. Adjust priorities
```bash
nmcli con mod "Wired 1" connection.autoconnect-priority 1
nmcli con mod "VPN" connection.autoconnect-priority 0
```

## Examples
```bash
$ nmcli connection show --active
NAME                UUID       TYPE   DEVICE
Wired 1             abc-123    ethernet  eth0
VPN                 def-456    vpn      tun0
```

---
title: "[Solution] Ubuntu Server: netplan-address-conflict"
description: "Fix Ubuntu netplan-address-conflict. IP address configured in netplan is already in use."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Netplan Address Conflict

The IP address configured in netplan is already in use.

## Common Causes
- Duplicate static IP on another server
- DHCP reservation conflict
- Virtual interface overlapping with physical
- Previous configuration not fully released

## How to Fix
1. Check which device has the address
```bash
ip addr show
arp -a
```
2. Use arping to find conflicting device
```bash
sudo arping -I eth0 192.168.1.10
```
3. Change IP in netplan config
```bash
sudo nano /etc/netplan/01-config.yaml
sudo netplan apply
```

## Examples
```bash
$ sudo netplan apply
Error: an address (192.168.1.10/24) is already assigned to eth0.

$ sudo arping -I eth0 192.168.1.10
ARPING 192.168.1.10
Unicast reply from 192.168.1.10 [AA:BB:CC:DD:EE:FF]  0.712ms
```

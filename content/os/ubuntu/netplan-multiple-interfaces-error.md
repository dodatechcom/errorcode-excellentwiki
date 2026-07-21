---
title: "[Solution] Ubuntu Server: netplan-multiple-interfaces-error"
description: "Fix Ubuntu netplan-multiple-interfaces-error. Multiple network interfaces cause routing conflicts."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Netplan Multiple Interfaces Conflict

Multiple interfaces cause routing conflicts.

## Common Causes
- Two interfaces on same subnet
- Both interfaces trying to be default gateway
- Bond/bridge member conflict
- VLAN interface overlapping with parent

## How to Fix
1. List all interfaces
```bash
ip link show
```
2. Check netplan for duplicates
```bash
cat /etc/netplan/01-config.yaml
```
3. Set specific routes per interface
```bash
sudo nano /etc/netplan/01-config.yaml
# Use routes instead of gateway4 for specific subnets
```

## Examples
```bash
$ ip link show
2: eth0: <BROADCAST,MULTICAST,UP> state UP
3: eth1: <BROADCAST,MULTICAST,UP> state UP

# Both have addresses in 192.168.1.0/24 -- conflict!
```

---
title: "[Solution] Ubuntu Server: netplan-bond-failover-error"
description: "Fix Ubuntu netplan-bond-failover-error. Network bonding failover does not work correctly."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Netplan Bond Failover Error

Network bonding fails to failover when a link goes down.

## Common Causes
- Bond mode not compatible with switch
- miimon interval too long
- Link detection not working
- Kernel bonding module not loaded

## How to Fix
1. Check bond status
```bash
cat /proc/net/bonding/bond0
```
2. Verify bond mode matches switch
```bash
sudo cat /etc/netplan/01-config.yaml
# mode: 802.3ad for LACP
```
3. Load bonding module
```bash
sudo modprobe bonding
```

## Examples
```bash
$ cat /proc/net/bonding/bond0
Bonding Mode: IEEE 802.3ad Link Aggregation
Slave Interface: eth0
MII Status: up
Slave Interface: eth1
MII Status: down
```

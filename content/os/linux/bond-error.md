---
title: "[Solution] Linux: bond-error — NIC bonding error"
description: "Fix Linux bond-error errors. NIC bonding error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 6
---

# Linux: Bond (NIC Teaming) Error

Bonding errors occur when network interfaces fail to aggregate into a bonded interface.

## Common Causes

- Bonding module not loaded
- Slave interface not available or down
- MII link monitoring failures
- Bond mode (balance-rr, active-backup, LACP) mismatch with switch
- MTU or speed mismatch between slaves

## How to Fix

### 1. Check Bond Status

```bash
cat /proc/net/bonding/bond0
sudo ip link show bond0
```

### 2. Check Bond Module

```bash
lsmod | grep bonding
sudo modprobe bonding
```

### 3. Check Slave Interfaces

```bash
sudo ip link show eth0 eth1
sudo ethtool eth0
```

### 4. Restart Bonding

```bash
sudo systemctl restart networking
# Or ifdown/ifup
sudo ifdown bond0 && sudo ifup bond0
```

## Examples

```bash
$ cat /proc/net/bonding/bond0
Ethernet Channel Bonding Driver: v5.15.0
Bonding Mode: IEEE 802.3ad Dynamic link aggregation
MII Status: up
MII Polling Interval (ms): 100
Up Delay (ms): 200
Down Delay (ms): 200

Slave Interface: eth0
MII Status: up
Link Failure Count: 0

$ sudo ip link set eth0 down
$ sudo ip link set eth0 up
$ cat /proc/net/bonding/bond0 | grep "MII Status"
MII Status: up
```

---
title: "[Solution] Ubuntu Server: netplan-vlan-error"
description: "Fix Ubuntu netplan-vlan-error. VLAN interfaces do not come up or have connectivity issues."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Netplan VLAN Error

VLAN interfaces fail to come up.

## Common Causes
- Parent interface not up
- VLAN ID mismatch with switch
- 8021q module not loaded
- VLAN sub-interface not created

## How to Fix
1. Check VLAN interfaces
```bash
ip -d link show type vlan
```
2. Load 8021q module
```bash
sudo modprobe 8021q
echo 8021q | sudo tee -a /etc/modules
```
3. Verify VLAN config syntax
```bash
sudo netplan generate
```

## Examples
```bash
$ ip -d link show type vlan
3: eth0.100@eth0: <BROADCAST,MULTICAST,UP> mtu 1500 state UP
    vlan protocol 802.1Q id 100 <REORDER_HDR>
```

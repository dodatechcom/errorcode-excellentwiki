---
title: "[Solution] Linux: vlan-error — VLAN configuration error"
description: "Fix Linux vlan-error errors. VLAN configuration error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 6
---
# Linux: VLAN Error

VLAN errors occur when 802.1Q VLAN tagging is misconfigured, preventing communication on the correct VLAN.

## Common Causes

- 8021q kernel module not loaded
- VLAN interface not created or not brought up
- Switch port not configured as trunk or incorrect allowed VLANs
- VLAN ID mismatch between host and switch
- Native VLAN mismatch causing untagged traffic issues

## How to Fix

### 1. Check VLAN Module

```bash
lsmod | grep 8021q
sudo modprobe 8021q
```

### 2. Create VLAN Interface

```bash
sudo ip link add link eth0 name eth0.100 type vlan id 100
sudo ip link set eth0.100 up
sudo ip addr add 192.168.100.1/24 dev eth0.100
```

### 3. Check Existing VLANs

```bash
cat /proc/net/vlan/config
ip link show | grep vlan
```

### 4. Remove VLAN Interface

```bash
sudo ip link delete eth0.100
```

### 5. Make Persistent

```bash
# For netplan:
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
  vlans:
    vlan.100:
      id: 100
      link: eth0
      addresses: [192.168.100.1/24]
```

## Examples

```bash
$ sudo ip link add link eth0 name eth0.10 type vlan id 10
$ sudo ip link set eth0.10 up
$ sudo ip addr add 192.168.10.100/24 dev eth0.10
$ ping 192.168.10.1
PING 192.168.10.1 (192.168.10.1) 56(84) bytes of data.
64 bytes from 192.168.10.1: icmp_seq=1 ttl=64 time=0.5 ms
```

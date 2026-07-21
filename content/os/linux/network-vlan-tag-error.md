---
title: "[Solution] Linux: network-vlan-tag-error -- VLAN tagging mismatch"
description: "Fix Linux network VLAN tagging errors. VLAN ID mismatch causing traffic drops."
os: ["linux"]
error-types: ["network-error"]
severities: ["error"]
---

# Linux: Network VLAN Tagging Error

VLAN tagging errors occur when VLAN IDs do not match between endpoints.

## Common Causes

- VLAN ID not matching switch configuration
- Trunk port not allowing the VLAN
- VLAN subinterface not properly created
- Native VLAN mismatch between devices
- Bonded interface VLAN misconfigured

## How to Fix

### 1. Check VLAN Configuration

```bash
ip -d link show eth0.100
bridge vlan show
```

### 2. Create or Fix VLAN Interface

```bash
sudo ip link add link eth0 name eth0.100 type vlan id 100
sudo ip addr add 192.168.100.10/24 dev eth0.100
sudo ip link set eth0.100 up
```

### 3. Verify Trunk Port

```bash
cat /proc/net/vlan/config
sudo tcpdump -i eth0 -e vlan -c 10
```

## Examples

```bash
$ cat /proc/net/vlan/config
VLAN Name   VID   Flags
eth0.100   100   REORDER_HDR
$ sudo tcpdump -i eth0 -e vlan -c 5
14:00:01 eth0 802.1Q vlan 100, p 0, encap IPv4
```

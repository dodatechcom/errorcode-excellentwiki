---
title: "[Solution] Ubuntu Server: netplan-route-error"
description: "Fix Ubuntu netplan-route-error. Netplan routing configuration fails or routes missing."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Netplan Route Error

netplan fails to apply routing configuration.

## Common Causes
- Missing default gateway configuration
- routes syntax incorrect in netplan
- Multiple default routes conflict
- Routing table full

## How to Fix
1. Check current routes
```bash
ip route show
```
2. Verify netplan routes syntax
```bash
sudo netplan generate
```
3. Add routes manually as test
```bash
sudo ip route add 10.0.0.0/8 via 192.168.1.1
```

## Examples
```bash
$ ip route show
default via 192.168.1.1 dev eth0 proto static
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.10
```

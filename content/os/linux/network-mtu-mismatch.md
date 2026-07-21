---
title: "[Solution] Linux: network-mtu-mismatch -- MTU mismatch"
description: "Fix Linux network MTU mismatch errors. MTU mismatch causing packet fragmentation or drops."
os: ["linux"]
error-types: ["network-error"]
severities: ["error"]
---

# Linux: Network MTU Mismatch

MTU mismatch causes packet fragmentation, performance degradation, and connectivity failures.

## Common Causes

- Different MTU values on both ends of a link
- VPN tunnel reducing effective MTU
- PPPoE adding 8-byte overhead
- ICMP fragmentation needed messages blocked
- Switch or router with non-standard MTU

## How to Fix

### 1. Test Path MTU

```bash
ping -M do -s 1472 -c 4 8.8.8.8
ip link show eth0 | grep mtu
```

### 2. Adjust MTU

```bash
sudo ip link set eth0 mtu 1500
sudo ip link set ppp0 mtu 1492
```

### 3. Check PMTU Discovery

```bash
sudo sysctl net.ipv4.ip_no_pmtu_disc
ip route get 8.8.8.8
```

## Examples

```bash
$ ping -M do -s 1472 -c 4 8.8.8.8
ping: local error: message too long, mtu=1500
$ ip link show eth0
2: eth0: <BROADCAST,MULTICAST,UP> mtu 9000
```

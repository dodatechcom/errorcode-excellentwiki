---
title: "[Solution] Linux: network-route-cache-error -- route cache corruption"
description: "Fix Linux network route cache corruption errors. Route cache corruption causing misrouting."
os: ["linux"]
error-types: ["network-error"]
severities: ["error"]
---

# Linux: Network Route Cache Corruption

Route cache corruption causes incorrect packet routing, leading to failed connections.

## Common Causes

- Kernel routing table corruption after hotplug
- Fibinfo cache not updating after interface changes
- Duplicate routes from multiple sources
- Policy routing rules conflicting with cache
- ARP cache poisoning affecting route resolution

## How to Fix

### 1. Flush Route Cache

```bash
sudo ip route flush cache
sudo ip neigh flush all
sudo sysctl -w net.ipv4.route.flush=1
```

### 2. Check Routing Table

```bash
ip route show table all
ip rule list
route -n
```

### 3. Rebuild Routes

```bash
sudo ip route del default
sudo ip route add default via <gateway>
ip route show
```

## Examples

```bash
$ ip route show
default via 192.168.1.1 dev eth0
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
$ sudo ip route flush cache
```

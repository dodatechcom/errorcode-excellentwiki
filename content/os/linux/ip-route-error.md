---
title: "[Solution] Linux: ip-route-error — ip route error"
description: "Fix Linux ip-route-error errors. ip route error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 8
---
# Linux: IP Route Error

IP route errors occur when the routing table is incorrect, missing, or has conflicting routes preventing network communication.

## Common Causes

- Default gateway missing or incorrect
- Multiple default routes on different interfaces causing ambiguity
- Wrong subnet mask causing incorrect route calculations
- Static route pointing to unreachable next-hop
- Routing table not updated after network changes

## How to Fix

### 1. View Routing Table

```bash
ip route show
route -n
```

### 2. Add Default Gateway

```bash
sudo ip route add default via 192.168.1.1
```

### 3. Delete Incorrect Routes

```bash
sudo ip route del default via 192.168.1.254
```

### 4. Add Specific Routes

```bash
# Route to specific subnet
sudo ip route add 10.0.0.0/24 via 192.168.1.1 dev eth0

# Route with metric
sudo ip route add default via 192.168.1.1 metric 100
```

### 5. Make Routes Persistent

```bash
# Edit /etc/network/interfaces or /etc/netplan/*.yaml
```

## Examples

```bash
$ ip route show
# No default route!

$ sudo ip route add default via 192.168.1.1
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=117 time=12.3 ms
```

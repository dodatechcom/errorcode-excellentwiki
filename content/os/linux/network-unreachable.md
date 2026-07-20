---
title: "[Solution] Linux: network-unreachable — network unreachable error"
description: "Fix Linux network-unreachable errors. network unreachable error with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["network"]
weight: 10
---
# Linux: Network Unreachable

"Network is unreachable" (ENETUNREACH) means the kernel has no route to the destination network.

## Common Causes

- Default gateway not configured or incorrect
- Network interface is down or has no IP address
- Destination network is on a disconnected interface
- Route to the network was deleted or never added
- VPN tunnel down causing routes to become unreachable

## How to Fix

### 1. Check Routing Table

```bash
ip route show
route -n
```

### 2. Check Interface Status

```bash
ip link show
ip addr show
```

### 3. Add Default Gateway

```bash
sudo ip route add default via 192.168.1.1
```

### 4. Add Specific Route

```bash
sudo ip route add 10.0.0.0/8 via 192.168.1.254 dev eth0
```

### 5. Restart Network

```bash
sudo systemctl restart networking
# Or on newer systems
sudo systemctl restart NetworkManager
```

## Examples

```bash
$ ping 8.8.8.8
connect: Network is unreachable

$ ip route show
# No routes!

$ sudo ip route add default via 192.168.1.1
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=117 time=12.3 ms
```

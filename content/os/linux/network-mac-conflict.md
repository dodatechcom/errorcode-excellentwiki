---
title: "[Solution] Linux: network-mac-conflict -- MAC address conflict"
description: "Fix Linux network MAC address conflict errors. Duplicate MAC causing network issues."
os: ["linux"]
error-types: ["network-error"]
severities: ["error"]
---

# Linux: Network MAC Address Conflict

MAC address conflicts cause intermittent connectivity with duplicated hardware addresses.

## Common Causes

- Virtual machine cloned with original MAC address
- NIC replacement copying old MAC configuration
- Docker or LXC containers using host MAC
- Duplicate MAC from firmware bug
- MAC address randomization collision

## How to Fix

### 1. Detect MAC Conflicts

```bash
arping -D -I eth0 -c 5 192.168.1.100
ip neigh show
nmap -sn 192.168.1.0/24
```

### 2. Change MAC Address

```bash
sudo ip link set dev eth0 down
sudo ip link set dev eth0 address 02:00:00:00:00:01
sudo ip link set dev eth0 up
```

### 3. Verify Resolution

```bash
arping -D -I eth0 -c 5 192.168.1.100
ip link show eth0 | grep link
```

## Examples

```bash
$ arping -D -I eth0 -c 5 192.168.1.100
ARPING 192.168.1.100 from 192.168.1.50 eth0
Unicast reply from 192.168.1.100 [02:15:5D:00:00:01] for 192.168.1.100
Sent 5 probes (5 broadcast(s))
Received 1 response(s)
```

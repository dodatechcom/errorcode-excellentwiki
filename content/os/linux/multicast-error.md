---
title: "[Solution] Linux: multicast-error — multicast configuration error"
description: "Fix Linux multicast-error errors. multicast configuration error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 6
---
# Linux: Multicast Error

Multicast errors occur when the network interface fails to join multicast groups or receive multicast traffic.

## Common Causes

- Multicast not enabled on the network interface
- IGMP/MLD snooping on switch filtering multicast traffic
- Firewall blocking multicast traffic (224.0.0.0/4)
- Application not joining the correct multicast group
- Routing table missing multicast route

## How to Fix

### 1. Check Multicast Configuration

```bash
ip link show | grep MULTICAST
cat /proc/net/dev_mcast
```

### 2. Enable Multicast on Interface

```bash
sudo ip link set eth0 multicast on
```

### 3. Join Multicast Group

```bash
sudo ip maddr add 224.0.0.1 dev eth0
```

### 4. Check IGMP Membership

```bash
cat /proc/net/igmp
cat /proc/net/igmp6
```

### 5. Add Multicast Route

```bash
sudo ip route add 224.0.0.0/4 dev eth0
```

## Examples

```bash
$ ip link show eth0
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000

$ cat /proc/net/dev_mcast
2 eth0  1  0  01005e000001
2 eth0  1  0  01005e0000fb

$ sudo ip maddr add 239.192.1.100 dev eth0
```

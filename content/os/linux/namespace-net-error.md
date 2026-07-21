---
title: "[Solution] Linux: namespace-net-error -- network namespace failure"
description: "Fix Linux network namespace errors. Network namespace creation or connectivity failure."
os: ["linux"]
error-types: ["namespace-error"]
severities: ["error"]
---

# Linux: Network Namespace Error

Network namespace errors occur when creating or connecting network namespaces fails.

## Common Causes

- veth pair creation failing due to permissions
- Bridge not configured for namespace connectivity
- iptables rules blocking namespace traffic
- Namespace not having loopback interface up
- Routes not configured for inter-namespace communication

## How to Fix

### 1. Create Network Namespace

```bash
sudo ip netns add myns
sudo ip netns list
sudo ip netns exec myns ip link list
```

### 2. Connect with veth Pair

```bash
sudo ip link add veth0 type veth peer name veth1
sudo ip link set veth1 netns myns
sudo ip addr add 192.168.100.1/24 dev veth0
sudo ip link set veth0 up
sudo ip netns exec myns ip addr add 192.168.100.2/24 dev veth1
sudo ip netns exec myns ip link set veth1 up
sudo ip netns exec myns ip link set lo up
```

### 3. Configure Routing

```bash
sudo ip netns exec myns ip route add default via 192.168.100.1
sudo ip route add 192.168.100.0/24 dev veth0
```

## Examples

```bash
$ sudo ip netns add myns
$ sudo ip netns exec myns ip link list
1: lo: <LOOPBACK> mtu 65536 qdisc noop state DOWN
$ sudo ip netns exec myns ip link set lo up
$ sudo ip netns exec myns ping -c 1 127.0.0.1
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.012 ms
```

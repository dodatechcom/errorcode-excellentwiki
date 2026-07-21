---
title: "[Solution] Linux: network-veth-pair-error -- veth pair creation failure"
description: "Fix Linux veth pair errors. Virtual ethernet pair creation or configuration failure."
os: ["linux"]
error-types: ["namespace-error"]
severities: ["error"]
---

# Linux: Veth Pair Error

Veth pair errors occur when creating virtual ethernet pairs fails.

## Common Causes

- Insufficient privileges for veth creation
- Kernel not compiled with veth module
- Peer namespace has conflicting interface name
- Bridge attachment failing for veth device
- Netns not properly initialized with loopback

## How to Fix

### 1. Check Veth Module

```bash
lsmod | grep veth
modprobe veth
ip link help veth
```

### 2. Create Veth Pair

```bash
sudo ip link add veth-host type veth peer name veth-ns
sudo ip link set veth-ns netns myns
sudo ip addr add 10.0.0.1/24 dev veth-host
sudo ip link set veth-host up
sudo ip netns exec myns ip addr add 10.0.0.2/24 dev veth-ns
sudo ip netns exec myns ip link set veth-ns up
```

### 3. Attach to Bridge

```bash
sudo ip link set veth-host master docker0
# Or with brctl
sudo brctl addif docker0 veth-host
```

## Examples

```bash
$ sudo ip link add veth-host type veth peer name veth-ns
$ sudo ip link show veth-host
3: veth-host@if2: <BROADCAST,MULTICAST,UP> mtu 1500
$ sudo ip link show veth-ns
4: veth-ns@if3: <BROADCAST,MULTICAST,UP> mtu 1500
```

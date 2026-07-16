---
title: "[Solution] Linux ENETUNREACH (errno 65) — Network Is Unreachable Fix"
description: "Fix Linux ENETUNREACH (errno 65) Network is unreachable error. Solutions for routing and network reachability issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enetunreach", "network", "errno-65", "routing", "unreachable"]
weight: 5
---

# Linux ENETUNREACH (errno 65) — Network Is Unreachable

ENETUNREACH (errno 65) means the network is unreachable. This error occurs when a program tries to communicate with a remote host but there is no route to reach the destination network. It is distinct from EHOSTUNREACH (errno 77) because ENETUNREACH refers to the network itself being unreachable, not a specific host.

## Common Causes

- No default gateway configured
- Routing table is missing an entry for the destination network
- Network interface lacks IP configuration
- Firewall or router blocking the route

## How to Fix ENETUNREACH

### 1. Check Routing Table

View the current routing configuration:

```bash
ip route show
route -n
```

### 2. Add a Default Gateway

Set a default gateway if missing:

```bash
sudo ip route add default via 192.168.1.1
```

### 3. Check IP Configuration

Verify the interface has an IP address:

```bash
ip addr show
```

### 4. Add a Static Route

For specific network destinations:

```bash
sudo ip route add 10.0.0.0/8 via 192.168.1.1
```

### 5. Restart Network Services

Apply routing changes:

```bash
sudo systemctl restart NetworkManager
```

## Verification

After fixing the route, confirm reachability:

```bash
ping -c 3 8.8.8.8
traceroute 8.8.8.8
```

## Related Error Codes

- [ENETDOWN (errno 64)](/os/linux/errno-64/) — Network is down
- [EHOSTUNREACH (errno 77)](/os/linux/errno-77/) — No route to host
- [ENONET (errno 49)](/os/linux/errno-49/) — Machine is not on the network

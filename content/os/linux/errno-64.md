---
title: "[Solution] Linux ENETDOWN (errno 64) — Network Is Down Fix"
description: "Fix Linux ENETDOWN (errno 64) Network is down error. Solutions for network interface and connectivity issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enetdown", "network", "errno-64", "interface", "down"]
weight: 5
---

# Linux ENETDOWN (errno 64) — Network Is Down

ENETDOWN (errno 64) means the network subsystem has been shut down. This error occurs when a program tries to send data over a network interface that is currently down or when the networking stack has been disabled. It is distinct from ENETUNREACH (errno 65) because ENETDOWN indicates the local network is down, not that a remote network is unreachable.

## Common Causes

- Network interface has been administratively disabled
- NetworkManager or systemd-networkd stopped the interface
- Physical disconnection of Ethernet cable
- Virtual machine network adapter is down

## How to Fix ENETDOWN

### 1. Check Network Interface Status

Verify which interfaces are up:

```bash
ip link show
ip -s link show
```

### 2. Bring Up the Network Interface

Enable the downed interface:

```bash
sudo ip link set eth0 up
sudo ifconfig eth0 up
```

### 3. Restart Network Services

Restart the networking stack:

```bash
sudo systemctl restart NetworkManager
sudo systemctl restart systemd-networkd
sudo systemctl restart networking
```

### 4. Check for Firewall Blocking

Ensure iptables or nftables is not blocking traffic:

```bash
sudo iptables -L
sudo nft list ruleset
```

### 5. Verify Physical Connection

Check the physical link status:

```bash
ethtool eth0
```

## Verification

After bringing the interface up, confirm connectivity:

```bash
ip link show eth0
ping -c 3 8.8.8.8
```

## Related Error Codes

- [ENETUNREACH (errno 65)](/os/linux/errno-65/) — Network is unreachable
- [ENONET (errno 49)](/os/linux/errno-49/) — Machine is not on the network
- [EHOSTUNREACH (errno 77)](/os/linux/errno-77/) — No route to host

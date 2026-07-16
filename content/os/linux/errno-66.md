---
title: "[Solution] Linux ENETRESET (errno 66) — Network Connection Reset Fix"
description: "Fix Linux ENETRESET (errno 66) Network connection reset error. Solutions for network reset and connection issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enetreset", "network", "errno-66", "reset", "connection"]
weight: 5
---

# Linux ENETRESET (errno 66) — Network Connection Reset

ENETRESET (errno 66) means the network connection was reset by the network subsystem. This error occurs when a network connection is forcibly closed by the networking layer, often due to a timeout, resource exhaustion, or hardware error on the network interface. It is distinct from ECONNRESET (errno 68) because ENETRESET refers to the network layer resetting the connection, not the remote peer.

## Common Causes

- Network hardware error caused connection reset
- Network interface buffer overflow
- TCP keepalive timeout on a stale connection
- Network driver encountering a fatal error

## How to Fix ENETRESET

### 1. Check Network Interface Errors

Look for hardware-level network errors:

```bash
ip -s link show
ethtool -S eth0 | grep -i error
```

### 2. Check Kernel Network Logs

Review kernel messages for network issues:

```bash
dmesg | grep -i "network\|eth0\|reset\|error"
```

### 3. Reset the Network Interface

Bring the interface down and back up:

```bash
sudo ip link set eth0 down
sudo ip link set eth0 up
```

### 4. Increase Network Buffer Sizes

Adjust kernel network buffer parameters:

```bash
sudo sysctl -w net.core.rmem_max=16777216
sudo sysctl -w net.core.wmem_max=16777216
```

### 5. Update Network Driver

Ensure the latest network driver is installed:

```bash
sudo apt update
sudo apt install --reinstall linux-modules-extra-$(uname -r)
```

## Verification

After resetting, confirm the connection works:

```bash
ip -s link show eth0
ping -c 10 target_host
```

## Related Error Codes

- [ECONNRESET (errno 68)](/os/linux/errno-68/) — Connection reset by peer
- [ENETDOWN (errno 64)](/os/linux/errno-64/) — Network is down
- [ETIMEDOUT (errno 74)](/os/linux/errno-74/) — Connection timed out

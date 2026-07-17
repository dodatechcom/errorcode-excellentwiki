---
title: "[Solution] Linux ENONET (errno 49) — Machine Is Not on the Network Fix"
description: "Fix Linux ENONET (errno 49) Machine is not on the network error. Solutions for network connectivity issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux ENONET (errno 49) — Machine Is Not on the Network

ENONET (errno 49) means the host is not connected to the network. This error occurs when a program attempts network communication but the machine has no active network connection. It is distinct from ENETUNREACH (errno 101) because ENONET indicates the local machine itself has no network interface active, not that a remote network is unreachable.

## Common Causes

- Network interface is down or not configured
- No Ethernet cable connected or Wi-Fi not associated
- Network manager has not brought up interfaces
- Virtual machine with no virtual network adapter

## How to Fix ENONET

### 1. Check Network Interface Status

Verify which interfaces are up:

```bash
ip link show
ifconfig -a
```

### 2. Bring Up the Network Interface

Enable the interface:

```bash
sudo ip link set eth0 up
```

### 3. Configure IP Address

Assign an IP address:

```bash
sudo ip addr add 192.168.1.100/24 dev eth0
```

### 4. Restart Network Manager

Restart networking services:

```bash
sudo systemctl restart NetworkManager
sudo systemctl restart networking
```

### 5. Check Physical Connection

Ensure the Ethernet cable is connected or Wi-Fi is associated:

```bash
iwconfig wlan0
sudo iwlist wlan0 scan | head -20
```

## Verification

After restoring connectivity, confirm:

```bash
ping -c 3 8.8.8.8
ip addr show
```

## Related Error Codes

- [ENETUNREACH (errno 65)](/os/linux/errno-65/) — Network is unreachable
- [ENETDOWN (errno 64)](/os/linux/errno-64/) — Network is down
- [EHOSTUNREACH (errno 77)](/os/linux/errno-77/) — No route to host

---
title: "[Solution] Linux: mtu-error — MTU configuration error"
description: "Fix Linux mtu-error errors. MTU configuration error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 6
---
# Linux: MTU Error

MTU (Maximum Transmission Unit) errors occur when a packet is too large for a network link and cannot be fragmented. This often appears as "Message too long" or connectivity issues with VPNs/tunnels.

## Common Causes

- VPN or tunnel interface has a lower MTU than the physical interface
- Path MTU discovery (PMTUD) disabled or ICMP blocked by firewall
- Jumbo frames enabled on switch but not on all devices in path
- PPPoE or other encapsulation overhead not accounted for
- Incorrect MTU setting on the interface

## How to Fix

### 1. Check Current MTU

```bash
ip link show | grep mtu
```

### 2. Test with Different Packet Sizes

```bash
# Test ping with specific MTU size
ping -M do -s 1472 google.com   # 1500 - 28 (IP+ICMP header)
ping -M do -s 1452 google.com   # 1492 - 40 (PPPoE overhead)
```

### 3. Change MTU on Interface

```bash
sudo ip link set eth0 mtu 1400
```

### 4. Change MTU for VPN Tunnel

```bash
sudo ip link set tun0 mtu 1400
```

### 5. Make Persistent

```bash
# For Netplan
sudo nano /etc/netplan/*.yaml
# Add: mtu: 1400
```

## Examples

```bash
$ ping -M do -s 1472 google.com
PING google.com (142.250.80.46) 56(84) bytes of data.
ping: local error: message too long, mtu=1500

$ ping -M do -s 1400 google.com
PING google.com (142.250.80.46) 56(84) bytes of data.
64 bytes from 142.250.80.46: icmp_seq=1 ttl=117 time=12.3 ms
```

---
title: "[Solution] Linux: link-local-error — link-local address error"
description: "Fix Linux link-local-error errors. link-local address error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 4
---
# Linux: Link-Local Address Error

Link-local address errors occur with IPv4 (169.254.x.x APIPA) or IPv6 (fe80::) addresses when the system cannot obtain a proper address from DHCP or router advertisement.

## Common Causes

- DHCP server unreachable or not responding
- Network interface configured for DHCP but no DHCP server available
- IPv6 router advertisement not received on the link
- Zeroconf/AVAHI conflicts with static IP configuration
- Network cable unplugged or switch port not forwarding

## How to Fix

### 1. Check Current Address

```bash
ip addr show
ip addr show | grep -E "169\.254|fe80"
```

### 2. Restart DHCP Client

```bash
sudo dhclient -v eth0
sudo dhcpcd eth0
```

### 3. Check DHCP Service

```bash
# Check if DHCP server is running
sudo systemctl status dhcpd
sudo systemctl status isc-dhcp-server
```

### 4. Assign Static IP (Temporary)

```bash
sudo ip addr add 192.168.1.100/24 dev eth0
sudo ip route add default via 192.168.1.1
```

## Examples

```bash
$ ip addr show eth0
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 169.254.12.34/16 brd 169.255.255.255 scope link eth0

$ sudo dhclient -v eth0
Listening on LPF/eth0/00:11:22:33:44:55
DHCPDISCOVER on eth0 to 255.255.255.255 port 67 interval 3
DHCPOFFER from 192.168.1.1
DHCPREQUEST on eth0 to 255.255.255.255 port 67
DHCPACK from 192.168.1.1
bound to 192.168.1.100 -- renewal in 3600 seconds.
```

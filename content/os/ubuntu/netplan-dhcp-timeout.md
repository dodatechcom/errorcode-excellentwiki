---
title: "[Solution] Ubuntu Server: netplan-dhcp-timeout"
description: "Fix Ubuntu netplan-dhcp-timeout. Netplan DHCP request times out without obtaining an IP."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Netplan DHCP Timeout

netplan fails to obtain an IP address via DHCP.

## Common Causes
- DHCP server unreachable on the network
- Network cable disconnected
- VLAN tagging required but not configured
- Firewall blocking DHCP packets

## How to Fix
1. Check link status
```bash
ip link show
ip addr show
```
2. Set static IP as fallback
```bash
sudo nano /etc/netplan/00-installer-config.yaml
```
3. Force DHCP re-request
```bash
sudo dhclient -v <interface>
```

## Examples
```bash
$ ip link show eth0
2: eth0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 state DOWN

$ sudo dhclient -v eth0
DHCPDISCOVER on eth0 to 255.255.255.255 port 67 interval 8
```

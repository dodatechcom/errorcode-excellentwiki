---
title: "[Solution] Linux: mac-address-error — MAC address configuration error"
description: "Fix Linux mac-address-error errors. MAC address configuration error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 6
---
# Linux: MAC Address Error

MAC address errors occur when the network interface's MAC address is invalid, duplicated, or blocked.

## Common Causes

- MAC address filtering on switch or router blocking the interface
- Duplicate MAC address on the network
- MAC address spoofing or change that conflicts
- Interface driver reporting an invalid or zero MAC
- MAC address not assigned to virtual interface

## How to Fix

### 1. Check Current MAC Address

```bash
ip link show eth0
cat /sys/class/net/eth0/address
```

### 2. Check for Duplicate MACs

```bash
# Scan network for duplicate MACs
arp-scan --local
```

### 3. Change MAC Address (Temporary)

```bash
sudo ip link set eth0 down
sudo ip link set eth0 address 00:11:22:33:44:55
sudo ip link set eth0 up
```

### 4. Make MAC Change Permanent

```bash
# Create systemd link file
cat <<EOF | sudo tee /etc/systemd/network/10-eth0.link
[Match]
MACAddress=original:mac:address

[Link]
MACAddress=new:mac:address
EOF
```

## Examples

```bash
$ cat /sys/class/net/eth0/address
00:00:00:00:00:00

$ sudo ip link set eth0 down
$ sudo ip link set eth0 address 00:11:22:33:44:55
$ sudo ip link set eth0 up
$ cat /sys/class/net/eth0/address
00:11:22:33:44:55
```

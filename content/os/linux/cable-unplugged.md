---
title: "[Solution] Linux: cable-unplugged — network cable unplugged"
description: "Fix Linux cable-unplugged errors. network cable unplugged with these solutions."
platforms: ["linux"]
severities: ["info"]
error-types: ["network"]
weight: 4
---
# Linux: Cable Unplugged (No Link)

A "cable unplugged" network error indicates the physical network connection is down, with no carrier signal detected.

## Common Causes

- Ethernet cable disconnected or not fully seated
- Switch port powered off or disabled
- Damaged Ethernet cable (cut, crushed, chewed by rodents)
- Network interface disabled or in bad state
- Port security or VLAN mismatch on switch

## How to Fix

### 1. Check Interface State

```bash
ip link show
cat /sys/class/net/eth0/carrier
cat /sys/class/net/eth0/operstate
```

### 2. Check Link Status

```bash
sudo ethtool eth0
sudo mii-tool eth0
```

### 3. Attempt to Bring Up Interface

```bash
sudo ip link set eth0 up
sudo dhclient eth0
```

### 4. Check Physical Connection

Verify cable is securely connected at both ends. Try a known-good cable.

### 5. Check Switch Port

Verify the switch port is enabled and not error-disabled.

## Examples

```bash
$ ip link show eth0
2: eth0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT group default qlen 1000

$ cat /sys/class/net/eth0/carrier
0

$ sudo ethtool eth0
Settings for eth0:
        Supported ports: [ TP ]
        Supported link modes:   10baseT/Half 10baseT/Full 
                                100baseT/Half 100baseT/Full 
                                1000baseT/Full 
        Advertised link modes:  10baseT/Half 10baseT/Full 
        Link detected: no
```

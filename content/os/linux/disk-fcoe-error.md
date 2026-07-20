---
title: "[Solution] Linux: disk-fcoe-error — FCoE disk error"
description: "Fix Linux disk-fcoe-error errors. FCoE disk error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 8
---
# Linux: FCoE Error

FCoE (Fibre Channel over Ethernet) errors indicate problems with SAN connectivity over Ethernet networks.

## Common Causes

- FCoE-capable switch not configured with dedicated FCoE VLAN
- DCB (Data Center Bridging) not enabled on the network interface
- FIP (FCoE Initialization Protocol) timeout during fabric login
- Interface driver does not support FCoE offload
- Fibre Channel zoning or LUN masking misconfiguration

## How to Fix

### 1. Check FCoE Interfaces and Sessions

```bash
sudo fcoeadm -i
sudo fcoeadm -s
```

### 2. Enable FCoE on Interface

```bash
sudo fipvlan -c -s <interface>
```

### 3. Check DCB Configuration

```bash
sudo lldptool -t -i <interface> -V PFC
sudo lldptool -t -i <interface> -V ETS
```

### 4. Check Kernel Messages

```bash
dmesg | grep -iE "fcoe|fip|dcb" | tail -20
```

## Examples

```bash
$ sudo fcoeadm -i
    Interface:          eth2
    Fabric:             20:01:00:11:22:33:44:55:66
    State:              Connected

$ sudo fcoeadm -s
    Interface:          eth2
    State:              Connected
    Fabric FCFs:        1
```

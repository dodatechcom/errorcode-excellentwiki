---
title: "[Solution] macOS Ethernet Error — Wired Network Not Working"
description: "Fix macOS Ethernet error: Ethernet not detected, self-assigned IP, Ethernet cable connected but no internet, no Ethernet icon in menu bar."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 169
---

# Ethernet Error — Wired Network Not Working

Fix macOS Ethernet error: Ethernet not detected, self-assigned IP, Ethernet cable connected but no internet, no Ethernet icon in menu bar.

## Common Causes

- Ethernet cable damaged or not fully seated in port
- Ethernet adapter or USB-C dongle incompatible with macOS
- DHCP server not assigning IP address to Mac
- Network switch or router Ethernet port failure

## How to Fix

### 1. Check Ethernet Connection Status

```bash
ifconfig en0 | grep 'status'
networksetup -getinfo Ethernet
system_profiler SPNetworkDataType
```

### 2. Renew DHCP Lease

```bash
sudo ipconfig set en0 DHCP
# Or System Settings → Network → Ethernet → Details → TCP/IP → Renew DHCP Lease
```

### 3. Reset Ethernet Interface

```bash
sudo ifconfig en0 down
sudo ifconfig en0 up
sudo networksetup -setmanual Ethernet 192.168.1.100 255.255.255.0 192.168.1.1
```

### 4. Check Ethernet Cable and Port

```bash
# Try different Ethernet cable
# Try different port on router/switch
# Test with another device to rule out cable/port issues
```

## Common Scenarios

This error commonly occurs when:

- Ethernet shows 'Cable Unplugged' even though cable is connected
- Self-Assigned IP address 169.254.x.x appearing instead of DHCP
- Ethernet connected but no internet access through wired connection
- Ethernet icon not appearing in menu bar despite cable connection

## Prevent It

- Use quality Cat6 or Cat6a cables for reliable Ethernet connections
- Test Ethernet cable with another device to rule out cable failure
- Update macOS for latest Ethernet adapter compatibility
- Keep router Ethernet ports clean and free of debris

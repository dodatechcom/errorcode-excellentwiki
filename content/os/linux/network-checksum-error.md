---
title: "[Solution] Linux: network-checksum-error -- checksum offload error"
description: "Fix Linux network checksum errors. Hardware checksum offload malfunction causing packet drops."
os: ["linux"]
error-types: ["network-error"]
severities: ["error"]
---

# Linux: Network Checksum Error

Network checksum errors occur when packet checksums are computed incorrectly.

## Common Causes

- Hardware checksum offload malfunctioning on NIC
- Driver bug miscalculating TCP/IP checksums
- Virtual machine NIC not handling offload correctly
- Corrupted packet data in transit
- MTU mismatch causing partial packet corruption

## How to Fix

### 1. Check for Errors

```bash
ethtool -S eth0 | grep -i checksum
ip -s link show eth0
ethtool -k eth0 | grep -E "checksum|offload"
```

### 2. Disable Hardware Offload

```bash
sudo ethtool -K eth0 tx off rx off
sudo ethtool -K eth0 tx-checksum-ipv4 off
```

### 3. Update NIC Driver

```bash
lspci | grep -i ethernet
sudo apt install firmware-iwlwifi 2>/dev/null
```

## Examples

```bash
$ ethtool -k eth0 | grep checksum
tx-checksum-ipv4: on
rx-checksum-ipv4: on
$ sudo ethtool -K eth0 tx off
Actual changes:
tx-checksum-ipv4: off
```

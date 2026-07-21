---
title: "[Solution] Ubuntu Server: ubuntu-multipass-bridge-error"
description: "Fix Ubuntu ubuntu-multipass-bridge-error. Multipass bridged networking fails."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Multipass Bridge Error

Multipass bridged networking fails to connect VMs to physical network.

## Common Causes
- Bridge interface not created
- Host bridge not configured
- DHCP server not responding on bridge

## How to Fix
1. Check Multipass network
```bash
multipass networks
```
2. Set bridged interface
```bash
multipass set local.bridged-network=<interface>
```
3. Launch bridged VM
```bash
multipass launch --network bridged
```

## Examples
```bash
$ multipass networks
Name        Type     IPv4            IPv6
multipass0   bridge   10.72.228.1     --
```
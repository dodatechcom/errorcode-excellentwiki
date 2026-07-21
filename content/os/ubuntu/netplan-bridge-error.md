---
title: "[Solution] Ubuntu Server: netplan-bridge-error"
description: "Fix Ubuntu netplan-bridge-error. Network bridge fails to create or forward traffic."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Netplan Bridge Error

Network bridge fails to create or forward traffic.

## Common Causes
- bridge module not loaded
- Member interface configured elsewhere
- STP conflict with upstream switch
- Bridge loop detected

## How to Fix
1. Check bridge status
```bash
brctl show
ip link show type bridge
```
2. Load bridge module
```bash
sudo modprobe br_netfilter
```
3. Verify netplan bridge config
```bash
sudo netplan generate
```

## Examples
```bash
$ brctl show
bridge name   bridge id           STP enabled   interfaces
br0           8000.aabbccddeeff   no            eth0
                                              eth1
```

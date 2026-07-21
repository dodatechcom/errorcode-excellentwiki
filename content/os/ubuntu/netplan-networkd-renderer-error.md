---
title: "[Solution] Ubuntu Server: netplan-networkd-renderer-error"
description: "Fix Ubuntu netplan-networkd-renderer-error. netplan fails to generate networkd units."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Netplan Networkd Renderer Error

netplan fails to generate valid networkd unit files.

## Common Causes
- Invalid YAML syntax
- networkd does not support configured option
- systemd-networkd version too old
- Conflicting renderer between files

## How to Fix
1. Check generated unit files
```bash
ls /run/systemd/network/
```
2. Verify networkd version
```bash
systemctl --version
```
3. Generate config manually
```bash
sudo netplan generate
sudo networkctl status
```

## Examples
```bash
$ sudo netplan generate
$ ls /run/systemd/network/
10-netplan-eth0.network

$ sudo networkctl status
● 2: eth0
      State: configured
```

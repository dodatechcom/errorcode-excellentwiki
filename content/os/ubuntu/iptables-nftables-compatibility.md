---
title: "[Solution] Ubuntu Server: iptables-nftables-compatibility"
description: "Fix Ubuntu iptables-nftables-compatibility. iptables and nftables conflict on Ubuntu."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Iptables Nftables Compatibility

iptables and nftables backends conflict causing firewall issues.

## Common Causes
- Ubuntu 20.04+ uses nftables by default
- iptables-legacy and iptables-nft both present
- UFW using wrong backend
- Rules not visible in both tools

## How to Fix
1. Check which backend is active
```bash
sudo iptables --version
sudo update-alternatives --display iptables
```
2. Switch to iptables-legacy if needed
```bash
sudo update-alternatives --set iptables /usr/sbin/iptables-legacy
sudo update-alternatives --set ip6tables /usr/sbin/ip6tables-legacy
```
3. Or migrate to nftables
```bash
sudo nft list ruleset
```

## Examples
```bash
$ sudo iptables --version
iptables v1.8.7 (nf_tables)

$ sudo update-alternatives --set iptables /usr/sbin/iptables-legacy
$ sudo iptables --version
iptables v1.8.7 (legacy)
```

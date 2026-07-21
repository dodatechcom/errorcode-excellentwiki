---
title: "[Solution] Ubuntu Server: ubuntu-kernel-nf-drop-error"
description: "Fix Ubuntu ubuntu-kernel-nf-drop-error. Netfilter/nftables packet drops cause connectivity loss."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Kernel NF Drop Error

Netfilter/nftables packet drops cause connectivity loss.

## Common Causes
- Drop rules too aggressive
- Default policy set to DROP
- Missing ACCEPT rules for established connections

## How to Fix
1. Check nftables rules
```bash
sudo nft list ruleset
```
2. Add established connection rule
```bash
sudo nft add rule inet filter input ct state established,related accept
```
3. Check packet counters
```bash
sudo nft list ruleset -a | grep counter
```

## Examples
```bash
$ sudo nft list ruleset
table inet filter {
    chain input {
        type filter hook input priority 0; policy drop;
        ct state established,related accept
    }
}
```
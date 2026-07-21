---
title: "[Solution] Ubuntu Server: nftables-set-ops-error"
description: "Fix Ubuntu nftables-set-ops-error. nftables set operations fail or rules not matching."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Nftables Set Ops Error

nftables set operations fail or rules do not match traffic.

## Common Causes
- Set type mismatch (ipv4_addr vs ipv6_addr)
- Timeout not supported in older nftables
- Element not added to set
- Set not referenced by rule

## How to Fix
1. List current sets
```bash
sudo nft list ruleset
```
2. Add elements to set
```bash
sudo nft add element inet filter blocked_ips { 1.2.3.4 }
```
3. Check set type
```bash
sudo nft list set inet filter blocked_ips
```

## Examples
```bash
$ sudo nft list ruleset
table inet filter {
    set blocked_ips {
        type ipv4_addr
        elements = { 1.2.3.4, 5.6.7.8 }
    }
}

$ sudo nft add element inet filter blocked_ips { 9.10.11.12 }
```

---
title: "[Solution] Linux: nftables-set-error -- nftables set error"
description: "Fix Linux nftables set errors. Nftables set element or table configuration error."
os: ["linux"]
error-types: ["firewall-error"]
severities: ["error"]
---

# Linux: Nftables Set Error

Nftables set errors occur when set elements cannot be added or matched.

## Common Causes

- Set type mismatch (IPv4 in IPv6 set)
- Maximum set element count exceeded
- Set interval flags conflicting with types
- Timeout values out of supported range
- Named set referenced before definition

## How to Fix

### 1. Check Current Sets

```bash
sudo nft list ruleset
sudo nft list sets
sudo nft list table inet filter
```

### 2. Fix Set Configuration

```bash
sudo nft delete set inet filter blocked_ips
sudo nft add set inet filter blocked_ips { type ipv4_addr\; flags interval\; }
sudo nft add element inet filter blocked_ips { 192.168.1.100 }
```

### 3. Verify Rules

```bash
sudo nft -a list ruleset
sudo nft list chain inet filter input
```

## Examples

```bash
$ sudo nft add element inet filter blocked_ips { 192.168.1.100 }
Error: could not add set element: Invalid argument
$ sudo nft list sets
table inet filter {
    set blocked_ips {
        type ipv4_addr
        flags interval
    }
}
```

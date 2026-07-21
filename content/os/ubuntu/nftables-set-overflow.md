---
title: "Nftables Set Element Limit Reached"
description: "Nftables set/hash table reaches maximum element count"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Nftables Set Element Limit Reached

Nftables set/hash table reaches maximum element count

## Common Causes

- Set element limit (65535) reached for IP set
- Large IP blacklist exceeding set capacity
- Hash table bucket size insufficient
- Elements not being cleaned up from set

## How to Fix

1. Check set size: `sudo nft list ruleset | grep elements`
2. Split large sets across multiple tables
3. Use interval sets for IP ranges
4. Increase hash limit: `elements limit over 100000`

## Examples

```bash
# Check set elements
sudo nft list set inet filter myset

# Count elements
sudo nft list set inet filter myset | grep -c element
```

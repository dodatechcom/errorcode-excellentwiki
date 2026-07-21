---
title: "Nftables Counter Statistics Error"
description: "Nftables counters not counting or resetting unexpectedly"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Nftables Counter Statistics Error

Nftables counters not counting or resetting unexpectedly

## Common Causes

- Counter rule removed and re-added causing reset
- Counter not attached to correct chain
- Multiple counters conflicting
- Counter data lost due to ruleset flush

## How to Fix

1. Check counters: `sudo nft list ruleset | grep counter`
2. Add counter: `nft add rule inet filter input counter accept`
3. Read counter: `nft list chain inet filter input`
4. Note: counters reset on rule removal or ruleset flush

## Examples

```bash
# Add rule with counter
sudo nft add rule inet filter input tcp port 22 counter accept

# Read counter values
sudo nft list chain inet filter input

# Check specific counter
sudo nft list chain inet filter input | grep counter
```

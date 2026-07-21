---
title: "Ubuntu Zswap Compressed Swap Error"
description: "Zswap compressed swap cache not functioning or causing issues"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Zswap Compressed Swap Error

Zswap compressed swap cache not functioning or causing issues

## Common Causes

- Zswap not enabled in kernel boot parameters
- Compressor algorithm not available
- Zpool backend not configured
- Max pool size exceeded

## How to Fix

1. Check zswap: `cat /sys/module/zswap/parameters/*`
2. Enable: add `zswap.enabled=1` to kernel boot params
3. Set compressor: `echo lz4 | sudo tee /sys/module/zswap/parameters/compressor`
4. Check stats: `cat /proc/meminfo | grep Zswap`

## Examples

```bash
# Check zswap status
cat /sys/module/zswap/parameters/enabled

# Enable zswap
echo 1 | sudo tee /sys/module/zswap/parameters/enabled

# Check zswap statistics
grep -i zswap /proc/meminfo
```

---
title: "Ubuntu ZRAM Compression Error"
description: "ZRAM compressed swap device fails or performs poorly"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu ZRAM Compression Error

ZRAM compressed swap device fails or performs poorly

## Common Causes

- ZRAM module not loaded in kernel
- Compression algorithm not available
- ZRAM device size exceeds available memory
- Compiling in low-memory situation causes OOM

## How to Fix

1. Check ZRAM: `ls /dev/zram*`
2. Load module: `sudo modprobe zram`
3. Set up ZRAM: `echo lz4 | sudo tee /sys/block/zram0/comp_algorithm`
4. Check status: `zramctl`

## Examples

```bash
# Check ZRAM status
zramctl

# Set up ZRAM manually
sudo modprobe zram
echo lz4 | sudo tee /sys/block/zram0/comp_algorithm
echo 4G | sudo tee /sys/block/zram0/disksize
sudo mkswap /dev/zram0
sudo swapon -p 100 /dev/zram0
```

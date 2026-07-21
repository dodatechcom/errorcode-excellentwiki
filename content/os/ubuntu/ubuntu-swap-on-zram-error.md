---
title: "[Solution] Ubuntu Server: ubuntu-swap-on-zram-error"
description: "Fix Ubuntu ubuntu-swap-on-zram-error. zram swap device fails or performs poorly."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Swap On Zram Error

zram-based swap fails or does not provide expected compression.

## Common Causes
- zram module not loaded
- Algorithm not supported
- zram size too small

## How to Fix
1. Check zram status
```bash
swapon --show
ls /dev/zram*
```
2. Load zram module
```bash
sudo modprobe zram
sudo modprobe zstd
```
3. Configure zram
```bash
echo zstd | sudo tee /sys/block/zram0/comp_algorithm
echo 4G | sudo tee /sys/block/zram0/disksize
sudo mkswap /dev/zram0
sudo swapon -p 100 /dev/zram0
```

## Examples
```bash
$ swapon --show
NAME      ALGORITHM DISKSIZE  DATA  COMPR  TOTAL
/dev/zram0 zstd         4G   32M   8M     10M
```
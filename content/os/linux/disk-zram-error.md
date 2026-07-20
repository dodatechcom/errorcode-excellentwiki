---
title: "[Solution] Linux: disk-zram-error — zram compression error"
description: "Fix Linux disk-zram-error errors. zram compression error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 6
---
# Linux: ZRAM Error

ZRAM errors occur with compressed RAM block devices used for swap or temporary storage.

## Common Causes

- ZRAM kernel module not loaded or not supported by kernel
- Insufficient RAM to allocate the ZRAM device of requested size
- Compression algorithm (lzo, lz4, zstd) not available in kernel
- Memory pressure causing thrashing in compressed swap
- Improper ZRAM configuration

## How to Fix

### 1. Check ZRAM Status

```bash
zramctl
cat /proc/swaps | grep zram
```

### 2. Load ZRAM Module

```bash
sudo modprobe zram
```

### 3. Configure ZRAM

```bash
# Set size to 50% of RAM
echo $(( $(free -b | grep Mem | awk '{print $2}') / 2 )) | sudo tee /sys/block/zram0/disksize
sudo mkswap /dev/zram0
sudo swapon -p 100 /dev/zram0
```

### 4. Change Compression Algorithm

```bash
cat /sys/block/zram0/comp_algorithm
echo zstd | sudo tee /sys/block/zram0/comp_algorithm
```

## Examples

```bash
$ zramctl
NAME       ALGORITHM DISKSIZE  DATA  COMPR TOTAL STREAMS MOUNTPOINT
/dev/zram0 lz4           7.5G  2.1G 331.2M  667M       4 [SWAP]

$ cat /proc/swaps
Filename                Type        Size        Used        Priority
/dev/zram0              partition   7812500     1234567     100
```

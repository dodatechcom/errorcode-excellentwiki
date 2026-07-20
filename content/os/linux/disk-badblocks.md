---
title: "[Solution] Linux: disk-badblocks — disk bad blocks error"
description: "Fix Linux disk-badblocks errors. disk bad blocks error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 8
---
# Linux: Bad Blocks on Disk

Bad blocks (bad sectors) are physical defects on a hard drive surface where data cannot be reliably stored or retrieved.

## Common Causes

- Normal wear and tear on aging magnetic media
- Head crashes where the read/write head contacts the platter
- Manufacturing defects that develop over time
- Physical shock or vibration during operation
- Power surges damaging the drive electronics or media

## How to Fix

### 1. Scan for Bad Blocks

```bash
# Read-only scan (safe)
sudo badblocks -sv /dev/sdX
```

### 2. Map Bad Blocks with fsck

```bash
sudo fsck -fcc /dev/sdX
```

### 3. Check SMART for Bad Sectors

```bash
sudo smartctl -A /dev/sdX | grep -E "Reallocated|Pending|Uncorrectable"
```

### 4. Recover Data

```bash
sudo ddrescue -d -r3 /dev/sdX /dev/sdY /tmp/rescue.log
```

### 5. Create Bad Block Map for mkfs

```bash
sudo badblocks -o /tmp/badblocks.txt /dev/sdX
sudo mkfs.ext4 -l /tmp/badblocks.txt /dev/sdX
```

## Examples

```bash
$ sudo badblocks -sv /dev/sda
Checking blocks 0 to 976762584
Checking for bad blocks (read-only test): done
Pass completed, 17 bad blocks found. (17/0/0 errors)

$ sudo smartctl -A /dev/sda | grep Reallocated
  5 Reallocated_Sector_Ct  0x0033   010   010   036    Pre-fail  Always  FAILING_NOW 245
```

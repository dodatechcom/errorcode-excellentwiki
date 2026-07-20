---
title: "[Solution] Linux: disk-ssd-error — SSD disk error"
description: "Fix Linux disk-ssd-error errors. SSD disk error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 8
---
# Linux: SSD Error

SSD errors indicate problems specific to solid-state drives, including NAND flash wear, controller failure, or interface issues.

## Common Causes

- NAND flash wear beyond rated endurance (TBW exceeded)
- Controller firmware bugs or hardware failure
- Power loss causing mapping table corruption
- Overheating causing throttling or data corruption
- TRIM/unmap operation failures degrading performance

## How to Fix

### 1. Check SSD Health

```bash
sudo smartctl -a /dev/sdX | grep -E "Percent_Life|Wear_Level|Media_Wearout|Total_LBAs_Written"
```

### 2. Check NVMe SMART

```bash
sudo nvme smart-log /dev/nvme0
```

### 3. Check TRIM Support

```bash
lsblk -D
sudo fstrim -v /
sudo fstrim -av
```

### 4. Check Remaining Life

```bash
sudo smartctl -A /dev/sdX | grep -i "percent\|used"
```

## Examples

```bash
$ sudo smartctl -A /dev/sda | grep -iE "wear|life|used"
233 Media_Wearout_Indicator  0x0032   100   100   000    Old_age   Always       -       0
231 SSD_Life_Left             0x0032   100   100   010    Old_age   Always       -       100

$ sudo nvme smart-log /dev/nvme0 | grep "percentage"
percentage_used                     : 5%
```

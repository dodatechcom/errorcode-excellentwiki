---
title: "[Solution] Linux: disk-smart-attribute — disk SMART attribute error"
description: "Fix Linux disk-smart-attribute errors. disk SMART attribute error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 8
---
# Linux: SMART Attribute Threshold Exceeded

SMART attribute threshold exceeded errors indicate a specific drive health metric has crossed its critical threshold, signaling likely failure.

## Common Causes

- Wear leveling indicator exceeding threshold (on SSDs)
- Temperature reading exceeding the drive's critical temperature
- Read error rate degradation beyond acceptable limits
- Reallocated sector count exceeding manufacturer threshold
- Power-on hours approaching drive design lifetime

## How to Fix

### 1. Identify Failing Attribute

```bash
sudo smartctl -A /dev/sdX | grep -i "failed"
sudo smartctl -l error /dev/sdX
```

### 2. View All Attributes with Thresholds

```bash
sudo smartctl -a /dev/sdX | grep -A 100 "SMART Attributes"
```

### 3. Run Extended Test

```bash
sudo smartctl -t long /dev/sdX
sudo smartctl -l selftest /dev/sdX
```

### 4. Backup Data

```bash
sudo rsync -av --progress /source/ /backup/destination/
```

## Examples

```bash
$ sudo smartctl -A /dev/sda | head -20
ID# ATTRIBUTE_NAME          FLAG     VALUE WORST THRESH TYPE      UPDATED  WHEN_FAILED RAW_VALUE
  5 Reallocated_Sector_Ct   0x0033   036   036   036    Pre-fail  Always   FAILING_NOW 245
197 Current_Pending_Sector  0x0032   100   100   000    Old_age   Always       -       150
```

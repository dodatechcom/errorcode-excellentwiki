---
title: "[Solution] Linux: disk-smart-error — disk SMART predictive failure"
description: "Fix Linux disk-smart-error errors. disk SMART predictive failure with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["disk"]
weight: 12
---
# Linux: SMART Error

SMART (Self-Monitoring, Analysis and Reporting Technology) errors indicate a storage device has detected conditions predicting imminent failure. These are critical early warnings.

## Common Causes

- Reallocated sector count increasing — drive remapping bad sectors
- Current pending sector count growing — sectors awaiting reallocation
- Uncorrectable sector count — sectors that could not be read at all
- Raw read error rate degradation — read/write head issues
- Drive exceeding rated workload or age limits

## How to Fix

### 1. Check Overall Health

```bash
sudo smartctl -H /dev/sdX
```

### 2. View Critical Attributes

```bash
sudo smartctl -A /dev/sdX | grep -E "Reallocated|Pending|Uncorrectable|CRC|Wear"
```

### 3. Run SMART Tests

```bash
# Short test (~2 minutes)
sudo smartctl -t short /dev/sdX

# Long test (hours)
sudo smartctl -t long /dev/sdX

# Check results
sudo smartctl -l selftest /dev/sdX
```

### 4. Backup Immediately

```bash
# Clone failing drive 
sudo ddrescue -d -r3 /dev/sdX /dev/sdY /tmp/rescue.log
```

## Examples

```bash
$ sudo smartctl -H /dev/sda
SMART overall-health self-assessment test result: FAILED
Drive failure expected in less than 24 hours. SAVE ALL DATA.

$ sudo smartctl -A /dev/sda | grep -E "Reallocated|Pending"
  5 Reallocated_Sector_Ct    0x0033   010   010   036    Pre-fail  Always  FAILING_NOW 245
197 Current_Pending_Sector   0x0032   100   100   000    Old_age   Always       -       150
```

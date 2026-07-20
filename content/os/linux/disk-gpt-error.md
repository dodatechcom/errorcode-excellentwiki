---
title: "[Solution] Linux: disk-gpt-error — GPT partition table error"
description: "Fix Linux disk-gpt-error errors. GPT partition table error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 8
---
# Linux: GPT Partition Table Error

GPT (GUID Partition Table) errors occur when the modern partition table format is corrupt. GPT uses primary and backup tables for redundancy.

## Common Causes

- GPT header or partition entry array corruption
- Primary and backup GPT tables do not match
- Protective MBR (0xEE partition) missing or incorrect
- Disk size mismatch in GPT header
- Corrupted partition entries after improper power-off

## How to Fix

### 1. Check GPT Status

```bash
sudo gdisk -l /dev/sdX
sudo parted /dev/sdX print
```

### 2. Verify and Repair with gdisk

```bash
sudo gdisk /dev/sdX
# v (verify), w (write if repairs needed)
```

### 3. Restore Backup GPT

```bash
sudo gdisk /dev/sdX
# r (recovery), b (use backup GPT), w (write)
```

### 4. Use sgdisk

```bash
sudo sgdisk -v /dev/sdX
```

## Examples

```bash
$ sudo gdisk -l /dev/sda
Warning! Disk size is smaller than the main header indicates!
Loading may result in partition table corruption.

$ sudo sgdisk -v /dev/sda
The main header's size is too large.
The backup header's size is too large.
The MBR is corrupt! The MBR is required to protect GPT.
```

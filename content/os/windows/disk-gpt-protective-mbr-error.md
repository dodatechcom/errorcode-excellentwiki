---
title: "[Solution] GPT Protective MBR Error Fix"
description: "Fix GPT protective MBR partition table error on Windows. Resolve disk showing as unknown or unreadable due to GPT protective partition entries."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] GPT Protective MBR Error Fix

A GPT protective MBR error occurs when a GPT disk is read by a tool that only understands MBR partition tables. The disk appears as a single protective partition and all data seems inaccessible.

## Common Causes
- BIOS configured for Legacy/CSM boot mode reading a GPT disk
- Third-party partition tool misinterpreting GPT structure
- Disk converted from MBR to GPT while BIOS is in Legacy mode
- USB enclosure firmware not supporting GPT
- Disk connected to a system with outdated storage drivers

## How to Fix

### Solution 1: Switch BIOS to UEFI Mode

Enter BIOS setup and change the boot mode from Legacy/CSM to UEFI.

### Solution 2: Use Diskpart to Inspect

```cmd
diskpart
list disk
select disk X
detail disk
```

### Solution 3: Convert to MBR (Data Loss Warning)

```cmd
diskpart
select disk X
clean
convert mbr
```

This destroys all data on the disk.

### Solution 4: Use GPT-Aware Tools

Use diskpart, Disk Management, or third-party GPT-aware tools to manage the disk.

### Solution 5: Update BIOS and Storage Drivers

Update your motherboard BIOS and storage controller drivers to properly support GPT disks.

## Examples
```powershell
Get-Disk | Select-Object Number, FriendlyName, PartitionStyle, Size
```

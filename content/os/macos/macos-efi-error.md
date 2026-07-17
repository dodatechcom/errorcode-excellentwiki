---
title: "[Solution] macOS EFI Boot Error"
description: "Fix EFI boot errors on Mac when the Mac fails to load the EFI partition, shows 'No bootable device,' or gets stuck before loading macOS."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# macOS EFI Boot Error Fix

EFI boot errors prevent the Mac from loading the Extensible Firmware Interface, which is responsible for handing off control from firmware to the OS. The Mac may show a blinking folder or refuse to boot entirely.

## What This Error Means

The EFI partition contains the boot loader and NVRAM data. When it's corrupt, the Mac cannot find or load the macOS kernel. This is different from firmware errors — the hardware POSTs successfully but can't find a bootable OS.

## Common Causes

- Corrupt EFI partition
- NVRAM data pointing to incorrect boot volume
- Disk partition map damage
- Failed macOS update that modified boot records
- APFS container corruption

## How to Fix

### 1. Reset NVRAM

```bash
# Shut down Mac
# Turn on and immediately hold Option+Command+P+R for 20 seconds
# This resets boot-related NVRAM variables
```

### 2. Rebuild the EFI boot partition

```bash
# Boot into Recovery Mode
# Open Terminal from Utilities menu

# List disks and partitions
diskutil list

# Rebuild the EFI partition (CAUTION: backup first)
diskutil eraseVolume FAT32 EFI /dev/disk0s1
```

### 3. Fix the APFS container

```bash
# From Recovery Terminal
diskutil apfs list
diskutil apfs repair /dev/disk3
```

### 4. Check and repair the boot volume

```bash
# From Recovery
diskutil verifyVolume /
diskutil repairVolume /
```

## Related Errors

- [Firmware Error](macos-firmware-error) — firmware-level corruption
- [Boot Error](macos-boot-error) — general boot failures
- [Disk Utility Error](disk-utility-error) — disk repair errors

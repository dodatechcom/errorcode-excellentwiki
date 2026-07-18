---
title: "[Solution] macOS Disk Convert Error — Cannot Convert from HFS+ to APFS"
description: "Fix macOS disk conversion failure: cannot convert disk from HFS+ to APFS, conversion interrupted or failed, APFS option not available."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 136
---

# Disk Convert Error — Cannot Convert from HFS+ to APFS

Fix macOS disk conversion failure: cannot convert disk from HFS+ to APFS, conversion interrupted or failed, APFS option not available.

## Common Causes

- Disk has too little free space for APFS conversion operation
- FileVault encryption must be disabled before conversion
- Third-party partition manager conflicting with conversion
- Disk contains bad blocks preventing safe conversion

## How to Fix

### 1. Check Disk Free Space and Prepare

```bash
df -h /Volumes/DiskName
diskutil info /Volumes/DiskName | grep 'File System'
sudo fdesetup status
```

### 2. Convert to APFS from Disk Utility

```bash
# Edit → Convert to APFS (non-destructive operation)
```

### 3. Convert Using Command Line

```bash
sudo diskutil apfs resizeContainer disk2s1 0
# WARNING for full conversion: sudo diskutil eraseDisk APFS NewVolume disk2
```

### 4. Back Up and Convert from Recovery

```bash
# 1. Back up all data
# 2. Boot into Recovery (Command+R)
# 3. Erase disk with APFS format
# 4. Restore data from backup
```

## Common Scenarios

This error commonly occurs when:

- Convert to APFS option grayed out in Disk Utility Edit menu
- APFS conversion fails partway through with error message
- Conversion process hangs at same percentage for hours
- APFS option not appearing for HFS+ formatted startup disk

## Prevent It

- Back up disk before attempting any file system conversion
- Ensure at least 10% free space before starting APFS conversion
- Disable FileVault encryption before converting file systems
- Convert to APFS during initial setup rather than later

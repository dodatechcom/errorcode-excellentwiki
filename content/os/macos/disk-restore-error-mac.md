---
title: "[Solution] macOS Disk Restore Error — Disk Utility Restore Operation Fails"
description: "Fix macOS disk restore failure: Disk Utility restore operation fails, disk image cannot be restored to volume, restore process hangs."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 146
---

# Disk Restore Error — Disk Utility Restore Operation Fails

Fix macOS disk restore failure: Disk Utility restore operation fails, disk image cannot be restored to volume, restore process hangs.

## Common Causes

- Source disk image corruption preventing restore
- Destination disk has errors blocking write operations
- Insufficient disk space on destination for restore
- USB connection dropping during restore operation

## How to Fix

### 1. Check Source and Destination Disks

```bash
diskutil list
diskutil info disk2 | grep 'Protocol'
```

### 2. Verify Disk Image Integrity

```bash
hdiutil verify /path/to/image.dmg
hdiutil attach /path/to/image.dmg
```

### 3. Repair Destination Disk Before Restore

```bash
# Recovery → Disk Utility → Select destination → First Aid
diskutil eraseDisk APFS RestoredVolume disk2
```

### 4. Use Terminal for Restore Operation

```bash
# WARNING: This erases the destination disk
sudo asr --source /path/to/image.dmg --target /Volumes/RestoredVolume --erase
```

## Common Scenarios

This error commonly occurs when:

- Disk Utility restore progress bar stuck at same percentage
- Restore fails with 'Could not restore' error message
- Disk image mounts but cannot be restored to target disk
- Restore operation completes but restored disk is not bootable

## Prevent It

- Verify disk image integrity before starting restore
- Use reliable USB/Thunderbolt connections for restore operations
- Keep source and destination disks healthy with regular First Aid
- Use 'asr' command line tool for more reliable restores

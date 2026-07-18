---
title: "[Solution] macOS Disk Mount Error — External Drive Not Appearing"
description: "Fix macOS disk mount failure: external drive not appearing in Finder, volume not mounting after connection, disk shows but won't mount."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 134
---

# Disk Mount Error — External Drive Not Appearing

Fix macOS disk mount failure: external drive not appearing in Finder, volume not mounting after connection, disk shows but won't mount.

## Common Causes

- Disk format not supported by macOS (NTFS write, ext4, etc.)
- Corrupted file system preventing mount operation
- USB or Thunderbolt connection issue preventing disk detection
- Disk partition table damaged or missing volume header

## How to Fix

### 1. Check Disk Detection and Connection

```bash
diskutil list
system_profiler SPUSBDataType
system_profiler SPThunderboltDataType
```

### 2. Force Mount the Disk

```bash
sudo diskutil mount /dev/disk2s1
sudo diskutil mountDisk disk2
```

### 3. Repair Disk and File System

```bash
diskutil verifyVolume disk2s1
# Recovery → Disk Utility → First Aid
```

### 4. Initialize Unrecognized Disk

```bash
# WARNING: This will erase all data
sudo diskutil eraseDisk APFS NewVolume disk2
```

## Common Scenarios

This error commonly occurs when:

- External USB drive is connected but does not appear in Finder
- Disk shows in Disk Utility but mount button is grayed out
- Drive was working before but stopped mounting after macOS update
- Disk mounts momentarily then immediately unmounts by itself

## Prevent It

- Use Mac-compatible formats (APFS or Mac OS Extended) for external drives
- Always eject drives properly before disconnecting them
- Test new external drives with Disk Utility First Aid before regular use
- Keep macOS updated for improved disk compatibility

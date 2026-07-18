---
title: "[Solution] macOS Disk Unmount Error — Cannot Eject Disk"
description: "Fix macOS disk unmount failure: cannot eject disk, volume in use error, disk busy and cannot be unmounted, disk eject grayed out."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 133
---

# Disk Unmount Error — Cannot Eject Disk

Fix macOS disk unmount failure: cannot eject disk, volume in use error, disk busy and cannot be unmounted, disk eject grayed out.

## Common Causes

- Application has open files on the disk preventing unmount
- Finder or Spotlight indexing the disk in background
- Terminal or other process holding file handle on disk
- Disk is being used as Time Machine backup destination

## How to Fix

### 1. Find and Stop Processes Using the Disk

```bash
lsof +D /Volumes/DiskName
sudo fuser -v /Volumes/DiskName
kill -9 PID_NUMBER
```

### 2. Force Unmount the Disk

```bash
sudo diskutil unmount force /Volumes/DiskName
sudo diskutil unmountDisk force disk2
sudo diskutil eject disk2
```

### 3. Disable Spotlight and Finder Indexing

```bash
sudo mdutil -i off /Volumes/DiskName
# Close all Finder windows showing disk contents
```

### 4. Eject from Terminal with Verification

```bash
sudo lsof | grep '/Volumes/DiskName'
diskutil info /Volumes/DiskName | grep 'Read-Only'
diskutil eject /Volumes/DiskName
```

## Common Scenarios

This error commonly occurs when:

- Finder shows 'disk in use' error when trying to eject external drive
- Disk eject option is grayed out in Finder or Disk Utility
- External hard drive makes noise after eject command
- USB drive cannot be safely removed even after closing all windows

## Prevent It

- Always use Eject or Safely Remove before physically disconnecting drives
- Close all files and applications accessing the drive
- Avoid using Time Machine backup drives as general storage
- Check running processes with Activity Monitor before ejecting

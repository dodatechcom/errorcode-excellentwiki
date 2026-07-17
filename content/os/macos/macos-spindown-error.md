---
title: "[Solution] macOS Spindown Error — Disk Did Not Eject Properly"
description: "Fix macOS spindown errors when internal or external disks fail to power down or eject properly."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["spindown", "disk", "eject", "hdd", "sleep", "power"]
weight: 5
---

# macOS Spindown Error Fix

A spindown error occurs when macOS cannot properly power down (spin down) a hard disk drive. This prevents the Mac from sleeping, causes excessive battery drain, and may display warnings about disks not ejecting properly.

## What This Error Means

When macOS enters sleep, it attempts to spin down all HDDs. If a process is holding the disk open, the spindown fails. macOS logs `"disk did not eject properly"` or the disk remains active during sleep.

## Common Causes

- Background processes accessing the disk (Time Machine, Spotlight indexing)
- External HDD with a faulty USB/SATA bridge
- Corrupt file system preventing clean unmount
- macOS bug with specific disk enclosures
- SMART errors on failing drives

## How to Fix

### 1. Find processes keeping the disk busy

```bash
# Find which process is accessing the disk
lsof +D /Volumes/YourDiskName

# Check Spotlight indexing
mdutil -s /Volumes/YourDiskName

# Disable Spotlight on external disk temporarily
mdutil -i off /Volumes/YourDiskName
```

### 2. Check disk health

```bash
# Check S.M.A.R.T. status
diskutil info /Volumes/YourDiskName | grep SMART

# Run first aid
diskutil verifyVolume /Volumes/YourDiskName
```

### 3. Force spin down the disk

```bash
# Force the disk to spin down
diskutil unmountDisk force /Volumes/YourDiskName

# Or eject it
diskutil eject /Volumes/YourDiskName
```

### 4. Check the system log for spindown errors

```bash
log show --predicate 'eventMessage contains "spindown"' --last 24h
```

## Related Errors

- [Disk Utility Error](disk-utility-error) — disk corruption and repair errors
- [Time Machine Error](time-machine-error) — backup errors that may keep disks busy
- [Finder Error](finder-error) — file system errors

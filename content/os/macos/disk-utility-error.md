---
title: "[Solution] macOS Disk Utility Error — Couldn't Unmount / Verify / Repair Disk"
description: "Fix Disk Utility errors: couldn't unmount disk, verify disk, or repair disk on macOS. Use First Aid from Recovery Mode and fix APFS/HFS+ errors."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 5
---

# Disk Utility Error — Couldn't Unmount / Verify / Repair Disk

Disk Utility errors occur when macOS cannot unmount, verify, or repair a disk or volume. These errors typically prevent you from running First Aid, erasing a disk, or modifying partitions. The most common variants are "Couldn't unmount disk," "Verify failed," and "Operation not permitted."

## Description

Disk Utility relies on the `diskutil` command-line tool under the hood. Errors occur when:

- **Volume is in use** — a process has files open on the volume, preventing unmount.
- **System volume can't be modified** — macOS System Volume (APFS) is read-only on running systems.
- **Disk corruption** — file system metadata is damaged.
- **Permissions issue** — Disk Utility lacks privileges to modify the disk.

Common error messages:

- `Disk Utility couldn't unmount disk because it is currently in use.`
- `First Aid found corruption that needs to be repaired.`
- `Couldn't modify partition map.`
- `The volume couldn't be verified completely.`

## Common Causes

- Running First Aid on the startup volume while booted from it
- Applications holding files open on the target volume
- Corrupted APFS container or HFS+ catalog
- Physical disk sectors failing (SMART errors)

## How to Fix Disk Utility Errors

### 1. Boot into Recovery Mode and Run First Aid

```bash
# Shut down Mac
# For Intel: Hold Cmd+R during startup
# For Apple Silicon: Hold power button → Options → Recovery
# Open Disk Utility → Select volume → Click "First Aid"
```

### 2. Use diskutil from Terminal in Recovery Mode

```bash
# List all disks and volumes
diskutil list

# Verify a specific volume
diskutil verifyVolume disk2s1

# Try to repair
diskutil repairVolume disk2s1

# Force unmount before repair
diskutil unmount force disk2s1
```

### 3. Force Unmount a Stuck Volume

```bash
# Check what's using the volume
lsof | grep /Volumes/YourVolumeName

# Force unmount
diskutil unmount force disk2s1

# Or use hdiutil for disk images
hdiutil detach /Volumes/DiskImage -force
```

### 4. Repair the Boot Volume from Recovery

```bash
# From Recovery Mode terminal
# Find your disk identifier
diskutil list

# Run First Aid on the container
diskutil verifyVolume disk1s1

# If APFS, repair the container first
diskutil apfs verifyContainer disk1
```

### 5. Erase and Reformat a Corrupted Disk

```bash
# WARNING: This erases all data
# From Recovery Mode → Disk Utility → Select disk → Erase
# Choose APFS (for SSDs) or Mac OS Extended (for HDDs)

# Or from terminal:
diskutil eraseDisk APFS "NewName" disk2
```

## Examples

This error commonly occurs when:

- Trying to run First Aid on the startup volume without booting to Recovery
- A mounted DMG cannot be ejected because an app has a file open
- After a forced shutdown, the file system journal is inconsistent
- Attempting to partition a disk while Time Machine is actively backing up

## Related Errors

- [Kernel Panic](kernel-panic) — disk corruption may cause system crashes
- [Time Machine Error](time-machine-error) — backup failures due to disk issues
- [Finder Error](finder-error) — "The operation can't be completed" when disk is corrupted

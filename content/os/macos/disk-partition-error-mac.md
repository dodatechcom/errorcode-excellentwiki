---
title: "[Solution] macOS Disk Partition Error — Cannot Create or Resize Partitions"
description: "Fix macOS disk partition failure: cannot create, resize, or delete partitions, partition map corrupted, partition operations fail."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 137
---

# Disk Partition Error — Cannot Create or Resize Partitions

Fix macOS disk partition failure: cannot create, resize, or delete partitions, partition map corrupted, partition operations fail.

## Common Causes

- Partition map corrupted preventing modifications
- Disk has mounted volumes that must be unmounted first
- Partition table uses unsupported format for requested operation
- Insufficient free space on disk for new partition creation

## How to Fix

### 1. Unmount Volumes Before Modifying Partitions

```bash
diskutil list
sudo diskutil unmountDisk disk2
```

### 2. Create New Partition from Terminal

```bash
sudo diskutil eraseDisk APFS NewVolume disk2
sudo diskutil partitionDisk disk2 GPTScheme APFS Part1 50G APFS Part2 50G
```

### 3. Fix Corrupted Partition Map

```bash
# WARNING: This erases ALL data
sudo diskutil partitionDisk disk2 GPTScheme APFS NewVolume 100%
```

### 4. Repair Partition Errors from Recovery

```bash
# Recovery → Disk Utility → Select disk → First Aid
```

## Common Scenarios

This error commonly occurs when:

- Disk Utility shows 'Partition Failed' when trying to add partition
- Cannot resize existing partition because it's the last on disk
- Partition map shows 'corrupted' or 'unreadable' status
- Creating new partition fails with 'No space left' despite free space

## Prevent It

- Plan partition layout carefully before creating partitions
- Back up disk contents before modifying partition structure
- Use GPT partition scheme for modern macOS compatibility
- Avoid third-party partition managers that may corrupt partition maps

---
title: "[Solution] macOS Disk Partition Error -- Disk Partitioning Failed"
description: "Fix macOS disk partition error when Disk Utility fails to partition or modify the disk partition map. Resolve partition errors on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Disk Partition Error -- Disk Partitioning Failed

Disk partitioning errors occur when Disk Utility cannot create, resize, or delete partitions on a disk. This prevents you from setting up new volumes or resizing existing ones.

## Common Causes
- Disk has a partition in use that cannot be modified
- File system is locked by FileVault or CoreStorage
- Partition map is corrupted
- Disk has bad sectors in the partition table area
- macOS is installed on the partition being modified

## How to Fix
1. Ensure no applications are using files on the partition
2. Disable FileVault before modifying partitions
3. Boot from Recovery Mode or an external drive to partition the internal disk
4. Use terminal commands for more control over partitioning
5. If the disk is corrupted, back up and erase the entire disk

```bash
# Check current partition layout
diskutil list disk0

# Attempt to erase and repartition (WARNING: destroys all data)
diskutil eraseDisk APFS "Macintosh HD" GPT disk0
```

## Examples

```bash
# Resize a partition (deletes data beyond the new boundary)
diskutil resizeVolume disk0s2 100g
```

This error is common when trying to modify the startup disk while macOS is running, when FileVault encryption locks the partition, or when the partition map has been corrupted by a failed resize operation.

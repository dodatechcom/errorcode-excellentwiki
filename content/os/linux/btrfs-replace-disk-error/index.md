---
title: "Fix Linux: btrfs-replace-disk-error -- btrfs device replace failure in Linux"
description: "Fix btrfs device replace errors when swapping disks in a btrfs filesystem."
os: ["linux"]
error-types: [["filesystem"]]
severities: [["error", "warning"]]
---

Btrfs device replace fails when the replacement disk is incompatible or the filesystem state is inconsistent.

## Common Causes
- Target disk smaller than source
- Filesystem already in degraded state
- Source device inaccessible during operation
- Btrfs version mismatch between kernels

## How to Fix
1. Check current filesystem status:
   btrfs filesystem show
   btrfs device stats /mountpoint
2. Start replacement:
   btrfs replace start /dev/old /dev/new /mountpoint
3. Monitor progress:
   btrfs replace status /mountpoint
4. Cancel if needed and retry:
   btrfs replace cancel /mountpoint

## Examples
### Common Error Message
ERROR: cannot replace, filesystem is degraded\n
ERROR: btrfs replace start: No space left on device

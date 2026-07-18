---
title: "[Solution] macOS Disk Clone Error — Cannot Clone Disk"
description: "Fix macOS disk clone failure: cannot clone disk with Disk Utility or third-party tools, clone process fails or produces unbootable result."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 147
---

# Disk Clone Error — Cannot Clone Disk

Fix macOS disk clone failure: cannot clone disk with Disk Utility or third-party tools, clone process fails or produces unbootable result.

## Common Causes

- Source disk errors preventing clean clone operation
- Destination disk too small for source data
- Block-level clone mismatch between different disk types
- Third-party cloning tool incompatibility with APFS

## How to Fix

### 1. Check Source and Destination Disks

```bash
diskutil list
diskutil info disk0 | grep 'Total Size'
diskutil info disk2 | grep 'Total Size'
```

### 2. Clone Using Disk Utility

```bash
# Recovery → Disk Utility → Select source → Restore → Choose destination
```

### 3. Clone Using Terminal (asr)

```bash
sudo asr --source /dev/disk0 --target /dev/disk2 --erase
```

### 4. Fix Boot After Clone

```bash
# Boot into Recovery → Disk Utility → First Aid on cloned disk
bless --mount /Volumes/Cloned\ HD --setBoot
```

## Common Scenarios

This error commonly occurs when:

- Cloned disk is not bootable when selected as startup disk
- Clone process fails partway through with I/O error
- Third-party clone tool cannot read APFS container
- Cloned disk has different capacity than expected

## Prevent It

- Use Disk Utility Restore or 'asr' for reliable disk cloning
- Ensure destination disk is same size or larger than source
- Verify cloned disk with First Aid before booting from it
- Keep macOS updated for APFS cloning compatibility

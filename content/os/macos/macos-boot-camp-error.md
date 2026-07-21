---
title: "[Solution] macOS Boot Camp Error -- Boot Camp Assistant Fails to Create Windows Partition"
description: "Fix macOS Boot Camp error when Boot Camp Assistant fails to create a Windows partition. Resolve Boot Camp issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Boot Camp Error -- Boot Camp Assistant Fails to Create Windows Partition

Boot Camp allows you to install Windows on a Mac alongside macOS. When Boot Camp Assistant fails, the Windows partition may not be created, or the Windows installer may not boot.

## Common Causes
- Insufficient disk space for the Windows partition
- Disk has errors that prevent partitioning
- Firmware password is blocking partition changes
- Windows ISO file is corrupted or incompatible
- Boot Camp Assistant is outdated

## How to Fix
1. Ensure at least 55 GB of free space for Windows
2. Run Disk Utility First Aid on the startup disk
3. Disable firmware password temporarily
4. Re-download the Windows ISO from Microsoft
5. Update Boot Camp Assistant and macOS

```bash
# Check available disk space
df -h /

# Run Disk Utility First Aid
# Boot into Recovery Mode, open Disk Utility, run First Aid

# Check firmware password status
# Boot into Recovery Mode and look for Firmware Password Utility
```

## Examples

```bash
# Open Boot Camp Assistant
open -a "Boot Camp Assistant"
```

This error is common when there is insufficient disk space, when the disk has errors that prevent partitioning, or when a firmware password blocks partition changes.

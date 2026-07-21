---
title: "[Solution] macOS Startup Disk Error -- No Bootable Device Found"
description: "Fix macOS startup disk error when no bootable device is found. Resolve Mac not recognizing the internal drive at startup."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Startup Disk Error -- No Bootable Device Found

The startup disk error occurs when macOS cannot locate or boot from the designated startup volume. The Mac may show a flashing folder icon, a prohibitory symbol, or the Startup Disk pane reports no valid system.

## Common Causes
- Startup disk was erased or the APFS container was damaged
- The boot picker lost track of the system volume
- A firmware update changed the boot policy
- External drive was set as startup disk but is now disconnected
- T2 chip security settings blocking boot from internal drive

## How to Fix
1. Hold Option during startup to see the available boot volumes
2. If no internal drive appears, boot into Recovery Mode
3. In Recovery, open Startup Disk and reselect your macOS volume
4. Use Disk Utility to repair the startup volume if it appears unmounted

```bash
# From Recovery terminal
diskutil list
diskutil apfs listVolumes
diskutil mount disk1s1
```

## Examples

```bash
# Check firmware mode and boot policy
bless --info --verbose /
bless --info --verbose --getboot
```

This error commonly occurs after erasing a partition in Disk Utility by mistake, after an interrupted macOS installation, or when Boot Camp partitions confuse the boot process.

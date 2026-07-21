---
title: "[Solution] macOS HFS+ to APFS Conversion Error -- Conversion Failed"
description: "Fix macOS HFS+ to APFS conversion error when converting from HFS+ to APFS fails. Resolve APFS conversion errors on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS HFS+ to APFS Conversion Error -- Conversion Failed

macOS can convert HFS+ volumes to APFS without erasing data. When this conversion fails, the volume may be left in an inconsistent state or the conversion may silently fail.

## Common Causes
- HFS+ volume has corruption that prevents conversion
- Disk does not have enough free space for conversion overhead
- Volume has too many files or directory entries
- Third-party encryption or disk management software is interfering
- The disk is connected via a slow or unreliable adapter

## How to Fix
1. Run Disk Utility First Aid on the HFS+ volume before converting
2. Ensure at least 10% free space on the volume
3. Disconnect external drives and use internal storage
4. Back up the volume and erase it as APFS instead of converting
5. Try the conversion from Recovery Mode

```bash
# Convert HFS+ to APFS
diskutil apfs convert disk1s2

# Check conversion status
diskutil apfs list
```

## Examples

```bash
# Check volume format before conversion
diskutil info disk1s2 | grep -i "file system"
```

This error is common when the HFS+ volume has directory corruption, when the disk is nearly full, or when third-party disk utilities have modified the volume in ways that prevent conversion.

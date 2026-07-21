---
title: "[Solution] macOS Installation Error 8 -- Installer Failed APFS Conversion"
description: "Fix macOS installation error 8 when APFS conversion fails during install. Resolve Mac OS install APFS conversion error."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Installation Error 8 -- Installer Failed APFS Conversion

Error code 8 indicates the installer failed to convert or create the APFS volume structure required for macOS.

## Common Causes
- Disk has insufficient space for APFS conversion overhead
- HFS+ volume has corruption preventing conversion
- Disk is connected via a slow or unreliable adapter
- Third-party disk management software interfering
- Disk partition map is not GUID Partition Map

## How to Fix
1. Ensure the disk uses GUID Partition Map (not MBR)
2. Verify disk space -- APFS conversion needs extra temporary space
3. Run Disk Utility First Aid on the disk before installing
4. Disconnect slow USB adapters and install on internal storage
5. Erase the disk as APFS before installing to skip conversion

```bash
# Check partition map type
diskutil list disk0 | grep -i "partition_map"

# Pre-format as APFS to skip conversion
diskutil eraseDisk APFS "Macintosh HD" GPT disk0
```

## Examples

```bash
# Verify APFS container structure
diskutil apfs list
```

This error is common on older Macs converting from HFS+ to APFS for the first time, when the disk is connected via a slow USB adapter, or when the disk has filesystem corruption.

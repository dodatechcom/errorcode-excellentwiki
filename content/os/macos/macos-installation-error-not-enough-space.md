---
title: "[Solution] macOS Installation Error -- Not Enough Disk Space"
description: "Fix macOS installation error when not enough disk space is available. Resolve not enough disk space during Mac OS install."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Installation Error -- Not Enough Disk Space

macOS requires significant free space for installation -- typically 15 to 35 GB depending on the version. The installer may fail with an explicit error or silently fail during the extraction phase.

## Common Causes
- Startup volume has less than 25 GB of free space
- Time Machine local snapshots consuming hidden space
- APFS purgeable space not being reclaimed automatically
- Large files in Trash still occupying disk space
- System caches and logs consuming space on the startup volume

## How to Fix
1. Check available disk space including purgeable space
2. Empty the Trash and clear Downloads folder
3. Remove Time Machine local snapshots to free hidden space
4. Use the Storage Management tool to identify large files
5. Move large files to an external drive before installing

```bash
# Check disk space
df -h /

# Remove Time Machine local snapshots
sudo tmutil deletelocalsnapshots /
```

## Examples

```bash
# Find large files in your home directory
du -sh ~/Downloads/* | sort -rh | head -20
du -sh ~/Documents/* | sort -rh | head -20
```

This error is common after accumulating many Photos library items, when Time Machine local snapshots silently fill the disk, or when Docker containers are consuming hidden space.

---
title: "[Solution] macOS Disk Unmount Error -- Volume Cannot Be Unmounted"
description: "Fix macOS disk unmount error when a volume cannot be unmounted. Resolve disk unmount failures on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Disk Unmount Error -- Volume Cannot Be Unmounted

When you try to eject or unmount a disk volume and macOS refuses, it usually means a process is still using files on the volume.

## Common Causes
- An application has files open on the volume
- Terminal has the volume as its current working directory
- Spotlight is indexing the volume
- Time Machine is backing up to the volume
- A background process has a file lock on the volume

## How to Fix
1. Check which processes are using the volume with lsof
2. Quit applications that may have files open on the volume
3. Change the Terminal working directory if it is on the volume
4. Force unmount the volume (risk of data loss)
5. Restart the Mac and try ejecting again

```bash
# Find processes using the volume
lsof +D /Volumes/ExternalDrive

# Force unmount (WARNING: may cause data loss)
diskutil unmount force disk2s1

# Or use the mount point
diskutil unmount force /Volumes/ExternalDrive
```

## Examples

```bash
# Check what is mounted
mount | grep /Volumes/

# List open files on a volume
lsof /Volumes/ExternalDrive
```

This error is common when a Terminal window has the volume as its working directory, when Spotlight is indexing a freshly connected drive, or when Time Machine is in the middle of a backup.

---
title: "[Solution] macOS Disk Full -- Startup Disk Is Out of Space"
description: "Fix macOS disk full error when the startup disk has no more free space. Resolve disk full on Mac with cleanup steps."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Disk Full -- Startup Disk Is Out of Space

When the macOS startup disk is full, apps crash, updates fail, and the system may become unresponsive. The 'Your disk is almost full' warning appears when space drops below 10 GB.

## Common Causes
- Large files accumulated in Downloads, Documents, or Trash
- Time Machine local snapshots consuming hidden space
- Docker containers or VMs using significant disk space
- System caches and logs growing over time
- Photo library or media files filling the drive

## How to Fix
1. Empty the Trash and clear the Downloads folder
2. Remove Time Machine local snapshots
3. Use Storage Management to identify and remove large files
4. Clear system and user caches
5. Move large files to an external drive or cloud storage

```bash
# Check disk space
df -h /

# Remove Time Machine local snapshots
sudo tmutil deletelocalsnapshots /

# Find large files
du -sh ~/Downloads/* | sort -rh | head -20
du -sh ~/Documents/* | sort -rh | head -20
```

## Examples

```bash
# Clear system caches
sudo rm -rf ~/Library/Caches/*

# Check what is taking up space
du -sh ~/* | sort -rh | head -20
```

This error is common when Docker images accumulate, when Photo libraries grow large, when Time Machine local snapshots silently fill the disk, or when large downloads are never cleaned up.

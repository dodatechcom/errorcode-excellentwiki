---
title: "[Solution] macOS Disk Full Error — Startup Disk Is Full"
description: "Fix macOS disk full: startup disk is full, cannot save files, system runs slowly, apps crash due to insufficient disk space."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 130
---

# Disk Full Error — Startup Disk Is Full

Fix macOS disk full: startup disk is full, cannot save files, system runs slowly, apps crash due to insufficient disk space.

## Common Causes

- Large files or applications consuming all available disk space
- System logs, caches, and temporary files accumulating over time
- Time Machine local snapshots filling disk silently
- iCloud Drive or Downloads folder containing unnecessary files

## How to Fix

### 1. Check Disk Space and Large Files

```bash
df -h /
du -sh ~/Library/Caches ~/Downloads ~/Documents 2>/dev/null | sort -hr | head -10
find / -type f -size +500M 2>/dev/null | head -20
```

### 2. Clear System Caches and Temporary Files

```bash
rm -rf ~/Library/Caches/*
sudo rm -rf /Library/Caches/*
sudo find /var/log -type f -mtime +7 -delete
tmutil deletelocalsnapshots /
```

### 3. Remove Unnecessary Applications and Files

```bash
du -sh /Applications/*.app | sort -hr | head -10
rm -rf ~/.Trash/*
```

### 4. Enable Storage Optimization

```bash
# Apple Menu → About This Mac → Storage → Manage
# Enable 'Reduce Clutter' and 'Store in iCloud' options
```

## Common Scenarios

This error commonly occurs when:

- Cannot save new files with 'disk is full' error message
- Mac runs extremely slowly with beachball cursor due to full disk
- Apps crash on launch because they cannot write temporary files
- macOS update fails because insufficient disk space available

## Prevent It

- Monitor disk usage regularly and keep at least 15% free space
- Empty Trash and Downloads folder weekly to reclaim space
- Enable iCloud Drive optimization to store large files in cloud
- Use storage management tools to identify and remove large unused files

---
title: "[Solution] Spotlight Not Indexing Files Error on Mac"
description: "Fix Spotlight errors on macOS when search doesn't find files, indexing is stuck, or Spotlight shows 'Indexing' forever."
platforms: ["macos"]
severities: ["error"]
error-types: ["system-error"]
tags: ["spotlight", "search", "indexing", "mds", "metadata", "macos"]
weight: 5
---

# Spotlight Not Indexing Files Error on Mac

Spotlight search doesn't find files, shows "Indexing" status indefinitely, or search results are incomplete/outdated.

## What This Error Means

Spotlight relies on the metadata server (mds) to index file contents. Indexing failures occur when the mds database is corrupted, the indexing process is stuck, or excluded folders prevent proper indexing.

## Common Causes

- Corrupted Spotlight index database
- mds process crashed or stuck
- Large files or folders overwhelming the indexer
- Privacy settings excluding important folders
- Third-party apps blocking indexing
- Disk errors preventing index writes

## How to Fix

### Check Indexing Status

```bash
# Check if mds is running
ps aux | grep mds

# Check indexing status
mdls -name kMDItemContentType <file_path>

# Check Spotlight preferences
mdutil -s /
```

### Rebuild Spotlight Index

```bash
# Disable Spotlight indexing
sudo mdutil -i off /

# Delete existing index
sudo mdutil -E /

# Re-enable indexing
sudo mdutil -i on /

# Force immediate reindex
sudo mdutil -E /
```

### Check Privacy Exclusions

```bash
# List excluded folders
defaults read com.apple.Spotlight orderedItems 2>/dev/null

# Or check via System Settings > Siri & Spotlight > Spotlight Privacy
```

### Restart mds Process

```bash
# Kill mds to force restart
sudo killall mds

# mds will automatically restart
# Wait for reindexing to complete
```

### Fix Permission Issues

```bash
# Reset Spotlight permissions
sudo chmod -R /Users/$USER/Library/Metadata 755

# Rebuild in safe mode
# Restart Mac while holding Shift key
```

### Check Disk Health

```bash
# Verify disk integrity
diskutil verifyVolume /

# Repair if needed
diskutil repairVolume /
```

## Related Errors

- [Finder Error]({{< relref "/os/macos/finder-error" >}}) — File browsing issues
- [macOS Recovery Error]({{< relref "/os/macos/macos-macos-recovery-error" >}}) — Recovery mode
- [SSD Error]({{< relref "/os/macos/macos-ssd-error-v2" >}}) — Storage issues

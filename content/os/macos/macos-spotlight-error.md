---
title: "[Solution] macOS Spotlight Not Indexing"
description: "Fix Spotlight not indexing on Mac when search results are incomplete, missing, or Spotlight shows 'Indexing.' Resolve Spotlight rebuild issues."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["spotlight", "indexing", "search", "mdls", "metadata"]
weight: 5
---

# macOS Spotlight Not Indexing Fix

Spotlight errors include incomplete search results, "Indexing" status that never completes, or Spotlight returning no results for known files. This affects file search and Quick Look previews.

## What This Error Means

Spotlight maintains a metadata index of all files on the system using the `mds` daemon. When indexing fails or stalls, search results become stale or empty. Common on external drives or after large file operations.

## Common Causes

- Spotlight index database corrupted
- External drive excluded from Spotlight
- `mds` daemon crashed or stuck
- Privacy settings excluding folders from indexing
- Disk full preventing index updates
- Spotlight spotlight process consuming excessive CPU

## How to Fix

### 1. Rebuild the Spotlight index

```bash
# Rebuild the entire Spotlight index
sudo mdutil -E /

# Check indexing status
mdutil -s /

# Force stop and restart indexing
sudo mdutil -i off /
sudo mdutil -i on /
```

### 2. Check if volumes are indexed

```bash
# List all volumes and their indexing status
mdutil -s -a

# Enable indexing on a specific volume
sudo mdutil -i on /Volumes/ExternalDrive
```

### 3. Delete and rebuild the Spotlight store

```bash
# Delete the Spotlight index database
sudo rm -rf /.Spotlight-V100

# Trigger a full re-index
sudo mdutil -E /
```

### 4. Check Spotlight privacy list

```bash
# View excluded folders
defaults read ~/Library/Preferences/com.apple.Spotlight orderedItems

# Remove exclusions if needed via System Preferences → Spotlight → Privacy
```

## Related Errors

- [Finder Error](finder-error) — file system navigation errors
- [Disk Utility Error](disk-utility-error) — disk corruption issues
- [Spotlight Error](spotlight-error) — Spotlight metadata framework errors

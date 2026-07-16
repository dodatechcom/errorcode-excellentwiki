---
title: "[Solution] macOS Spotlight Not Working — Indexing Error Fix"
description: "Fix macOS Spotlight search not working or stuck indexing. Rebuild Spotlight index, fix metadata corruption, and restore search functionality."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
tags: ["spotlight", "search", "indexing", "mdfind", "metadata"]
weight: 5
---

# Spotlight Not Working — Indexing Error

Spotlight not working means the macOS search system either returns no results, returns incomplete results, or is stuck "Indexing." Spotlight relies on a metadata index maintained by the `mds` and `mds_stores` processes. When the index is corrupted or incomplete, search stops working.

## Description

Spotlight issues manifest as:

- Search returns no results or "No Results"
- Spotlight shows "Indexing" indefinitely in Spotlight preferences
- `mdfind` returns empty results from the terminal
- Some files are missing from search results
- Search is extremely slow

## Common Causes

- Spotlight index corrupted after disk errors or forced shutdown
- Excluded folders in Spotlight privacy list
- `mds` or `mds_stores` process crashed or is hung
- APFS snapshot conflicts preventing index updates
- Third-party antivirus interfering with metadata service

## How to Fix Spotlight Indexing Errors

### 1. Check if Spotlight is Enabled

```bash
# Check if Spotlight is disabled
mdutil -s /

# Enable Spotlight if it's off
sudo mdutil -i on /
```

### 2. Rebuild the Spotlight Index

```bash
# Delete the existing index and rebuild
sudo mdutil -E /

# Monitor the re-indexing process
# This may take 30-60 minutes for large disks
mdutil -s /
```

### 3. Check and Remove Privacy Exclusions

```bash
# List excluded volumes
mdutil -s

# Remove a volume from the exclusion list
sudo mdutil -i on /Volumes/ExternalDrive

# Or via System Settings → Siri & Spotlight → Spotlight Privacy
```

### 4. Restart the Metadata Server

```bash
# Kill the metadata server to force restart
sudo killall mds
sudo killall mds_stores

# They will restart automatically
# Monitor with:
ps aux | grep mds
```

### 5. Check for Spotlight Errors in Console

```bash
# Open Console.app → Search for "mds" or "Spotlight"
# Or from terminal:
log show --predicate 'process == "mds"' --last 1h

# Check system logs for index errors
log show --predicate 'process == "mds_stores"' --last 30m
```

## Examples

This error commonly occurs when:

- After a macOS upgrade that changed the metadata schema
- A hard drive has bad sectors corrupting the Spotlight database
- External drives are repeatedly connected/disconnected
- Anti-virus software locks files that Spotlight needs to index

## Related Errors

- [Finder Error](finder-error) — Spotlight failures can cause Finder to lag
- [Kernel Panic](kernel-panic) — corrupted metadata service can cause system crashes
- [Disk Utility Error](disk-utility-error) — disk issues may corrupt the Spotlight index

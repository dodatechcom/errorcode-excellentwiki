---
title: "[Solution] macOS Finder Error — The Operation Can't Be Completed"
description: "Fix macOS Finder error: 'The operation can't be completed.' Resolve file operation failures, permission issues, and Finder crashes on Mac."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
tags: ["finder", "operation-not-completed", "file-manager", "copy", "move", "delete"]
weight: 5
---

# Finder Error — The Operation Can't Be Completed

A Finder error occurs when the macOS Finder cannot complete a file operation such as copy, move, rename, or delete. The generic message "The operation can't be completed because one or more required items can't be found" or "The operation can't be completed because an unexpected error occurred" provides little diagnostic information.

## Description

Finder errors are among the most vague macOS errors. They can result from file system corruption, permission issues, corrupted Finder preferences, or conflicts with cloud services like iCloud Drive.

Common variants:

- `The operation can't be completed because one or more required items can't be found.`
- `The operation can't be completed because an unexpected error occurred (error code -50).`
- `The operation can't be completed because you don't have permission.`
- `The operation can't be completed because the item "X" is in use.`

## Common Causes

- File is locked or in use by another process
- Corrupted Finder preferences or cache
- File name contains special characters that Finder can't handle
- iCloud Drive sync conflict preventing file operations
- Disk permissions are incorrect

## How to Fix Finder Errors

### 1. Restart Finder

```bash
# Force quit Finder
killall Finder

# Finder will automatically restart
# Or: Hold Option → Right-click Finder in Dock → Relaunch
```

### 2. Fix Permissions on the Target File/Folder

```bash
# Check current permissions
ls -la /path/to/file

# Take ownership
sudo chown $(whoami) /path/to/file

# Make writable
chmod u+w /path/to/file
```

### 3. Delete Finder Preferences

```bash
# Kill Finder first
killall Finder

# Remove corrupted preferences
rm ~/Library/Preferences/com.apple.finder.plist

# Restart Finder — preferences will be recreated
killall Finder
```

### 4. Use Terminal for File Operations

```bash
# When Finder can't copy/move/delete, use terminal
# Force delete a stuck file
rm -rf /path/to/file

# Force move
mv /path/to/source /path/to/destination

# Force rename
mv /path/to/old-name /path/to/new-name
```

### 5. Clear Finder Cache

```bash
# Clear Finder's cached data
rm -rf ~/Library/Caches/com.apple.finder

# Restart Finder
killall Finder
```

## Examples

This error commonly occurs when:

- Trying to delete a file that iCloud Drive is actively syncing
- Renaming a file to the same name with different case on a case-insensitive volume
- Moving files to a USB drive that was ejected improperly
- Copying files with emoji or special characters in the name

## Related Errors

- [iCloud Error](icloud-error) — Finder errors when iCloud Drive is involved
- [Disk Utility Error](disk-utility-error) — file system corruption causes Finder failures
- [Spotlight Error](spotlight-error) — Spotlight issues can slow or block Finder operations

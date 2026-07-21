---
title: "[Solution] macOS Notes Error -- Notes App Not Syncing or Crashing"
description: "Fix macOS Notes error when the Notes app fails to sync, crashes, or loses notes. Resolve Notes app issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Notes Error -- Notes App Not Syncing or Crashing

The Notes app on macOS syncs notes via iCloud. Errors can include notes disappearing, sync failures, or the app crashing when opening certain notes.

## Common Causes
- iCloud Notes sync is disabled or not working
- Notes database is corrupted
- Note contains embedded content that is corrupt
- iCloud storage is full
- Notes account is locked or expired

## How to Fix
1. Ensure iCloud Notes sync is enabled in System Preferences
2. Sign out of iCloud and back in to force re-sync
3. Check iCloud storage and free up space
4. Rebuild the Notes database
5. Export notes before attempting database repair

```bash
# Check Notes database
ls -la ~/Library/Containers/com.apple.Notes/Data/Library/Notes/

# View Notes errors
log show --predicate 'process == "Notes"' --last 10m
```

## Examples

```bash
# Check iCloud storage
# System Preferences > Apple ID > iCloud > Manage
```

This error is common when iCloud storage is full, when the Notes database is corrupted, or when a note contains embedded content that causes the app to crash.

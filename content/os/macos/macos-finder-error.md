---
title: "[Solution] macOS Finder Error -- Finder Encounters an Unexpected Error"
description: "Fix macOS Finder error when Finder shows 'The operation can't be completed' or other errors. Resolve Finder issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Finder Error -- Finder Encounters an Unexpected Error

Finder is the file manager on macOS. Finder errors can prevent you from opening folders, copying files, or moving items. The most common message is 'The operation can't be completed because an unexpected error occurred.'

## Common Causes
- Finder preference files are corrupted
- File system permissions are incorrect
- A file or folder name contains invalid characters
- Network drive or shared folder is unreachable
- Spotlight indexing is conflicting with file operations

## How to Fix
1. Restart Finder by force quitting (Option+Command+Escape)
2. Delete Finder preference files and restart
3. Reset Finder's view settings
4. Check file system permissions
5. Boot into Safe Mode to test if third-party software is causing the issue

```bash
# Force quit and restart Finder
killall Finder

# Delete Finder preferences
defaults delete com.apple.finder

# Reset Finder preferences
defaults delete com.apple.finder; killall Finder
```

## Examples

```bash
# Check Finder crash reports
ls -lt ~/Library/Logs/DiagnosticReports/ | grep -i Finder
```

This error is common after a macOS update corrupts Finder preferences, when a network drive becomes unavailable, or when file names contain characters that Finder cannot handle.

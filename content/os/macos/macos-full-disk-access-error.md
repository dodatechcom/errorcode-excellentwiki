---
title: "[Solution] macOS Full Disk Access Error -- App Cannot Access All Files"
description: "Fix macOS full disk access error when an app needs full disk access but cannot get it. Resolve full disk access permission issues."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Full Disk Access Error -- App Cannot Access All Files

Full Disk Access is a macOS privacy setting that allows apps to access files in protected locations like Mail, Messages, and Safari data. Without it, apps cannot read these protected files.

## Common Causes
- Full Disk Access was not granted in System Preferences
- App was updated and needs permission re-granted
- TCC database is corrupted
- MDM profile is restricting full disk access
- macOS update reset privacy permissions

## How to Fix
1. Open System Preferences > Privacy & Security > Full Disk Access
2. Add the app to the allowed list using the + button
3. Remove and re-add the app if it was updated
4. Reset TCC permissions for full disk access
5. Check for MDM restrictions

```bash
# Check full disk access permissions
sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db "SELECT client FROM access WHERE service='kTCCServiceSystemPolicyAllFiles';"

# Reset full disk access permissions
tccutil reset SystemPolicyAllFiles
```

## Examples

```bash
# View TCC database entries
sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db "SELECT * FROM access;"
```

This error is common after updating an app when permissions need to be re-granted, when the TCC database is corrupted, or when MDM profiles restrict full disk access.

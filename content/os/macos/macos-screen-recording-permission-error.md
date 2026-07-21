---
title: "[Solution] macOS Screen Recording Permission Error -- App Cannot Record Screen"
description: "Fix macOS screen recording permission error when an app cannot record the screen. Resolve screen recording permission issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Screen Recording Permission Error -- App Cannot Record Screen

Apps need screen recording permission to capture the screen content. When permission is not granted, the app cannot record or stream the screen.

## Common Causes
- Screen recording permission was not granted in System Preferences
- App was updated and needs permission re-granted
- TCC database is corrupted
- Screen recording is restricted by MDM
- macOS version has different screen recording requirements

## How to Fix
1. Open System Preferences > Privacy & Security > Screen Recording
2. Add the app to the allowed list
3. Restart the app after granting permission
4. Reset TCC permissions and re-grant them
5. Check for MDM restrictions

```bash
# Check screen recording permissions
sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db "SELECT client FROM access WHERE service='kTCCServiceScreenCapture';"

# Reset screen recording permissions
tccutil reset ScreenCapture
```

## Examples

```bash
# Test screen recording
# Open QuickTime Player > File > New Screen Recording
```

This error is common after updating an app when permissions need to be re-granted, when the TCC database is corrupted, or when MDM profiles restrict screen recording.

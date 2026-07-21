---
title: "[Solution] macOS Camera Permission Error -- App Cannot Access Camera"
description: "Fix macOS camera permission error when an app cannot access the camera. Resolve camera permission issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Camera Permission Error -- App Cannot Access Camera

Apps need camera permission to capture photos or video. When permission is not granted, the app cannot access the camera and video capture fails.

## Common Causes
- Camera permission was not granted in System Preferences
- App was updated and needs permission re-granted
- TCC database is corrupted
- Built-in camera hardware issue
- External camera is not detected

## How to Fix
1. Open System Preferences > Privacy & Security > Camera
2. Add the app to the allowed list
3. Check that the camera hardware is working
4. Test with a different app to confirm hardware is functional
5. Reset TCC permissions and re-grant them

```bash
# Check camera permissions
sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db "SELECT client FROM access WHERE service='kTCCServiceCamera';"

# Reset camera permissions
tccutil reset Camera
```

## Examples

```bash
# Test camera from terminal
# Open Photo Booth or FaceTime to test
open -a "Photo Booth"
```

This error is common after updating an app when permissions need to be re-granted, when the TCC database is corrupted, or when the camera hardware has an issue.

---
title: "[Solution] macOS Microphone Permission Error -- App Cannot Access Microphone"
description: "Fix macOS microphone permission error when an app cannot access the microphone. Resolve microphone permission issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Microphone Permission Error -- App Cannot Access Microphone

Apps need microphone permission to record audio. When permission is not granted, the app cannot access the microphone and audio recording fails.

## Common Causes
- Microphone permission was not granted in System Preferences
- App was updated and needs permission re-granted
- TCC database is corrupted
- Built-in microphone hardware issue
- External microphone is not detected

## How to Fix
1. Open System Preferences > Privacy & Security > Microphone
2. Add the app to the allowed list
3. Check that the microphone hardware is working
4. Test with a different app to confirm hardware is functional
5. Reset TCC permissions and re-grant them

```bash
# Check microphone permissions
sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db "SELECT client FROM access WHERE service='kTCCServiceMicrophone';"

# Reset microphone permissions
tccutil reset Microphone
```

## Examples

```bash
# Test microphone from terminal (requires installed tools)
# Use Audio MIDI Setup to check input levels
open -a "Audio MIDI Setup"
```

This error is common after updating an app when permissions need to be re-granted, when the TCC database is corrupted, or when the microphone hardware has an issue.

---
title: "[Solution] macOS Audio Input Error -- Mac Microphone Not Working"
description: "Fix macOS audio input error when the Mac microphone is not picking up sound. Resolve audio input issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Audio Input Error -- Mac Microphone Not Working

Audio input errors prevent the microphone from capturing sound. This affects voice calls, recording, and voice recognition features.

## Common Causes
- Microphone is muted or volume is set to zero
- Wrong input device is selected
- Microphone permission is not granted
- Core Audio input service has crashed
- External microphone is not detected

## How to Fix
1. Check the input device and volume in System Preferences > Sound > Input
2. Ensure the microphone is not physically muted
3. Grant microphone permission to the app
4. Restart the Core Audio service
5. Test with a different microphone

```bash
# Check audio input devices
system_profiler SPAudioDataType

# Restart Core Audio
sudo launchctl stop com.apple.audio.coreaudiod
sudo launchctl start com.apple.audio.coreaudiod
```

## Examples

```bash
# Check input levels
# System Preferences > Sound > Input > observe input level meter
```

This error is common when the wrong input device is selected, when microphone permissions are not granted, or when Core Audio input service has crashed.

---
title: "[Solution] macOS Volume Error -- Mac Volume Not Working or Stuck"
description: "Fix macOS volume error when Mac volume controls do not work or volume is stuck. Resolve volume issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Volume Error -- Mac Volume Not Working or Stuck

Volume controls on Mac allow you to adjust audio output level. When they fail, the volume may be stuck at a certain level, the keys may not respond, or the volume slider may be greyed out.

## Common Causes
- Audio device is not selected correctly
- Core Audio service has crashed
- Volume keys are not mapped correctly
- Audio MIDI Setup has incorrect volume settings
- SMC is not managing audio hardware correctly

## How to Fix
1. Check the audio output device in System Preferences > Sound
2. Restart the Core Audio service
3. Reset SMC on Intel Macs
4. Check Audio MIDI Setup for volume settings
5. Try adjusting volume from the menu bar instead of keyboard

```bash
# Restart Core Audio
sudo launchctl stop com.apple.audio.coreaudiod
sudo launchctl start com.apple.audio.coreaudiod

# Check volume settings
osascript -e "output volume of (get volume settings)"
```

## Examples

```bash
# Set volume from terminal
osascript -e "set volume output volume 50"

# Check audio device
system_profiler SPAudioDataType
```

This error is common when Core Audio crashes, when the SMC needs a reset, or when the audio device is not selected correctly.

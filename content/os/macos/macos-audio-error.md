---
title: "[Solution] macOS Audio Error — No Sound Output"
description: "Fix macOS audio errors including no sound, crackling, digital distortion, or audio devices not appearing in Sound preferences."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["audio", "sound", "speakers", "headphones", "core-audio", "output"]
weight: 5
---

# macOS Audio Error Fix

Audio errors on macOS include no sound output, crackling or popping, audio cutting out, devices not recognized, or the Audio MIDI Setup showing no devices.

## What This Error Means

macOS uses Core Audio for all sound processing. When audio fails, it's typically a driver issue, misconfigured audio device, or the audio daemon (`coreaudiod`) is stuck.

## Common Causes

- `coreaudiod` daemon crashed or stuck
- Wrong output device selected in Sound preferences
- Audio MIDI format mismatch (sample rate/bit depth)
- USB audio device driver incompatibility
- macOS update changing audio routing

## How to Fix

### 1. Restart the Core Audio daemon

```bash
# Restart the audio service
sudo killall coreaudiod
# macOS will automatically relaunch it
```

### 2. Check and set audio device format

```bash
# List audio devices
system_profiler SPAudioDataType

# Open Audio MIDI Setup
open -a "Audio MIDI Setup"
# Select your output device → ensure format matches (e.g., 44100 Hz, 2ch)
```

### 3. Reset audio preferences

```bash
# Delete audio preference files
defaults delete com.apple.systempreferences
rm -f ~/Library/Preferences/com.apple.sound.*plist

# Restart the Mac
```

### 4. Check for audio device conflicts

```bash
# List all audio devices
coreaudiod --version 2>&1 || true
system_profiler SPAudioDataType | grep -A5 "Default Output"

# Force a specific output device
SwitchAudioSource -s "Built-in Output"
```

## Related Errors

- [Core Audio Error](core-audio) — Core Audio framework errors
- [AVFoundation Error](avfoundation) — audio/video playback framework errors
- [USB Error](macos-usb-error) — USB audio device not recognized

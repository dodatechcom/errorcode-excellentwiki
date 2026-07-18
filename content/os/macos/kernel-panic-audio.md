---
title: "[Solution] macOS Kernel Panic Audio — Audio Driver Crash"
description: "Fix macOS kernel panic caused by audio drivers: system restarts during audio playback, recording, or when connecting audio devices."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 96
---

# Kernel Panic Audio — Audio Driver Crash

Fix macOS kernel panic caused by audio drivers: system restarts during audio playback, recording, or when connecting audio devices.

## Common Causes

- Faulty audio interface driver or USB audio device
- CoreAudio daemon crash triggering kernel panic
- Conflicting audio drivers from third-party DAW or plugins
- Audio hardware failure on older Mac models

## How to Fix

### 1. Check Audio Panic Logs

```bash
log show --predicate 'eventMessage contains "CoreAudio"' --last 24h | grep -i panic
system_profiler SPAudioDataType
```

### 2. Reset Audio Configuration

```bash
sudo rm -f /Library/Preferences/Audio/*.plist
sudo killall coreaudiod
rm -f ~/Library/Preferences/Audio/*.plist
sudo shutdown -r now
```

### 3. Remove Problematic Audio Software

```bash
kextstat | grep -i audio
# Temporarily move third-party audio plugins out of Plug-Ins folder
```

### 4. Test with Different Audio Output

```bash
# System Settings → Sound → Output → Select MacBook Speakers
# Disconnect external audio interface
```

## Common Scenarios

This error commonly occurs when:

- Kernel panic occurs when starting playback in Logic Pro or GarageBand
- Panic log references AppleHDA or CoreAudio in crash stack
- Mac crashes when plugging in or unplugging audio interface
- Audio distortion precedes kernel panic by a few seconds

## Prevent It

- Keep audio interface firmware and drivers updated
- Avoid using multiple audio drivers simultaneously
- Test audio hardware with Apple Diagnostics for frequent panics
- Use built-in audio output as baseline before adding third-party devices

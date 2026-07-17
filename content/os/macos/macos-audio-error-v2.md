---
title: "[Solution] macOS Audio Device Not Found Error"
description: "Fix macOS audio device not found, no sound output, or audio not working errors. Resolve Core Audio issues on Mac."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["audio", "sound", "output", "input", "core-audio", "device", "macos"]
weight: 5
---

# macOS Audio Device Not Found Error

Audio device errors on macOS include no sound output, audio device not appearing in Sound settings, or crackling/popping audio.

## What This Error Means

macOS Core Audio manages all audio input and output. When the audio device is not found, it means the audio subsystem cannot initialize the hardware, the device was disconnected, or Core Audio preference files are corrupted.

## Common Causes

- Core Audio daemon (coreaudiod) crashed
- Audio device driver issue (especially third-party USB audio)
- Corrupt audio preference files
- macOS update changed audio device mapping
- Bluetooth audio device disconnected but still selected as output
- Audio MIDI Setup misconfiguration

## How to Fix

### Restart Core Audio

```bash
sudo killall -9 coreaudiod
# Audio will automatically restart
```

### Check Audio Devices

```bash
system_profiler SPAudioDataType
```

### Reset Audio Preferences

```bash
sudo rm -f /Library/Preferences/com.apple.systempreferences.plist
# Restart Mac
```

### Fix Audio MIDI Setup

```bash
open /Applications/Utilities/Audio\ MIDI\ Setup.app
```

Verify correct input/output device is selected and sample rate matches.

### Reset NVRAM/PRAM

```bash
# Intel Mac: Shut down, then hold Option+Command+P+R for 20 seconds
# Apple Silicon: Shut down, hold power button until startup options appear
```

### Check Bluetooth Audio

```bash
# If using Bluetooth headphones, check connection
defaults read com.apple.Bluetooth
```

## Related Errors

- [macOS Bluetooth Error]({{< relref "/os/macos/macos-bluetooth-error-v2" >}}) — Bluetooth device issues
- [macOS USB Error]({{< relref "/os/macos/macos-usb-error-v2" >}}) — USB device recognition issues
- [Core Audio Error]({{< relref "/os/macos/core-audio" >}}) — Core Audio framework errors

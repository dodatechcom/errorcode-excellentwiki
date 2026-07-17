---
title: "[Solution] macOS Core Audio Errors"
description: "Fix macOS Core Audio errors. Causes and solutions for audio hardware, session, and processing failures."
platforms: ["macos"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# macOS Core Audio Errors

Core Audio errors indicate failures in macOS audio subsystem, including hardware device issues, session management, and audio processing pipeline failures.

## What This Error Means

Core Audio errors use `OSStatus` codes:

- `kAudioHardwareNotRunningError (-2005137727)` — Audio hardware is not running
- `kAudioHardwareBadDeviceError (-2005137728)` — Invalid audio device reference
- `kAudioHardwareBadStreamError (-2005137730)` — Invalid audio stream
- `kAudioDeviceUnsupportedFormatError (-2005137722)` — Audio format not supported by device

## Common Causes

- Audio device disconnected or not recognized
- Audio hardware in use by another application exclusively
- Sample rate or format mismatch between source and device
- Audio driver conflict or missing driver

## How to Fix

### Check Audio Device Status

```bash
# List audio devices
system_profiler SPAudioDataType

# Check Core Audio device state
coreaudio-toolbox-info 2>/dev/null || echo "Use System Information app"
```

### Reset Audio System

```bash
# Restart Core Audio daemon
sudo killall coreaudiod

# Audio daemon will restart automatically
```

### Verify Audio Format Compatibility

```swift
import AVFoundation

let session = AVAudioSession.sharedInstance()
do {
    try session.setPreferredSampleRate(44100.0)
    try session.setCategory(.playback, mode: .default)
    try session.setActive(true)
} catch {
    print("Audio session error: \(error)")
}
```

### Reconnect Audio Device

```bash
# Check USB audio devices
system_profiler SPUSBDataType | grep -A5 "Audio"

# Reset Bluetooth audio
sudo defaults write com.apple.Bluetooth ControllerPowerState 0
sudo defaults write com.apple.Bluetooth ControllerPowerState 1
```

## Related Errors

- [AVFoundation Errors]({{< relref "/os/macos/avfoundation" >}}) — Higher-level audio/video capture errors
- [Cocoa Error Codes]({{< relref "/os/macos/cocoa-error" >}}) — Foundation errors wrapping Core Audio issues
- [Metal GPU Errors]({{< relref "/os/macos/metal-error" >}}) — Related hardware subsystem errors

---
title: "[Solution] macOS AVFoundation Camera/AV Errors"
description: "Fix macOS AVFoundation camera and AV errors. Causes and solutions for video capture, playback, and media processing failures."
platforms: ["macos"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# macOS AVFoundation Camera/AV Errors

AVFoundation errors indicate failures in camera capture, video playback, and media processing. These errors use `AVErrorDomain` and appear in applications using the AVFoundation framework.

## What This Error Means

Common AVFoundation error codes:

- `AVErrorSessionNotRunning (-11800)` — Capture session is not running
- `AVErrorMediaServicesWereReset (-11819)` — Media services daemon restarted
- `AVErrorDeviceNotConnected (-11801)` — Camera or microphone is disconnected
- `AVErrorInvalidComposition (-11821)` — Media composition is invalid
- `AVErrorExportFailed (-11820)` — Export operation failed

## Common Causes

- Camera or microphone permission not granted in System Preferences
- Camera is in use by another application
- Media services daemon (mediaserverd) crashed
- Invalid video format or codec configuration

## How to Fix

### Verify Camera Permissions

```bash
# Check camera permission status
tccutil reset Camera
tccutil reset Microphone
```

### Check Camera Availability

```swift
import AVFoundation

guard AVCaptureDevice.default(for: .video) != nil else {
    print("No camera available")
    return
}

AVCaptureDevice.requestAccess(for: .video) { granted in
    if granted {
        print("Camera access granted")
    } else {
        print("Camera access denied — check System Preferences > Privacy")
    }
}
```

### Reset Media Services

```bash
# Restart media services daemon
sudo killall mediaserverd
sudo killall mediaremoteagent
```

### Check for Device Conflicts

```bash
# Check which apps are using the camera
sudo lsof /dev/video*
```

## Related Errors

- [Core Audio Errors]({{< relref "/os/macos/core-audio" >}}) — Audio capture hardware errors
- [NSURLError]({{< relref "/os/macos/nsurlerror" >}}) — Network errors for streaming media
- [Core Foundation Errors]({{< relref "/os/macos/core-foundation" >}}) — Low-level framework errors

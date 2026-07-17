---
title: "[Solution] ARKit Session Interruption Error Fix"
description: "Fix ARKit session interruption and error handling in iOS augmented reality apps."
languages: ["swift"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["ARKit", "session", "interruption", "augmented-reality", "swift"]
weight: 5
---

# ARKit: Session Interruption Error Fix

An ARKit session interruption error occurs when the AR session is interrupted by phone calls, app backgrounding, or camera access issues.

## What This Error Means

`ARSession` manages the camera and motion tracking. Interruptions occur when the camera is taken by another app, the device moves too fast, or tracking quality degrades.

## Common Causes

- Phone call or notification interrupts camera
- App goes to background
- Insufficient lighting for tracking
- Camera not available (used by another app)
- Device motion too fast for tracking

## How to Fix

### 1. Handle session interruptions

```swift
// CORRECT: Implement ARSessionDelegate
extension ViewController: ARSessionDelegate {
    func sessionWasInterrupted(_ session: ARSession) {
        print("Session interrupted")
        // Pause UI updates
    }

    func sessionInterruptionEnded(_ session: ARSession) {
        print("Session resumed")
        // Reset and restart tracking
        resetTracking()
    }

    func session(_ session: ARSession, didFailWithError error: Error) {
        print("Session failed: \(error)")
        if let arError = error as? ARError {
            switch arError.code {
            case .worldTrackingFailed:
                resetTracking()
            case .sensorUnavailable:
                showCameraAccessAlert()
            default:
                break
            }
        }
    }
}
```

### 2. Reset tracking when needed

```swift
// CORRECT: Reset AR tracking
func resetTracking() {
    let config = ARWorldTrackingConfiguration()
    config.planeDetection = [.horizontal, .vertical]
    sceneView.session.run(config, options: [.resetTracking, .removeExistingAnchors])
}
```

### 3. Request camera permission properly

```swift
// CORRECT: Check camera access
func checkCameraAccess() {
    switch AVCaptureDevice.authorizationStatus(for: .video) {
    case .authorized:
        startARSession()
    case .notDetermined:
        AVCaptureDevice.requestAccess(for: .video) { granted in
            if granted { self.startARSession() }
        }
    case .denied, .restricted:
        showCameraAccessAlert()
    @unknown default:
        break
    }
}
```

### 4. Handle low tracking quality

```swift
// CORRECT: Monitor tracking quality
func session(_ session: ARSession, didUpdate frame: ARFrame) {
    switch frame.camera.trackingState {
    case .normal:
        // Good tracking
        break
    case .limited(let reason):
        print("Tracking limited: \(reason)")
        // Show guidance to user
    case .notAvailable:
        print("Tracking unavailable")
    }
}
```

## Related Errors

- [ARKit Error]({{< relref "/languages/swift/arkit-error" >}}) — ARKit general errors
- [CoreML Error](coreml-error-v2) — model loading
- [Swift Concurrency Error](swift-concurrency-error-v2) — concurrency issues

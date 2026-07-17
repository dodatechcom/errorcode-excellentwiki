---
title: "[Solution] Swift AVFoundation Recording Error Fix"
description: "Fix Swift AVFoundation recording errors. Learn why audio/video recording fails and how to handle AVFoundation issues."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

An AVFoundation recording error occurs when audio or video recording fails. This can happen due to missing permissions, hardware issues, or configuration errors.

## Common Causes

- Missing microphone/camera permission
- Audio session not configured
- Hardware unavailable
- Storage space full

## How to Fix

```swift
// WRONG: Not requesting recording permission
import AVFoundation

let session = AVCaptureSession()
// May fail without permission

// CORRECT: Request permission first
AVCaptureDevice.requestAccess(for: .audio) { granted in
    if granted {
        AVCaptureDevice.requestAccess(for: .video) { videoGranted in
            if videoGranted {
                // Start recording
            }
        }
    }
}
```

```swift
// WRONG: Not configuring audio session
let recorder = AVAudioRecorder(url: url, settings: [:])  // Wrong settings

// CORRECT: Configure audio session
let session = AVAudioSession.sharedInstance()
do {
    try session.setCategory(.playAndRecord, mode: .default)
    try session.setActive(true)
} catch {
    print("Audio session failed: \(error)")
}
```

## Examples

```swift
// Example 1: Basic audio recording
import AVFoundation

var audioRecorder: AVAudioRecorder?

func startRecording() {
    let audioSession = AVAudioSession.sharedInstance()
    try? audioSession.setCategory(.playAndRecord, mode: .default)
    try? audioSession.setActive(true)

    let url = FileManager.default.temporaryDirectory.appendingPathComponent("recording.m4a")
    let settings = [
        AVFormatIDKey: Int(kAudioFormatMPEG4AAC),
        AVSampleRateKey: 44100,
        AVNumberOfChannelsKey: 1,
        AVEncoderAudioQualityKey: AVAudioQuality.high.rawValue
    ]

    audioRecorder = try? AVAudioRecorder(url: url, settings: settings)
    audioRecorder?.record()
}

// Example 2: Video recording
let session = AVCaptureSession()
let output = AVCaptureMovieFileOutput()
if session.canAddOutput(output) {
    session.addOutput(output)
}
output.startRecording(to: url, recordingDelegate: self)

// Example 3: Stop recording
audioRecorder?.stop()
try? AVAudioSession.sharedInstance().setActive(false)
```

## Related Errors

- [AVFoundation playback error](AVFoundation-player-error) — playback failed
- [WKWebView JavaScript error](wkwebview-error) — web view error
- [PDFKit rendering error](pdfkit-error) — PDF rendering failed

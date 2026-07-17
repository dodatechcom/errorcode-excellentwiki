---
title: "[Solution] Swift AVFoundation Playback Error Fix"
description: "Fix Swift AVFoundation playback errors. Learn why audio/video playback fails and how to handle AVPlayer issues."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["avfoundation", "playback", "avplayer", "swift"]
weight: 5
---

## What This Error Means

An AVFoundation playback error occurs when audio or video playback fails. This can happen due to invalid URLs, unsupported formats, network issues, or player configuration problems.

## Common Causes

- Invalid or unreachable media URL
- Unsupported media format
- Network timeout during streaming
- Player not properly configured

## How to Fix

```swift
// WRONG: Not handling playback errors
let player = AVPlayer(url: url)
player.play()  // May fail silently

// CORRECT: Observe player errors
import AVFoundation

player.addObserver(self, forKeyPath: "status", options: [.new], context: nil)
player.addObserver(self, forKeyPath: "error", options: [.new], context: nil)

override func observeValue(forKeyPath keyPath: String?, of object: Any?, change: [NSKeyValueChangeKey: Any]?, context: UnsafeMutableRawPointer?) {
    if keyPath == "status" {
        switch player.status {
        case .readyToPlay:
            player.play()
        case .failed:
            print("Player error: \(player.error?.localizedDescription ?? "unknown")")
        default:
            break
        }
    }
}
```

```swift
// WRONG: Playing URL without validation
let url = URL(string: "invalid-url")
let player = AVPlayer(url: url!)  // Crash

// CORRECT: Validate URL
if let url = URL(string: "https://example.com/video.mp4") {
    let player = AVPlayer(url: url)
    player.play()
}
```

## Examples

```swift
// Example 1: Basic AVPlayer usage
import AVKit

let url = URL(string: "https://example.com/video.mp4")!
let player = AVPlayer(url: url)
let playerLayer = AVPlayerLayer(player: player)
playerLayer.frame = view.bounds
view.layer.addSublayer(playerLayer)
player.play()

// Example 2: Player with time observer
let interval = CMTime(seconds: 1, preferredTimescale: 600)
player.addPeriodicTimeObserver(forInterval: interval, queue: .main) { time in
    print("Current time: \(time.seconds)")
}

// Example 3: Handle buffering
player.currentItem?.addObserver(self, forKeyPath: "playbackBufferEmpty", options: .new, context: nil)
player.currentItem?.addObserver(self, forKeyPath: "playbackLikelyToKeepUp", options: .new, context: nil)
```

## Related Errors

- [AVFoundation recording error](AVFoundation-error-swift) — recording failed
- [WKWebView JavaScript error](wkwebview-error) — web view error
- [PDFKit rendering error](pdfkit-error) — PDF rendering failed

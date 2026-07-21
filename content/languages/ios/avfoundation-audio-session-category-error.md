---
title: "[Solution] AVFoundation Audio Session Category Error"
description: "Fix AVAudioSession category configuration errors in iOS apps."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# AVFoundation Audio Session Category Error

Incorrect audio session category causes audio to not play, interruptions, or conflicts with other audio sources.

## Common Causes
- Wrong category set for playback type
- Category changed during active playback
- Missing category options for background audio
- Interruption handling not implemented

## How to Fix
1. Set the appropriate category before playing audio
2. Configure category options for your use case
3. Handle audio session interruptions
4. Reactivate audio session after interruptions

```swift
// Set audio session category:
do {
    try AVAudioSession.sharedInstance().setCategory(.playback, mode: .default)
    try AVAudioSession.sharedInstance().setActive(true)
} catch {
    print("Audio session setup failed: \(error)")
}
```

## Examples
```swift
// Handle audio interruptions:
NotificationCenter.default.addObserver(
    forName: AVAudioSession.interruptionNotification,
    object: nil, queue: nil
) { notification in
    guard let userInfo = notification.userInfo,
          let typeValue = userInfo[AVAudioSessionInterruptionTypeKey] as? UInt,
          let type = AVAudioSession.InterruptionType(rawValue: typeValue) else { return }
    switch type {
    case .began: player.pause()
    case .ended: try? AVAudioSession.sharedInstance().setActive(true); player.play()
    @unknown default: break
    }
}
```

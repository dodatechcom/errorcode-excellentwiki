---
title: "[Solution] AVFoundation Video Export Error"
description: "Fix AVAssetExportSession video export failures in iOS apps."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# AVFoundation Video Export Error

Video export fails when the output URL is invalid, the preset is incompatible with the asset, or the export session encounters encoding issues.

## Common Causes
- Output URL already exists and cannot be overwritten
- Export preset not compatible with asset format
- Export session cancelled or timed out
- Output file type not supported by preset

## How to Fix
1. Remove existing file at output URL before export
2. Choose compatible export preset
3. Handle export session status changes
4. Set appropriate output file type

```swift
// Export video:
let asset = AVAsset(url: videoURL)
guard let exportSession = AVAssetExportSession(asset: asset, presetName: AVAssetExportPresetHighestQuality) else { return }

let outputURL = FileManager.default.temporaryDirectory.appendingPathComponent("export.mp4")
try? FileManager.default.removeItem(at: outputURL)

exportSession.outputURL = outputURL
exportSession.outputFileType = .mp4

exportSession.exportAsynchronously {
    if exportSession.status == .completed {
        print("Export succeeded")
    }
}
```

## Examples
```swift
// Export with progress monitoring:
func exportVideo(from asset: AVAsset, to url: URL) {
    guard let session = AVAssetExportSession(asset: asset, presetName: AVAssetExportPresetMediumQuality) else { return }
    session.outputURL = url
    session.outputFileType = .mp4
    session.shouldOptimizeForNetworkUse = true

    let timer = Timer.scheduledTimer(withTimeInterval: 0.1, repeats: true) { _ in
        print("Progress: \(session.progress * 100)%")
    }

    session.exportAsynchronously {
        timer.invalidate()
        switch session.status {
        case .completed: print("Done")
case .failed: print("Failed: \(session.error?.localizedDescription ?? \"unknown\")")
default: break
        }
    }
}
```

---
title: "[Solution] Vision VNImageRequestHandler Error"
description: "Fix Vision framework request handler initialization errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Vision VNImageRequestHandler Error

VNImageRequestHandler fails when initialized with invalid image data, incorrect orientation, or when the request is not properly configured.

## Common Causes
- Image data is nil or corrupt
- Orientation value incorrect for the image
- Request options missing required keys
- Handler created on wrong thread

## How to Fix
1. Verify image data or CGImage is valid
2. Set correct orientation (CGImagePropertyOrientation)
3. Provide proper options dictionary
4. Create handler and perform requests on same queue

```swift
// Create handler with image:
guard let cgImage = UIImage(named: "photo")?.cgImage else { return }
let handler = VNImageRequestHandler(cgImage: cgImage, orientation: .up)

let request = VNDetectFaceRectanglesRequest { request, error in
    guard let results = request.results as? [VNFaceObservation] else { return }
    print("Found \(results.count) faces")
}

try? handler.perform([request])
```

## Examples
```swift
// Vision request with options:
let handler = VNImageRequestHandler(
    cgImage: cgImage,
    orientation: .up,
    options: [:]
)

let request = VNGenerateImageFeaturePrintRequest()
try handler.perform([request])

if let results = request.results as? [VNFeaturePrintObservation] {
    // Process results
}
```

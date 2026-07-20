---
title: "[Solution] Swift Vision Framework Error — Request & Recognition"
description: "Fix Swift Vision framework errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 143
---

Vision framework errors occur when requests aren't properly configured, observation handling fails, or image preparation is incorrect.

## Common Causes

```swift
// Not handling request results
let request = VNDetectBarcodesRequest { request, error in
    // Not checking for nil observations
}

// Wrong image orientation
let handler = VNImageRequestHandler(cgImage: cgImage, orientation: .up)
```

## How to Fix

**1. Text recognition**

```swift
import Vision

func recognizeText(in image: CGImage) {
    let request = VNRecognizeTextRequest { request, error in
        guard let observations = request.results as? [VNRecognizedTextObservation] else {
            return
        }
        for observation in observations {
            if let topCandidate = observation.topCandidates(1).first {
                print("Text: \(topCandidate.string)")
            }
        }
    }
    request.recognitionLevel = .accurate
    
    let handler = VNImageRequestHandler(cgImage: image, options: [:])
    try? handler.perform([request])
}
```

**2. Barcode detection**

```swift
func detectBarcodes(in image: CGImage) {
    let request = VNDetectBarcodesRequest { request, error in
        guard let observations = request.results as? [VNBarcodeObservation] else {
            return
        }
        for barcode in observations {
            print("Barcode: \(barcode.payloadStringValue ?? "unknown")")
            print("Type: \(barcode.symbology.rawValue)")
        }
    }
    
    let handler = VNImageRequestHandler(cgImage: image, options: [:])
    try? handler.perform([request])
}
```

**3. Face detection**

```swift
func detectFaces(in image: CGImage) {
    let request = VNDetectFaceRectanglesRequest { request, error in
        guard let faces = request.results as? [VNFaceObservation] else {
            return
        }
        print("Found \(faces.count) faces")
    }
    
    let handler = VNImageRequestHandler(cgImage: image, options: [:])
    try? handler.perform([request])
}
```

**4. Async/await usage**

```swift
func recognizeTextAsync(in image: CGImage) async throws -> [String] {
    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    
    let handler = VNImageRequestHandler(cgImage: image, options: [:])
    try handler.perform([request])
    
    return (request.results as? [VNRecognizedTextObservation])?
        .compactMap { $0.topCandidates(1).first?.string } ?? []
}
```

**5. CIImage integration**

```swift
func processImage(_ ciImage: CIImage) {
    let handler = VNImageRequestHandler(ciImage: ciImage, options: [:])
    let request = VNRecognizeTextRequest()
    try? handler.perform([request])
}
```

## Examples

Complete Vision processing:

```swift
class VisionProcessor {
    func processImage(at url: URL) async throws -> [String] {
        let data = try Data(contentsOf: url)
        guard let image = NSImage(data: data)?.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
            throw VisionError.invalidImage
        }
        
        return try await recognizeText(in: image)
    }
    
    private func recognizeText(in cgImage: CGImage) async throws -> [String] {
        let request = VNRecognizeTextRequest()
        request.recognitionLevel = .accurate
        request.usesLanguageCorrection = true
        
        let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
        try handler.perform([request])
        
        return (request.results as? [VNRecognizedTextObservation])?
            .compactMap { $0.topCandidates(1).first?.string } ?? []
    }
}

enum VisionError: Error {
    case invalidImage
    case processingFailed
}
```

## Related Errors

- [CoreML Error](/languages/swift/coreml-error)
- [Data Error](/languages/swift/swift-data-error)
- [PhotoKit Error](/languages/swift/swift-photokit-error)

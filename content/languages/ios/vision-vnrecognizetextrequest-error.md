---
title: "[Solution] Vision VNRecognizeTextRequest Error"
description: "Fix Vision text recognition request errors and accuracy issues in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Vision VNRecognizeTextRequest Error

Text recognition fails when the image is too low resolution, when the request language is not supported, or when the recognition level is not appropriate for the content.

## Common Causes
- Image resolution too low for text recognition
- Language not supported by on-device recognition
- Recognition level set too low for complex text
- Image orientation incorrect

## How to Fix
1. Provide high-resolution images for text recognition
2. Specify supported languages in the request
3. Use .accurate recognition level for best results
4. Set correct image orientation

```swift
// Text recognition request:
let request = VNRecognizeTextRequest { request, error in
    guard let observations = request.results as? [VNRecognizedTextObservation] else { return }
    for observation in observations {
        if let topCandidate = observation.topCandidates(1).first {
            print("Text: \(topCandidate.string)")
        }
    }
}
request.recognitionLevel = .accurate
request.recognitionLanguages = ["en-US"]

let handler = VNImageRequestHandler(cgImage: image.cgImage!, orientation: .up)
try? handler.perform([request])
```

## Examples
```swift
// Text recognition with preprocessing:
func recognizeText(in image: UIImage) {
    guard let cgImage = image.cgImage else { return }
    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = true
    request.recognitionLanguages = ["en-US", "fr-FR"]

    let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
    try? handler.perform([request])

    guard let results = request.results else { return }
    let text = results.compactMap { $0.topCandidates(1).first?.string }.joined(separator: "\n")
    print(text)
}
```

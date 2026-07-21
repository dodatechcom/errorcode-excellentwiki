---
title: "[Solution] Core ML Model Loading Error"
description: "Fix Core ML model loading failures in iOS applications."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Core ML Model Loading Error

Core ML models fail to load when the model file is missing, incompatible with the current device, or compiled for a different platform.

## Common Causes
- Model file not included in the bundle
- Model compiled for wrong platform
- Input or output configuration mismatch
- Model requires features unavailable on device

## How to Fix
1. Verify the .mlmodel file is in the bundle
2. Check model compilation target matches device
3. Verify input/output types match your code
4. Test model loading on the target device

```swift
// Load Core ML model:
guard let model = try? VNCoreMLModel(for: MyModel().model) else {
    print("Failed to load model")
    return
}

let request = VNCoreMLRequest(model: model) { request, error in
    guard let results = request.results as? [VNClassificationObservation] else { return }
    print("Top result: \(results.first?.identifier ?? \"none\")")
}
```

## Examples
```swift
// Model loading with error handling:
func loadModel() -> VNCoreMLModel? {
    guard let url = Bundle.main.url(forResource: "MyModel", withExtension: "mlmodelc") else {
        print("Model file not found")
        return nil
    }
    do {
        let model = try MLModel(contentsOf: url)
        return try VNCoreMLModel(for: model)
    } catch {
        print("Model loading failed: \(error)")
        return nil
    }
}
```

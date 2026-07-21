---
title: "Firebase ML Kit Error"
description: "Fix Firebase ML Kit model loading and inference errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Firebase ML Kit fails to load model or process input data

## Common Causes

- ML model not bundled correctly in APK
- Input format not matching model requirements
- Model file not accessible at runtime
- GPU acceleration not configured

## Fixes

- Verify model file is in assets or bundled correctly
- Check model input/output format documentation
- Use Task API for async inference
- Configure delegate for GPU or NNAPI acceleration

## Code Example

```kotlin
// Bundled model from assets
val localModel = LocalModel.Builder()
    .setAssetFilePath("model.tflite")
    .build()

val options = CustomLocalModel.Options.Builder()
    .setLocalModel(localModel)
    .build()

val detector = Detection.getClient(options)

// Process image:
val image = InputImage.fromFilePath(context, imageUri)
detector.process(image)
    .addOnSuccessListener { results ->
        // Process results
    }
    .addOnFailureListener { e ->
        Log.e("ML", "Inference failed", e)
    }
```

# Download model from Firebase console
# Or bundle in assets/ folder
# Use Task API for async results

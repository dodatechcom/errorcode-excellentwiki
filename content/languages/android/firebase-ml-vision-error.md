---
title: "Firebase ML Vision Error"
description: "Fix Firebase ML Vision text and image recognition errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Firebase ML Vision fails to detect text or objects in images

## Common Causes

- Camera image format not compatible with ML Vision
- Image resolution too low for accurate detection
- Vision client not properly configured
- Results not processed on correct thread

## Fixes

- Convert camera image to InputImage correctly
- Ensure adequate image resolution
- Use appropriate Vision API for task
- Process results on main thread

## Code Example

```kotlin
val image = InputImage.fromMediaImage(
    mediaImage,
    imageInfo.rotationDegrees
)

val recognizer = TextRecognition.getClient(ChineseTextRecognizerOptions.Builder().build())

recognizer.process(image)
    .addOnSuccessListener { visionText ->
        for (block in visionText.textBlocks) {
            val text = block.text
            for (line in block.lines) {
                Log.d("Vision", line.text)
            }
        }
    }
    .addOnFailureListener { e ->
        Log.e("Vision", "Text recognition failed", e)
    }
```

# TextRecognition: text detection
# BarcodeScanning: barcode detection
# FaceDetection: face detection
# ImageLabeling: object classification

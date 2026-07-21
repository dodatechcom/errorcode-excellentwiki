---
title: "CameraX Analysis Error"
description: "Fix CameraX image analysis and frame processing errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
CameraX image analysis does not process frames correctly

## Common Causes

- ImageAnalysis not configured with analyzer
- Analyzer not handling ImageProxy correctly
- ImageProxy not closed after processing
- Analysis resolution too high causing frame drops

## Fixes

- Set ImageAnalysis with appropriate resolution
- Close ImageProxy in finally block after processing
- Use backpressure strategy for frame handling
- Process on background thread

## Code Example

```kotlin
val imageAnalysis = ImageAnalysis.Builder()
    .setTargetAspectRatio(AspectRatio.RATIO_4_3)
    .setBackpressureStrategy(ImageAnalysis.STRATEGY_KEEP_ONLY_LATEST)
    .build()

imageAnalysis.setAnalyzer(ContextCompat.getMainExecutor(context)) { imageProxy ->
    val mediaImage = imageProxy.image
    if (mediaImage != null) {
        val image = InputImage.fromMediaImage(
            mediaImage,
            imageProxy.imageInfo.rotationDegrees
        )
        // Process image...
    }
    imageProxy.close()  // Always close!
}
```

# STRATEGY_KEEP_ONLY_LATEST: drop frames if busy
# Always close ImageProxy to free camera resources
# Use background thread for heavy processing

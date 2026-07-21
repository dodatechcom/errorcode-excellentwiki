---
title: "CameraX Capture Error"
description: "Fix CameraX image capture and file saving errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
CameraX image capture fails or saved image is corrupted

## Common Causes

- File output path not accessible
- ImageCapture not configured before capture
- Capture callback error not handled
- Image saved to external storage without permission

## Fixes

- Ensure output file is in accessible directory
- Configure ImageCapture before binding to lifecycle
- Handle capture callback with onSuccess/onError
- Use MediaStore API for saving to gallery

## Code Example

```kotlin
val imageCapture = ImageCapture.Builder()
    .setCaptureMode(ImageCapture.CAPTURE_MODE_MINIMIZE_LATENCY)
    .build()

val outputOptions = ImageCapture.OutputFileOptions.Builder(file).build()

imageCapture.takePicture(
    outputOptions,
    ContextCompat.getMainExecutor(context),
    object : ImageCapture.OnImageSavedCallback {
        override fun onImageSaved(output: ImageCapture.OutputFileResults) {
            val savedUri = output.savedUri
        }
        override fun onError(exception: ImageCaptureException) {
            Log.e("Camera", "Capture failed: ${exception.message}")
        }
    }
)
```

# Save to app-specific directory:
# context.getExternalFilesDir(Environment.DIRECTORY_PICTURES)
# Use MediaStore for gallery visibility

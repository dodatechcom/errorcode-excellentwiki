---
title: "CameraX Preview Error"
description: "Fix CameraX preview configuration and display errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
CameraX preview does not show or shows black screen

## Common Causes

- PreviewView not properly bound to lifecycle
- Camera permission not granted
- Camera use case not configured correctly
- Preview not using correct implementation mode

## Fixes

- Bind CameraX to lifecycle with LifecycleOwner
- Request CAMERA permission before opening camera
- Configure Preview use case with setSurfaceProvider
- Use ImplementationMode.COMPATIBLE or PERFORMANCE

## Code Example

```kotlin
val cameraProviderFuture = ProcessCameraProvider.getInstance(context)
cameraProviderFuture.addListener({
    val cameraProvider = cameraProviderFuture.get()

    val preview = Preview.Builder()
        .setTargetAspectRatio(AspectRatio.RATIO_4_3)
        .build()
        .also { it.setSurfaceProvider(previewView.surfaceProvider) }

    val imageCapture = ImageCapture.Builder()
        .setTargetAspectRatio(AspectRatio.RATIO_4_3)
        .build()

    val cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA

    cameraProvider.unbindAll()
    cameraProvider.bindToLifecycle(
        this, cameraSelector, preview, imageCapture
    )
}, ContextCompat.getMainExecutor(context))
```

# PreviewView in layout:
# <androidx.camera.view.PreviewView
#     android:id="@+id/previewView" />

# Bind to lifecycle before opening camera

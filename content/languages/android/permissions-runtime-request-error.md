---
title: "Runtime Permission Request Error"
description: "Fix Android runtime permission request flow errors and denied permission handling"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Runtime permission request fails or app crashes after permission denied

## Common Causes

- Requesting permission before checking shouldShowRequestPermissionRationale
- Permission request callback not properly handled
- App crashes after permission denied without fallback
- Multiple permissions requested simultaneously incorrectly

## Fixes

- Check shouldShowRequestPermissionRationale before requesting
- Handle permission result in onRequestPermissionsResult
- Provide graceful fallback when permission denied
- Use requestPermissions() with multiple permissions array

## Code Example

```kotlin
// Request permission properly
fun requestCameraPermission() {
    when {
        ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA)
            == PackageManager.PERMISSION_GRANTED -> {
            openCamera()
        }
        shouldShowRequestPermissionRationale(Manifest.permission.CAMERA) -> {
            showRationaleDialog("Camera needed for photos")
        }
        else -> {
            ActivityCompat.requestPermissions(this,
                arrayOf(Manifest.permission.CAMERA), REQUEST_CAMERA)
        }
    }
}

override fun onRequestPermissionsResult(
    requestCode: Int, permissions: Array<String>, grantResults: IntArray
) {
    super.onRequestPermissionsResult(requestCode, permissions, grantResults)
    if (requestCode == REQUEST_CAMERA) {
        if (grantResults.isNotEmpty() && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
            openCamera()
        } else {
            showSettingsRedirect()
        }
    }
}
```

# Use ActivityResultContracts for modern approach:
val launcher = registerForActivityResult(
    RequestPermission()
) { granted -> if (granted) openCamera() }
launcher.launch(Manifest.permission.CAMERA)

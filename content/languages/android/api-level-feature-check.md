---
title: "Hardware Feature Not Available"
description: "Fix Android hardware feature check errors for devices without required sensors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App crashes because device lacks required hardware feature declared in manifest

## Common Causes

- Using camera without checking hasSystemFeature
- NFC not available but app assumes it exists
- GPS hardware missing on WiFi-only tablet
- Bluetooth LE not supported on older device

## Fixes

- Check hasSystemFeature() before using hardware
- Declare feature as android:required=false
- Provide graceful fallback for missing features
- Use PackageManager to query available features

## Code Example

```kotlin
<!-- Declare optional feature -->
<uses-feature android:name="android.hardware.camera"
    android:required="false" />

<!-- Check at runtime -->
val hasCamera = packageManager.hasSystemFeature(PackageManager.FEATURE_CAMERA_ANY)
if (hasCamera) {
    openCamera()
} else {
    showCameraUnavailableMessage()
}
```

# Common features to check:
# FEATURE_CAMERA_ANY
# FEATURE_BLUETOOTH_LE
# FEATURE_NFC
# FEATURE_SENSOR_ACCELEROMETER
# FEATURE_TOUCHSCREEN

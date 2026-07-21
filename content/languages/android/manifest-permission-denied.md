---
title: "Permission Not Declared in Manifest"
description: "Fix Android permission denied errors caused by missing manifest permissions"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App throws SecurityException because required permission is not in manifest

## Common Causes

- Permission tag missing from AndroidManifest.xml
- Using dangerous permission without runtime request
- Permission in wrong scope (manifest vs uses-permission)
- Target SDK requires new permission model

## Fixes

- Add uses-permission tag for required permissions
- Implement runtime permission request for API 23+
- Check permission group for runtime vs install-time
- Request permissions before API call

## Code Example

```kotlin
<!-- AndroidManifest.xml -->
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.READ_CONTACTS" />

<!-- For background location (API 30+) -->
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

# Runtime permission request (Kotlin)
if (ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA)
    != PackageManager.PERMISSION_GRANTED) {
    ActivityCompat.requestPermissions(this,
        arrayOf(Manifest.permission.CAMERA), REQUEST_CODE)
}

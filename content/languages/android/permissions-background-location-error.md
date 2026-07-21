---
title: "Background Location Permission Error"
description: "Fix Android 10+ background location permission access and request errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App cannot access location in background because background permission is not properly requested

## Common Causes

- ACCESS_BACKGROUND_LOCATION not declared in manifest
- Requesting background location without foreground first
- Android 11+ requires separate background location request
- Location permission dialog shows wrong option

## Fixes

- Add ACCESS_BACKGROUND_LOCATION to manifest
- Request foreground location first, then background
- Use ActivityResultContracts for two-step request
- Show explanation before requesting background access

## Code Example

```kotlin
<!-- Manifest -->
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />

// Two-step request (Android 11+):
val foregroundPermissionLauncher = registerForActivityResult(
    RequestMultiplePermissions()
) { permissions ->
    if (permissions[Manifest.permission.ACCESS_FINE_LOCATION] == true) {
        // Now request background
        backgroundPermissionLauncher.launch(
            Manifest.permission.ACCESS_BACKGROUND_LOCATION
        )
    }
}

val backgroundPermissionLauncher = registerForActivityResult(
    RequestPermission()
) { granted ->
    if (granted) enableBackgroundLocation()
}
```

# Android 10+: background location is separate
# Android 11+: requires foreground first
# Android 12+: approximate location option removed

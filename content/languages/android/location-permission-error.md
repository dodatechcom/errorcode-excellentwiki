---
title: "Location Permission Error"
description: "Fix Android location permission errors for GPS and network provider"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Location request fails because of missing or improperly handled permissions

## Common Causes

- ACCESS_FINE_LOCATION not requested
- ACCESS_COARSE_LOCATION insufficient for GPS
- Background location permission not requested (API 29+)
- Permission request not shown to user

## Fixes

- Request ACCESS_FINE_LOCATION for GPS accuracy
- Request foreground location first, then background
- Use ActivityResultContracts for modern permission flow
- Handle denied permissions gracefully

## Code Example

```kotlin
// Request location permission
val locationPermissionRequest = registerForActivityResult(
    ActivityResultContracts.RequestMultiplePermissions()
) { permissions ->
    when {
        permissions[Manifest.permission.ACCESS_FINE_LOCATION] == true -> {
            startLocationUpdates()
        }
        permissions[Manifest.permission.ACCESS_COARSE_LOCATION] == true -> {
            startLocationUpdates()  // Coarse accuracy
        }
        else -> {
            showPermissionDeniedMessage()
        }
    }
}

locationPermissionRequest.launch(arrayOf(
    Manifest.permission.ACCESS_FINE_LOCATION,
    Manifest.permission.ACCESS_COARSE_LOCATION
))
```

# ACCESS_FINE_LOCATION: GPS accuracy
# ACCESS_COARSE_LOCATION: network accuracy
# ACCESS_BACKGROUND_LOCATION: background (API 29+)

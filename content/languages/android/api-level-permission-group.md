---
title: "Permission Group Configuration Error"
description: "Fix permission group errors for Android runtime permissions and API levels"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Runtime permission request fails because permission group is misconfigured

## Common Causes

- Requesting permission from wrong group
- Multiple permissions from same group requested separately
- Group behavior changed in newer API level
- Permission not in expected group for device manufacturer

## Fixes

- Group permissions by group for batch requests
- Check current group mappings for target API level
- Use requestPermissions() with array of same-group permissions
- Handle denied permissions gracefully

## Code Example

```kotlin
// Request all camera permissions at once
val permissions = arrayOf(
    Manifest.permission.CAMERA,
    Manifest.permission.READ_MEDIA_IMAGES
)
ActivityCompat.requestPermissions(this, permissions, REQUEST_CODE)
```

# Permission groups (may change per API level):
# CAMERA group: CAMERA
# LOCATION group: ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION
# STORAGE group: READ_MEDIA_IMAGES, READ_MEDIA_VIDEO

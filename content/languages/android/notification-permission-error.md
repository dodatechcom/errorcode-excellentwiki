---
title: "Notification Permission Error"
description: "Fix Android 13+ notification permission request errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Notifications not showing because POST_NOTIFICATIONS permission not granted

## Common Causes

- POST_NOTIFICATIONS permission not declared in manifest
- Runtime permission not requested for API 33+
- Permission request not shown before posting
- Notification shown before permission granted

## Fixes

- Add POST_NOTIFICATIONS permission to manifest
- Request runtime permission before posting
- Check permission status before creating notification
- Handle permission denial gracefully

## Code Example

```kotlin
<!-- AndroidManifest.xml (API 33+) -->
<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />

// Request permission:
val notificationPermissionLauncher = registerForActivityResult(
    RequestPermission()
) { granted ->
    if (granted) {
        showNotification()
    }
}

if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
    notificationPermissionLauncher.launch(Manifest.permission.POST_NOTIFICATIONS)
}
```

# API 33+: POST_NOTIFICATIONS permission required
# API 32-: no permission needed for notifications
# Check permission before every notification

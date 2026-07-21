---
title: "Android 14 Permission Error"
description: "Fix Android 14 runtime permission changes and new permission requirements"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Permission requests fail on Android 14 because of new requirements

## Common Causes

- Partial media permission for photo picker
- Runtime-registered receivers need EXPORTED flag
- Schedule exact alarm permission not requested
- New permission groups not properly handled

## Fixes

- Use photo picker instead of READ_MEDIA_IMAGES
- Add RECEIVER_EXPORTED or RECEIVER_NOT_EXPORTED flag
- Request USE_EXACT_ALARM permission
- Handle Android 14 permission model changes

## Code Example

```kotlin
// Android 14: Use photo picker instead of READ_MEDIA_IMAGES
val pickMedia = registerForActivityResult(PickVisualMedia()) { uri ->
    uri?.let { /* use image */ }
}
pickMedia.launch(PickVisualMediaRequest(ActivityResultContracts.PickVisualMedia.ImageOnly))

// Runtime-registered receivers must specify export flag:
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
    registerReceiver(receiver, filter, Context.RECEIVER_NOT_EXPORTED)
}
```

# Android 14 changes:
# Photo picker preferred over storage permissions
# Runtime receivers need EXPORTED flag
# Exact alarm permission: USE_EXACT_ALARM

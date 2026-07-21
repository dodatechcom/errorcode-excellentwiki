---
title: "Compose Permission Error"
description: "Fix permission handling in Jetpack Compose with Accompanist or ActivityResultContracts"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Permission request flow does not work correctly in Jetpack Compose

## Common Causes

- Permission request not launching from Compose
- Permission state not triggering recomposition
- Rationale dialog not showing before request
- Multiple permissions not handled together

## Fixes

- Use rememberLauncherForActivityResult in Compose
- Use mutableStateOf for permission status
- Check permission before requesting
- Use RequestMultiplePermissions for groups

## Code Example

```kotlin
@Composable
fun RequestCameraPermission(onGranted: () -> Unit) {
    val launcher = rememberLauncherForActivityResult(
        RequestPermission()
    ) { granted ->
        if (granted) onGranted()
    }

    Button(onClick = { launcher.launch(Manifest.permission.CAMERA) }) {
        Text("Grant Camera Permission")
    }
}

// Check permission first:
if (ContextCompat.checkSelfPermission(context, Manifest.permission.CAMERA)
    == PackageManager.PERMISSION_GRANTED) {
    // Already granted
}
```

# Use rememberLauncherForActivityResult
# Check permission status with ContextCompat
# Handle denial with shouldShowRequestPermissionRationale

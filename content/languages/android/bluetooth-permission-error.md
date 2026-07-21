---
title: "Bluetooth Permission Error"
description: "Fix Android Bluetooth permission errors for scanning and connecting devices"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Bluetooth scanning or connection fails because of missing permissions

## Common Causes

- BLUETOOTH_SCAN not declared for API 31+
- BLUETOOTH_CONNECT permission missing
- ACCESS_FINE_LOCATION required for older APIs
- Permission request not handling denial

## Fixes

- Add BLUETOOTH_SCAN, BLUETOOTH_CONNECT to manifest
- Request runtime permissions for Bluetooth
- Check API level for required permissions
- Handle permission denial with settings redirect

## Code Example

```kotlin
<!-- AndroidManifest.xml -->
<uses-permission android:name="android.permission.BLUETOOTH_SCAN"
    android:usesPermissionFlags="neverForLocation" />
<uses-permission android:name="android.permission.BLUETOOTH_CONNECT" />
<!-- For API 30 and below -->
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"
    android:maxSdkVersion="30" />

// Runtime permission request:
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
    requestPermissions(arrayOf(BLUETOOTH_SCAN, BLUETOOTH_CONNECT), REQUEST_CODE)
} else {
    requestPermissions(arrayOf(ACCESS_FINE_LOCATION), REQUEST_CODE)
}
```

# API 31+: BLUETOOTH_SCAN, BLUETOOTH_CONNECT
# API 30-: ACCESS_FINE_LOCATION for scanning
# BLUETOOTH_CONNECT for all connection operations

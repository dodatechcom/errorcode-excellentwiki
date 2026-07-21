---
title: "Android 15 Changes"
description: "Fix Android 15 (Vanilla Ice Cream) behavioral changes and deprecations"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App behavior changes or crashes when targeting Android 15

## Common Causes

- Foreground service type restrictions tightened
- Package visibility changes affecting queries
- Edge-to-edge enforced by default
- New permission requirements

## Fixes

- Review Android 15 behavioral changes
- Update targetSdkVersion to 35
- Test edge-to-edge rendering
- Update permission declarations

## Code Example

```kotlin
// Android 15 requires edge-to-edge
// Called automatically for targetSdk 35
// Or call explicitly:
enableEdgeToEdge()

// Foreground service types now mandatory
<service
    android:name=".SyncService"
    android:foregroundServiceType="dataSync"
    android:exported="false" />
```

# Review developer.android.com/about/versions/15
# Test on Android 15 emulator
# Update deprecated APIs
# Check foreground service types

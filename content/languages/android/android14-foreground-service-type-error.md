---
title: "Android 14 Foreground Service Error"
description: "Fix Android 14 foreground service type requirements and permission errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Foreground service crashes on Android 14+ because of missing service type

## Common Causes

- foregroundServiceType not declared in manifest
- FOREGROUND_SERVICE permission not added
- Wrong service type for use case
- Missing platform-specific permission

## Fixes

- Add foregroundServiceType attribute to service in manifest
- Add FOREGROUND_SERVICE permission and type-specific permission
- Use correct type: camera, location, mediaPlayback, etc.
- Check Android 14 service type requirements

## Code Example

```kotlin
<!-- AndroidManifest.xml -->
<uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_DATA_SYNC" />

<service
    android:name=".SyncService"
    android:foregroundServiceType="dataSync"
    android:exported="false" />
```

# Types: camera, connectedDevice, dataSync,
# health, location, mediaPlayback, mediaProjection,
# microphone, phoneCall, remoteMessaging,
# shortService, specialUse, systemExempted

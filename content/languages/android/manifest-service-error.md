---
title: "Service Declaration Error"
description: "Fix Android service declaration and foreground service type errors in manifest"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Service fails to start because of manifest configuration issues

## Common Causes

- Service not declared in manifest
- Missing foregroundServiceType for API 34+
- Service declared with wrong process attribute
- Exported attribute missing on bound service

## Fixes

- Declare service in manifest inside application tag
- Add foregroundServiceType attribute for foreground services
- Set exported=false for internal services only
- Use Context.startForegroundService() with notification

## Code Example

```kotlin
<!-- Manifest declaration -->
<service
    android:name=".MusicService"
    android:exported="false"
    android:foregroundServiceType="mediaPlayback" />

<!-- Required permissions for foreground service (API 34+) -->
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK" />
```

# Start foreground service
val intent = Intent(this, MusicService::class.java)
ContextCompat.startForegroundService(this, intent)

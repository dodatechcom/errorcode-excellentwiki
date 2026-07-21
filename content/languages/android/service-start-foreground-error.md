---
title: "Foreground Service Start Error"
description: "Fix Android foreground service notification errors and startForeground requirements"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Foreground service crashes because notification is not shown within time limit

## Common Causes

- startForegroundService called but startForeground not called
- Notification channel missing for API 26+
- FOREGROUND_SERVICE permission missing
- Notification does not meet foreground service requirements

## Fixes

- Call startForeground() with notification immediately in onStartCommand
- Create notification channel before starting service
- Add FOREGROUND_SERVICE permission in manifest
- Use NotificationCompat.Builder for compatible notifications

## Code Example

```kotlin
class MyService : Service() {
    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val notification = NotificationCompat.Builder(this, "channel_id")
            .setContentTitle("Service Running")
            .setContentText("Processing in background")
            .setSmallIcon(R.drawable.ic_notification)
            .build()

        startForeground(1, notification)

        // Do work...
        return START_NOT_STICKY
    }

    override fun onBind(intent: Intent?): IBinder? = null
}
```

<!-- AndroidManifest.xml (API 34+) -->
<uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_DATA_SYNC" />
<service
    android:name=".MyService"
    android:foregroundServiceType="dataSync"
    android:exported="false" />

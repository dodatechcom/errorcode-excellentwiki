---
title: "WorkManager Foreground Service Error"
description: "Fix WorkManager foreground service notification errors for long-running work"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
WorkManager foreground service fails because notification is not properly configured

## Common Causes

- setForeground not called in Worker
- Notification channel not created for API 26+
- FOREGROUND_SERVICE permission missing
- Notification does not meet foreground service requirements

## Fixes

- Call setForeground() in Worker with valid Notification
- Create notification channel before starting service
- Add FOREGROUND_SERVICE permission in manifest
- Use NotificationCompat.Builder for compatible notifications

## Code Example

```kotlin
class LongRunningWorker(
    context: Context,
    params: WorkerParameters
) : CoroutineWorker(context, params) {

    override suspend fun doWork(): Result {
        val notification = NotificationCompat.Builder(applicationContext, "channel_id")
            .setContentTitle("Processing")
            .setContentText("Uploading files...")
            .setSmallIcon(R.drawable.ic_upload)
            .setOngoing(true)
            .build()

        setForeground(ForegroundInfo(1, notification))

        // Do long work...
        return Result.success()
    }
}
```

<!-- Manifest permission (API 34+) -->
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_DATA_SYNC" />
<service
    android:name="androidx.work.impl.background.systemjob.SystemJobService"
    android:foregroundServiceType="dataSync" />

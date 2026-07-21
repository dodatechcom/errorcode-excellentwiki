---
title: "ForegroundInfo Notification Error"
description: "Fix WorkManager ForegroundInfo notification configuration for foreground work"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
WorkManager foreground service fails because ForegroundInfo notification is invalid

## Common Causes

- Notification not built before calling setForeground
- Notification channel ID does not exist
- ForegroundInfo notification missing required fields
- FOREGROUND_SERVICE permission missing

## Fixes

- Build notification before setForeground call
- Create notification channel first
- Set small icon, title, and content at minimum
- Add foreground service permission in manifest

## Code Example

```kotlin
class ForegroundWorker(
    context: Context,
    params: WorkerParameters
) : CoroutineWorker(context, params) {

    override suspend fun doWork(): Result {
        val notification = createNotification()
        setForeground(ForegroundInfo(NOTIFICATION_ID, notification))
        // Do work...
        return Result.success()
    }

    private fun createNotification(): Notification {
        createNotificationChannel()
        return NotificationCompat.Builder(applicationContext, CHANNEL_ID)
            .setContentTitle("Syncing")
            .setContentText("Syncing your data...")
            .setSmallIcon(R.drawable.ic_sync)
            .setOngoing(true)
            .build()
    }

    private fun createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val channel = NotificationChannel(
                CHANNEL_ID, "Sync", NotificationManager.IMPORTANCE_LOW
            )
            notificationManager.createNotificationChannel(channel)
        }
    }
}
```

# Small icon is required for notification
# Channel must exist before posting notification (API 26+)

---
title: "Notification Channel Error"
description: "Fix Android notification channel creation and configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Notifications not displayed because notification channel is not created or configured

## Common Causes

- Notification channel not created before posting
- Channel ID mismatch between creation and posting
- Channel importance set too low to show heads-up
- Channel cannot be modified after creation on API 26+

## Fixes

- Create notification channel in onCreate before any notification
- Use consistent channel ID string
- Set appropriate importance level
- Delete and recreate channel to change properties

## Code Example

```kotlin
// Create channel BEFORE posting notification
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
    val channel = NotificationChannel(
        "messages",
        "Messages",
        NotificationManager.IMPORTANCE_HIGH
    ).apply {
        description = "Direct messages"
        enableVibration(true)
    }
    notificationManager.createNotificationChannel(channel)
}

// Post notification with matching channel ID
val notification = NotificationCompat.Builder(context, "messages")
    .setSmallIcon(R.drawable.ic_message)
    .setContentTitle("New message")
    .setContentText("Hello!")
    .setPriority(NotificationCompat.PRIORITY_HIGH)
    .build()
```

# Channel importance:
# IMPORTANCE_HIGH: heads-up notification
# IMPORTANCE_DEFAULT: status bar only
# IMPORTANCE_LOW: no sound, status bar
# IMPORTANCE_MIN: no sound, no status bar

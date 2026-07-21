---
title: "FCM Push Notification Error"
description: "Fix Firebase Cloud Messaging push notification errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Push notifications not received or displayed because of FCM misconfiguration

## Common Causes

- FCM token not obtained or refreshed
- Notification channel not created for API 26+
- onMessageReceived not called for notification messages
- FirebaseMessagingService not registered in manifest

## Fixes

- Obtain FCM token with FirebaseMessaging.token
- Create notification channel before showing notifications
- Use data messages to ensure onMessageReceived is called
- Declare FirebaseMessagingService in manifest

## Code Example

```kotlin
class MyFirebaseService : FirebaseMessagingService() {
    override fun onNewToken(token: String) {
        // Send token to server
        sendTokenToServer(token)
    }

    override fun onMessageReceived(message: RemoteMessage) {
        // Handle data message
        message.data["title"]?.let { title ->
            showNotification(title, message.data["body"] ?: "")
        }
    }
}

// In manifest:
<service
    android:name=".MyFirebaseService"
    android:exported="false">
    <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
    </intent-filter>
</service>
```

# Create notification channel (API 26+):
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
    val channel = NotificationChannel("id", "name", IMPORTANCE_HIGH)
    notificationManager.createNotificationChannel(channel)
}

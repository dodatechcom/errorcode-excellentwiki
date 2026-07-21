---
title: "Firebase Installations Error"
description: "Fix Firebase Installations ID and FCM token registration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Firebase Installations ID or FCM token is not available or stale

## Common Causes

- Firebase Installations not initialized
- FCM token not refreshed after app update
- Token not sent to backend server
- Installation ID deleted during app reinstall

## Fixes

- Wait for Firebase installations initialization
- Listen for token refresh in onNewToken
- Send token to server on each app launch
- Store and refresh installation ID

## Code Example

```kotlin
// Get FCM token
FirebaseMessaging.getInstance().token.addOnCompleteListener { task ->
    if (task.isSuccessful) {
        val token = task.result
        sendTokenToServer(token)
    }
}

// Listen for token refresh:
class MyFirebaseService : FirebaseMessagingService() {
    override fun onNewToken(token: String) {
        sendTokenToServer(token)
    }
}

// Get installation ID:
FirebaseInstallations.getInstance().id.addOnCompleteListener { task ->
    val fid = task.result
}
```

# FCM token may change on reinstall or token refresh
# Always send token to server on app launch
# Use onNewToken to handle refreshes

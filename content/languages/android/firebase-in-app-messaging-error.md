---
title: "Firebase In-App Messaging Error"
description: "Fix Firebase In-App Messaging campaign display and trigger errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Firebase In-App Messaging campaigns do not display or trigger incorrectly

## Common Causes

- Campaign not properly configured in Firebase console
- Firebase In-App Messaging SDK not initialized
- Trigger events not being logged
- Campaign impression not being tracked

## Fixes

- Configure campaign in Firebase console with correct triggers
- Add Firebase In-App Messaging SDK dependency
- Log trigger events with FirebaseAnalytics
- Verify campaign status is active

## Code Example

```kotlin
dependencies {
    implementation 'com.google.firebase:firebase-inappmessaging-display:20.4.0'
}

// Log trigger event:
Firebase.analytics.logEvent("view_item_detail") {
    param("item_id", "12345")
}

// Campaign triggers on this event name
// in Firebase console configuration
```

# Firebase Console > In-App Messaging > Create campaign
# Set trigger event name matching your logEvent calls

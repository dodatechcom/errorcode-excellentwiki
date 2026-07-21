---
title: "Firebase Analytics Error"
description: "Fix Firebase Analytics event tracking and parameter errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Analytics events not logged correctly or missing parameters

## Common Causes

- Event name contains invalid characters
- Parameter bundle exceeds maximum size
- Custom event name too long or reserved
- Analytics collection not enabled in manifest

## Fixes

- Use only letters, numbers, and underscores in event names
- Limit parameters to 25 per event
- Avoid reserved event names from Firebase
- Ensure analytics collection is enabled

## Code Example

```kotlin
// Log custom event
val params = bundleOf(
    "item_name" to "Shoes",
    "price" to 49.99,
    "currency" to "USD"
)
Firebase.analytics.logEvent("add_to_cart", params)

// Log predefined event
Firebase.analytics.logEvent(FirebaseAnalytics.Event.LOGIN) {
    param(FirebaseAnalytics.Method.GOOGLE)
}
```

# Event names: max 40 characters
# Parameter names: max 50 characters
# Parameter values: max 100 characters
# 500 distinct event names max

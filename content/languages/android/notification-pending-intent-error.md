---
title: "Notification PendingIntent Error"
description: "Fix Android notification PendingIntent configuration and flag errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Notification tap does not open correct screen or crashes

## Common Causes

- PendingIntent FLAG_IMMUTABLE required on API 31+
- PendingIntent targets wrong activity
- Multiple notifications sharing same PendingIntent
- PendingIntent extras not being passed

## Fixes

- Add FLAG_IMMUTABLE or FLAG_MUTABLE to PendingIntent
- Set correct target component
- Use unique request codes per notification
- Bundle extras into PendingIntent

## Code Example

```kotlin
// CORRECT PendingIntent with FLAG_IMMUTABLE
val intent = Intent(context, DetailActivity::class.java).apply {
    putExtra("item_id", itemId)
    flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK
}

val pendingIntent = PendingIntent.getActivity(
    context,
    itemId.toInt(),  // Unique request code per notification
    intent,
    PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
)
```

# FLAG_IMMUTABLE: required for API 31+
# FLAG_UPDATE_CURRENT: update existing PendingIntent
# FLAG_CANCEL_CURRENT: cancel previous and create new
# Unique request code per notification

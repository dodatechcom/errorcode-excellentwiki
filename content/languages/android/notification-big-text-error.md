---
title: "Notification Big Text Error"
description: "Fix Android notification expanded style and big text display errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Notification does not expand or show big text when pulled down

## Common Causes

- BigTextStyle not applied to notification builder
- Big content title not set
- Summary text not provided for expanded view
- Style not compatible with notification priority

## Fixes

- Apply BigTextStyle to NotificationCompat.Builder
- Set bigContentTitle for expanded view
- Use setSummaryText for additional context
- Set appropriate priority for visibility

## Code Example

```kotlin
val notification = NotificationCompat.Builder(context, "messages")
    .setSmallIcon(R.drawable.ic_message)
    .setContentTitle("New message")
    .setContentText("Hello!")
    .setStyle(NotificationCompat.BigTextStyle()
        .bigText("This is the full long text that appears when the notification is expanded. It can contain much more content than the collapsed view.")
        .setBigContentTitle("Expanded Title")
        .setSummaryText("Additional context"))
    .setPriority(NotificationCompat.PRIORITY_HIGH)
    .build()
```

# BigTextStyle: expandable text
# InboxStyle: list of lines
# MessagingStyle: chat messages
# MediaStyle: media controls

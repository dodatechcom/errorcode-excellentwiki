---
title: "API Level Check Missing"
description: "Fix Android API level check errors and SDK_INT version guards"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App crashes on older devices because API level is not checked before calling newer methods

## Common Causes

- Calling API introduced after minSdk without version check
- Missing Build.VERSION.SDK_INT guard
- Using reflection to call hidden APIs
- Third-party library internally uses newer APIs

## Fixes

- Wrap newer API calls in if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.X) check
- Use @RequiresApi annotation on methods
- Provide fallback implementation for older devices
- Check library documentation for minimum API requirements

## Code Example

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
    // Android 13+ code
    val poster = notificationManager.getNotificationPoster()
} else {
    // Fallback for older devices
    val builder = NotificationCompat.Builder(this, channelId)
}
```

# Use Android Studio lint to find API issues
./gradlew lintDebug | grep "RequiresApi"
# Or annotate entire class
@RequiresApi(Build.VERSION_CODES.O)
class MyService : Service() { ... }

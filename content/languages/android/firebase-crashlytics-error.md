---
title: "Crashlytics Reporting Error"
description: "Fix Firebase Crashlytics error reporting and custom log configuration"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Crashlytics does not report crashes or custom logs are missing

## Common Causes

- Crashlytics not initialized properly
- Custom keys not set on crash reports
- Non-fatal exceptions not recorded
- Debug mode not disabled for production

## Fixes

- Verify Crashlytics is initialized on app start
- Set custom keys for context on crashes
- Use recordException() for non-fatal errors
- Disable Crashlytics for debug builds

## Code Example

```kotlin
// Record non-fatal exception
try {
    riskyOperation()
} catch (e: Exception) {
    Crashlytics.recordException(e)
}

// Set custom keys for crash context
Crashlytics.setCustomKey("user_id", userId)
Crashlytics.setCustomKey("screen", currentScreen)
Crashlytics.log("User tapped checkout button")

// Force a crash for testing:
Crashlytics.getInstance().crash()
```

# Disable for debug in build.gradle:
# firebaseCrashlytics.mappingFileUploadEnabled false
# Or in code:
# FirebaseCrashlytics.getInstance().setCrashlyticsCollectionEnabled(false)

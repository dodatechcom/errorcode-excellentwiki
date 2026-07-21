---
title: "Exception Group Handling Error"
description: "Fix Android error handling with exception groups and multi-catch patterns"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Multiple exception types not properly caught or handled in try-catch blocks

## Common Causes

- Generic catch catching too broadly
- Specific exceptions not distinguished from generic
- Nested try-catch obscuring error source
- Exception cause chain not properly logged

## Fixes

- Catch specific exceptions before generic
- Log full exception chain with cause
- Use when() for exception type matching
- Handle each exception type appropriately

## Code Example

```kotlin
try {
    riskyOperation()
} catch (e: IOException) {
    // Network/disk error
    showRetryMessage()
} catch (e: HttpException) {
    // API error
    when (e.code) {
        401 -> redirectToLogin()
        404 -> showNotFound()
        500 -> showServerError()
    }
} catch (e: CancellationException) {
    throw e  // Never catch coroutine cancellation!
} catch (e: Exception) {
    // Unexpected error
    Log.e("Error", "Unexpected error", e)
    showGenericError()
}
```

# Catch order: most specific to most generic
# Always rethrow CancellationException
# Log full stack trace with Log.e()

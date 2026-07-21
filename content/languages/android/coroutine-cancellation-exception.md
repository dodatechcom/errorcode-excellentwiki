---
title: "Coroutine Cancellation Error"
description: "Fix Kotlin coroutine CancellationException handling errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Coroutine throws CancellationException which is not properly handled

## Common Causes

- Catching CancellationException with generic catch
- Calling cancel() without checking isActive
- Using runBlocking in UI thread
- Throwing non-CancellationException in finally block

## Fixes

- Let CancellationException propagate through catch blocks
- Check coroutineContext.isActive before long operations
- Use supervisorScope for independent child failures
- Catch specific exceptions, not generic Throwable

## Code Example

```kotlin
// WRONG: swallowing CancellationException
try {
    delay(1000)
} catch (e: Exception) {
    Log.e("Error", e.message)  // Catches Cancellation too!
}

// CORRECT: rethrow CancellationException
try {
    delay(1000)
} catch (e: CancellationException) {
    throw e  // Must rethrow!
} catch (e: Exception) {
    Log.e("Error", e.message)
}
```

# CancellationException is special in coroutines
# Always rethrow it in catch blocks
# Use isActive check for cooperative cancellation

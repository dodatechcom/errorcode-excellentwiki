---
title: "Coroutine Timeout Error"
description: "Fix Kotlin coroutine timeout and cancellation pattern errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Coroutine timeout not cancelling operation or cancelling wrong scope

## Common Causes

- withTimeout not properly cancelling underlying operation
- Timeout exception not handled gracefully
- Cascading cancellation affecting other coroutines
- Timeout on wrong dispatcher

## Fixes

- Use withTimeoutOrNull for non-crashing timeout
- Handle TimeoutCancellationException in catch
- Use supervisorScope for independent timeouts
- Ensure IO operations support cancellation

## Code Example

```kotlin
// Crashes on timeout:
try {
    val result = withTimeout(5000) {
        apiCall()
    }
} catch (e: TimeoutCancellationException) {
    // Handle timeout
}

// Non-crashing timeout:
val result = withTimeoutOrNull(5000) {
    apiCall()
}
if (result == null) {
    // Timeout occurred
}

// Independent timeouts:
supervisorScope {
    launch { withTimeout(3000) { task1() } }
    launch { withTimeout(5000) { task2() } }
}
```

# withTimeout: throws TimeoutCancellationException
# withTimeoutOrNull: returns null on timeout
# Ensure underlying operations check for cancellation

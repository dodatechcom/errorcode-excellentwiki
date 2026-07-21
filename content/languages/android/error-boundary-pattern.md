---
title: "Error Boundary Pattern Error"
description: "Implement error boundary pattern for composable function error isolation"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Error in one Compose component crashes entire screen

## Common Causes

- No error boundary wrapping composable tree
- Throwable crashing entire UI
- Error not properly caught in composition
- Recovery not offered to user

## Fixes

- Wrap composable tree with error boundary
- Use try-catch or setErrorHandler for composition errors
- Show fallback UI for crashed components
- Allow user to retry failed operations

## Code Example

```kotlin
@Composable
fun ErrorBoundary(
    fallback: @Composable (Throwable) -> Unit,
    content: @Composable () -> Unit
) {
    var error by remember { mutableStateOf<Throwable?>(null) }
    CompositionLocalProvider(
        LocalErrorHandler provides { error = it }
    ) {
        if (error != null) {
            fallback(error!!)
        } else {
            content()
        }
    }
}

// Usage:
ErrorBoundary(
    fallback = { e -> Text("Error: ${e.message}") }
) {
    RiskyComposable()
}

// Or with try-catch in LaunchedEffect:
LaunchedEffect(Unit) {
    try {
        fetchData()
    } catch (e: Exception) {
        _error.value = e
    }
}
```

# Error boundary isolates crashes to subtree
# Use for non-critical composable sections
# Always provide retry mechanism

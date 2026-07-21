---
title: "Compose Side Effect Error"
description: "Fix Jetpack Compose side effect and LaunchedEffect errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LaunchedEffect or sideEffect produces unexpected behavior or memory leaks

## Common Causes

- LaunchedEffect key changes causing infinite recomposition
- SideEffect running on every recomposition unnecessarily
- DisposableEffect missing onDispose cleanup
- rememberCoroutineScope not used for event-driven work

## Fixes

- Use correct key parameter for LaunchedEffect
- Use SideEffect for non-Compose side effects
- Always implement onDispose in DisposableEffect
- Use rememberCoroutineScope for click handlers

## Code Example

```kotlin
// LaunchedEffect with key - runs when key changes
LaunchedEffect(userId) {
    viewModel.loadUser(userId)
}

// SideEffect - runs after every successful recomposition
SideEffect {
    analytics.logScreen("Home")
}

// DisposableEffect - cleanup on dispose
DisposableEffect(Unit) {
    val listener = setupListener()
    onDispose {
        listener.cleanup()
    }
}

// Remember coroutine scope for events
val scope = rememberCoroutineScope()
Button(onClick = {
    scope.launch { apiCall() }
}) { ... }
```

# LaunchedEffect: coroutine tied to composition
# SideEffect: non-Compose side effect
# DisposableEffect: setup + cleanup
# rememberCoroutineScope: event handlers

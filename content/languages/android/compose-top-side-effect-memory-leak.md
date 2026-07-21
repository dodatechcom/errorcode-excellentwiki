---
title: "Side Effect Memory Leak"
description: "Fix memory leaks from side effects holding references in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Side effects not properly cancelling leading to memory leaks or stale data

## Common Causes

- LaunchedEffect coroutine running after composable leaves composition
- DisposableEffect not disposing resources
- produceState holding stale reference
- SideEffect running on every recomposition

## Fixes

- Use DisposableEffect for resources needing cleanup
- Return cleanup function from DisposableEffect
- Ensure LaunchedEffect keys are correct
- Use View-specific lifecycle in side effects

## Code Example

```kotlin
DisposableEffect(Unit) {
    val listener = registerListener()
    onDispose {
        listener.unregister()  // Cleanup
    }
}
```

# DisposableEffect: cleanup when leaving composition# Return onDispose lambda# Unit key: run once only# Ensure all side effects have cleanup

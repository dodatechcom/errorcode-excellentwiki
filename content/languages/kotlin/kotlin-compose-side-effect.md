---
title: "[Solution] Kotlin Compose Side Effect — LaunchedEffect/DisposableEffect Key Mismatch"
description: "Fix Compose side effect errors with key mismatch. Learn correct LaunchedEffect, DisposableEffect, and rememberCoroutineScope usage."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1020
---

## What This Error Means

Side effect key mismatch causes effects to restart unexpectedly or fail to restart when they should. Each effect (LaunchedEffect, DisposableEffect) must have correctly specified keys to control its lifecycle.

## Common Causes

- Missing key in `LaunchedEffect` causing effect to run only once
- Wrong key value causing effect to restart on every recomposition
- `DisposableEffect` not calling `onDispose`
- Using `rememberCoroutineScope` instead of `LaunchedEffect` for fire-and-forget

```kotlin
// WRONG: No key — effect runs once, never restarts
LaunchedEffect(Unit) {
    observeLocationChanges()  // Never restarts on userId change
}
```

## How to Fix

**1. Use correct keys for LaunchedEffect**

```kotlin
// CORRECT: Restart when userId changes
LaunchedEffect(userId) {
    loadUser(userId)  // Restarts when userId changes
}
```

**2. Always call onDispose in DisposableEffect**

```kotlin
DisposableEffect(userId) {
    val listener = registerListener(userId)
    onDispose {
        listener.unregister()
    }
}
```

**3. Use rememberCoroutineScope for non-lifecycle-bound work**

```kotlin
@Composable
fun ChatScreen() {
    val scope = rememberCoroutineScope()
    Button(onClick = {
        scope.launch { sendMessage() }
    }) { Text("Send") }
}
```

**4. Use SideEffect for non-suspending side effects**

```kotlin
SideEffect {
    analytics.log("composable displayed")
}
```

## Examples

```kotlin
// Example 1: Multiple keys
LaunchedEffect(userId, sessionId) {
    trackSession(userId, sessionId)
}

// Example 2: DisposableEffect with cleanup
@Composable
fun LifecycleObserver() {
    val lifecycleOwner = LocalLifecycleOwner.current
    DisposableEffect(lifecycleOwner) {
        val observer = LifecycleEventObserver { _, event -> handleEvent(event) }
        lifecycleOwner.lifecycle.addObserver(observer)
        onDispose { lifecycleOwner.lifecycle.removeObserver(observer) }
    }
}

// Example 3: produceState for async data loading
@Composable
fun LoadData(url: String): State<Result<Data>> {
    return produceState<Result<Data>>(initialValue = Result.Loading, url) {
        value = try {
            Result.Success(fetchData(url))
        } catch (e: Exception) {
            Result.Failure(e)
        }
    }
}
```

## Related Errors

- [Compose recomposition](kotlin-compose-recomposition) — excessive recomposition
- [Compose navigation](kotlin-compose-navigation) — navigation issues
- [Compose modifier error](kotlin-compose-modifier-error) — modifier issues

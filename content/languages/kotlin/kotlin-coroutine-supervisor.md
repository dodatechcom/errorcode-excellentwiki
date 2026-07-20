---
title: "[Solution] Kotlin SupervisorJob vs Job — Child Cancellation Propagation"
description: "Fix Kotlin coroutine supervisor job vs job confusion. Learn how child cancellation propagates and when to use SupervisorJob."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1009
---

## What This Error Means

Using a regular `Job` instead of `SupervisorJob` causes one child coroutine failure to cancel all sibling coroutines. This is a common source of unexpected cascade cancellations in structured concurrency.

## Common Causes

- Using default `Job()` in a scope where children should be independent
- Not understanding that `Job` cancels children on failure
- Missing `SupervisorJob` in custom CoroutineScope
- ViewModel scope accidentally sharing a regular Job

```kotlin
// All children cancelled when first one fails
val scope = CoroutineScope(Job() + Dispatchers.Default)
scope.launch { throw Exception("child 1 failed") }
scope.launch { println("child 2 — cancelled too!") }
```

## How to Fix

**1. Use SupervisorJob for independent children**

```kotlin
// Children survive independently
val scope = CoroutineScope(SupervisorJob() + Dispatchers.Default)
scope.launch { throw Exception("child 1 fails") }
scope.launch { delay(100); println("child 2 still runs!") }
```

**2. Use supervisorScope for structured concurrency**

```kotlin
supervisorScope {
    launch { throw Exception("fails") }
    launch { println("survives") }  // Not cancelled
}
```

**3. Use custom exception handler with SupervisorJob**

```kotlin
val handler = CoroutineExceptionHandler { _, exception ->
    println("Caught: ${exception.message}")
}
val scope = CoroutineScope(SupervisorJob() + handler)
```

**4. Add exception handler to individual children**

```kotlin
val scope = CoroutineScope(SupervisorJob())
scope.launch {
    val child = launch(CoroutineExceptionHandler { _, e -> log(e) }) {
        riskyWork()
    }
}
```

## Examples

```kotlin
// Example 1: SupervisorJob in ViewModel
class MyViewModel : ViewModel() {
    init {
        viewModelScope.launch { loadUser() }    // Independent
        viewModelScope.launch { loadPosts() }   // Independent
    }
}

// Example 2: supervisorScope with structured concurrency
suspend fun loadDashboard() = supervisorScope {
    val user = async { fetchUser() }
    val posts = async { fetchPosts() }
    val notifications = async { fetchNotifications() }
    // One failure doesn't cancel the others
}

// Example 3: Parent cancellation still propagates down
val parent = CoroutineScope(SupervisorJob())
val child = parent.launch { delay(10000) }
parent.cancel()  // Child IS cancelled by parent
```

## Related Errors

- [CancellationException](cancellationexception-kotlin) — coroutine cancelled
- [CoroutineScope cancelled error](coroutine-scope-error) — scope cancelled
- [kotlinx.coroutines error](kotlinx-coroutines-error) — coroutine error

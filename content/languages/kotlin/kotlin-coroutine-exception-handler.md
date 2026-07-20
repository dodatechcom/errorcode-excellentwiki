---
title: "[Solution] Kotlin CoroutineExceptionHandler Not Triggered"
description: "Fix Kotlin CoroutineExceptionHandler not being called. Learn correct placement and dispatcher requirements for exception handlers."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1010
---

## What This Error Means

A CoroutineExceptionHandler not being triggered means the handler is either incorrectly placed, not installed on the right coroutine context, or the exception is being caught elsewhere (e.g., `runBlocking`).

## Common Causes

- CoroutineExceptionHandler installed on child, not the scope
- Using with `runBlocking` which catches exceptions itself
- Exception handler on a dispatcher that doesn't propagate exceptions
- CoroutineExceptionHandler not catching CancellationException (by design)

```kotlin
// WRONG: Handler on child — never triggered
val scope = CoroutineScope(Job())
scope.launch {
    launch(CoroutineExceptionHandler { _, e -> println(e) }) {
        throw Exception("boom")  // Handler on sibling, not parent
    }
}
```

## How to Fix

**1. Install handler on the scope, not individual launches**

```kotlin
val handler = CoroutineExceptionHandler { _, exception ->
    println("Caught: ${exception.message}")
}
val scope = CoroutineScope(SupervisorJob() + handler)
scope.launch { throw Exception("caught") }  // Handler triggered
```

**2. Use supervisorScope to prevent scope cancellation**

```kotlin
val handler = CoroutineExceptionHandler { _, e -> log(e) }
val scope = CoroutineScope(SupervisorJob() + handler)
scope.launch {
    supervisorScope {
        launch { throw Exception("caught by handler") }
    }
}
```

**3. Don't rely on CoroutineExceptionHandler inside runBlocking**

```kotlin
// WRONG: runBlocking catches internally
runBlocking {
    launch(CoroutineExceptionHandler { _, e -> println(e) }) {
        throw Exception("runBlocking handles this")
    }
}

// CORRECT: Use GlobalScope or custom scope
GlobalScope.launch(handler + Dispatchers.Default) {
    throw Exception("caught by handler")
}
```

**4. Use try-catch for expected exceptions**

```kotlin
scope.launch {
    try {
        riskyOperation()
    } catch (e: ExpectedException) {
        handleError(e)  // Caught locally
    }
}
```

## Examples

```kotlin
// Example 1: Full handler setup
val exceptionHandler = CoroutineExceptionHandler { coroutineContext, exception ->
    val job = coroutineContext[Job]
    println("Job $job failed: ${exception.message}")
}
val scope = CoroutineScope(SupervisorJob() + Dispatchers.Default + exceptionHandler)

// Example 2: Handler with logging
val handler = CoroutineExceptionHandler { ctx, e ->
    val name = ctx[CoroutineName]?.name ?: "unnamed"
    Logger.error("Coroutine $name failed", e)
}

// Example 3: Nested coroutine exception propagation
val scope = CoroutineScope(SupervisorJob() + handler)
scope.launch {
    val inner = async { throw Exception("inner fails") }
    // async exception re-thrown on await()
    try { inner.await() } catch (e: Exception) { handleLocally(e) }
}
```

## Related Errors

- [CancellationException](cancellationexception-kotlin) — coroutine cancelled
- [kotlinx.coroutines error](kotlinx-coroutines-error) — coroutine error
- [Coroutine dispatcher error](kotlin-coroutine-dispatchers) — dispatcher issue

---
title: "[Solution] Kotlin Flow Exception — Flow Error Fix"
description: "Fix Kotlin Flow exception propagation errors. Handle flow exceptions with catch operator, use runCatching, and manage terminal operators."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Flow Exception — Flow Error Fix

A Flow exception occurs when an exception is thrown during flow emission or collection. Kotlin's Flow uses the `catch` operator to handle upstream exceptions and `onCompletion` for terminal events.

## Description

Kotlin Flows are cold asynchronous streams. Exceptions can occur during emission (in `flow {}` block) or collection (in `collect {}` block). The `catch` operator only catches upstream exceptions, not downstream ones.

Common scenarios:

- **Exception in emission** — error thrown in `flow { }` block.
- **Exception in collection** — error thrown in `collect { }` block.
- **Missing catch operator** — unhandled exception propagates.
- **catch placement wrong** — catch only works on upstream operators.

## Common Causes

```kotlin
// Cause 1: Exception in emission
fun fetchData(): Flow<String> = flow {
    emit("data")
    throw RuntimeException("Emission failed")  // Exception in flow
}

// Cause 2: Exception in collection
val flow = flowOf(1, 2, 3)
flow.collect { value ->
    if (value == 2) throw RuntimeException("Collection failed")
}

// Cause 3: Missing catch operator
fetchData()
    .map { it.uppercase() }
    .collect { println(it) }  // No catch, exception propagates

// Cause 4: catch after terminal operator
fetchData()
    .catch { e -> println("Caught: ${e.message}") }  // Wrong placement
    .collect { println(it) }
```

## Solutions

### Fix 1: Use catch operator for upstream exceptions

```kotlin
// Wrong — no error handling
fetchData()
    .collect { println(it) }

// Correct — catch upstream exceptions
fetchData()
    .catch { e -> println("Error: ${e.message}") }
    .collect { println(it) }
```

### Fix 2: Place catch before terminal operators

```kotlin
// Wrong — catch after collect
fetchData()
    .collect { println(it) }
    .catch { e -> println("Error") }

// Correct — catch before collect
fetchData()
    .catch { e -> println("Error: ${e.message}") }
    .collect { println(it) }
```

### Fix 3: Handle collection exceptions separately

```kotlin
// Wrong — catch doesn't cover collection exceptions
fetchData()
    .catch { e -> println("Upstream error: ${e.message}") }
    .collect { value ->
        process(value)  // Exception here not caught by catch
    }

// Correct — use try-catch in collect
fetchData()
    .catch { e -> println("Upstream error: ${e.message}") }
    .collect { value ->
        try {
            process(value)
        } catch (e: Exception) {
            println("Collection error: ${e.message}")
        }
    }
```

### Fix 4: Use onCompletion for cleanup

```kotlin
// Wrong — cleanup not guaranteed
fetchData()
    .collect { println(it) }

// Correct — onCompletion runs on both success and failure
fetchData()
    .onCompletion { cause ->
        if (cause != null) println("Flow failed: ${cause.message}")
        else println("Flow completed successfully")
    }
    .catch { e -> println("Error: ${e.message}") }
    .collect { println(it) }
```

## Examples

```kotlin
import kotlinx.coroutines.flow.*

fun fetchNumbers(): Flow<Int> = flow {
    for (i in 1..5) {
        if (i == 3) throw RuntimeException("Error at $i")
        emit(i)
    }
}

fun main() = runBlocking {
    fetchNumbers()
        .onCompletion { cause ->
            println("Flow ${if (cause == null) "completed" else "failed: ${cause.message}"}")
        }
        .catch { e -> println("Caught: ${e.message}") }
        .collect { println("Received: $it") }
}
// Received: 1
// Received: 2
// Caught: Error at 3
// Flow failed: Error at 3
```

## Related Errors

- [CancellationException]({{< relref "/languages/kotlin/cancellation-exception" >}}) — flow cancelled.
- [IOException]({{< relref "/languages/kotlin/io-exception" >}}) — I/O error in flow.
- [RuntimeException]({{< relref "/languages/kotlin/runtime-exception" >}}) — general runtime error.

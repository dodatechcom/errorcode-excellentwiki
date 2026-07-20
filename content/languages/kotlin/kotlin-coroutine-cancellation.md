---
title: "[Solution] Kotlin JobCancellationException: Job was cancelled"
description: "Fix Kotlin kotlinx.coroutines.JobCancellationException errors. Learn how coroutine cancellation propagates and how to handle CancellationException properly."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# JobCancellationException: Job was cancelled

A `JobCancellationException` is thrown when a coroutine is cancelled and code attempts to perform a suspending operation without checking for cancellation.

## Error Message

```
kotlinx.coroutines.JobCancellationException: Job was cancelled
```

## Description

Kotlin coroutines use cooperative cancellation. When a `Job` is cancelled, any subsequent call to a suspending function (like `delay`, `yield`, or `withContext`) will throw a `JobCancellationException`. This exception is a subclass of `CancellationException` and signals that the coroutine's work should stop.

If you catch and swallow this exception, the coroutine framework will not propagate the cancellation correctly, leading to resource leaks and zombie coroutines.

## Common Causes

- Catching `Exception` broadly and not re-throwing `CancellationException`
- Long-running loops that do not check `isActive`
- Using `runBlocking` inside a coroutine scope that gets cancelled
- Parent scope cancelled before child coroutine finishes
- Network or I/O calls inside a cancelled scope

## Solutions

### Solution 1: Re-throw CancellationException

Always let `CancellationException` propagate through catch blocks so the coroutine framework handles it correctly.

```kotlin
import kotlinx.coroutines.*

suspend fun fetchData(): String {
    return withContext(Dispatchers.IO) {
        try {
            val response = makeNetworkCall()
            response.body?.string() ?: ""
        } catch (e: CancellationException) {
            throw e // Re-throw so cancellation propagates
        } catch (e: Exception) {
            println("Network error: ${e.message}")
            ""
        }
    }
}

fun main() = runBlocking {
    val job = launch {
        val result = fetchData()
        println("Result: $result")
    }

    delay(100)
    job.cancelAndJoin()
    println("Coroutine was cancelled gracefully")
}
```

### Solution 2: Check isActive in long-running loops

When performing CPU-bound work, regularly check whether the coroutine is still active before continuing.

```kotlin
import kotlinx.coroutines.*

fun processItems(items: List<Int>) = runBlocking {
    val job = launch(Dispatchers.Default) {
        var index = 0
        while (isActive && index < items.size) {
            println("Processing item ${items[index]}")
            index++
        }
        println("Loop finished or cancelled at index $index")
    }

    delay(50)
    job.cancelAndJoin()
}
```

### Solution 3: Use SupervisorJob to isolate cancellations

Use a `SupervisorJob` so that the cancellation of one child coroutine does not cancel its siblings.

```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    val supervisor = SupervisorJob()
    val scope = CoroutineScope(supervisor + Dispatchers.Default)

    val job1 = scope.launch {
        delay(100)
        throw RuntimeException("Child 1 failed")
    }

    val job2 = scope.launch {
        repeat(10) { i ->
            println("Child 2 working: $i")
            delay(50)
        }
        println("Child 2 completed successfully")
    }

    job1.join()
    job2.join()
    supervisor.cancel()
}
```

## Prevention Tips

- Always re-throw `CancellationException` in catch blocks
- Use `isActive` in long-running loops to check for cancellation
- Prefer `SupervisorJob` when child coroutines should be independent
- Use structured concurrency instead of launching coroutines without a parent scope
- Use `withTimeout` instead of manual cancellation for time limits

## Related Errors

- [CancellationException]({{< relref "/languages/kotlin/cancellation-exception" >}}) — general coroutine cancellation.
- [TimeoutCancellationException]({{< relref "/languages/kotlin/timeout-exception" >}}) — timeout caused cancellation.
- [IllegalStateException]({{< relref "/languages/kotlin/illegal-state" >}}) — invalid state transition.

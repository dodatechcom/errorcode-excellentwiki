---
title: "[Solution] Kotlin Coroutine Scope Leak — Uncaught Cancellation"
description: "Fix Kotlin coroutine scope leaks. Learn why scopes leak and how to properly manage CoroutineScope lifecycle."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1008
---

## What This Error Means

A coroutine scope leak occurs when a CoroutineScope outlives its intended lifecycle, causing coroutines to continue running and consuming resources. This often manifests as uncaught cancellation exceptions or zombie coroutines.

## Common Causes

- Creating a CoroutineScope without cancelling it on teardown
- Storing scope reference in a class that outlives the scope
- Using `GlobalScope` instead of structured concurrency
- Not cancelling the scope in `onDestroy`/`onCleared`

```kotlin
// Leak: Scope never cancelled
class MyService {
    val scope = CoroutineScope(Dispatchers.Default)

    fun start() {
        scope.launch { while (true) { delay(1000) } }
    }
    // No cancel — coroutines run forever
}
```

## How to Fix

**1. Cancel scope in lifecycle methods**

```kotlin
class MyViewModel : ViewModel() {
    private val scope = CoroutineScope(SupervisorJob() + Dispatchers.IO)

    fun start() {
        scope.launch { fetchData() }
    }

    override fun onCleared() {
        super.onCleared()
        scope.cancel()
    }
}
```

**2. Use viewModelScope / lifecycleScope instead**

```kotlin
class MyViewModel : ViewModel() {
    fun loadData() {
        viewModelScope.launch {
            val data = repository.fetch()
        }
    }
    // Automatically cancelled when ViewModel is cleared
}
```

**3. Use structured concurrency**

```kotlin
class MyService : CoroutineScope {
    private val job = SupervisorJob()
    override val coroutineContext = job + Dispatchers.Default

    fun start() { launch { work() } }
    fun stop() { job.cancel() }
}
```

**4. Track scope with a Job handle**

```kotlin
var currentJob: Job? = null

fun startWork() {
    currentJob?.cancel()
    currentJob = scope.launch { longRunningTask() }
}

fun stopWork() {
    currentJob?.cancel()
    currentJob = null
}
```

## Examples

```kotlin
// Example 1: Lifecycle-aware scope
class MyActivity : ComponentActivity() {
    private val scope = lifecycleScope

    override fun onCreate(savedInstanceState: Bundle?) {
        scope.launch { loadData() }
    }
}

// Example 2: Custom scope with SupervisoryJob
val appScope = CoroutineScope(SupervisorJob() + Dispatchers.Default)

// Example 3: Scope monitoring
fun CoroutineScope.launchMonitored(name: String, block: suspend CoroutineScope.() -> Unit): Job {
    return launch(CoroutineName(name)) {
        try {
            block()
        } catch (e: CancellationException) {
            println("Coroutine $name cancelled: ${e.message}")
            throw e
        }
    }
}
```

## Related Errors

- [CancellationException](cancellationexception-kotlin) — coroutine cancelled
- [CoroutineScope cancelled error](coroutine-scope-error) — scope cancelled
- [OutOfMemoryError](outofmemory-kotlin) — heap memory exhausted

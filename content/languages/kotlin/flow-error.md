---
title: "[Solution] Kotlin Flow Collection Error Fix"
description: "Fix Kotlin Flow collection errors. Learn why Flow operations fail and how to handle Flow properly."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A Flow collection error occurs when collecting or transforming Flow values fails. This can happen due to unhandled exceptions, wrong dispatcher, or improper Flow configuration.

## Common Causes

- Exception in flow builder
- Missing catch operator
- Wrong collector context
- Cold flow not collected

## How to Fix

```kotlin
// WRONG: Not handling exceptions
flow {
    emit(fetchData())
}.collect { data ->
    // May throw
}

// CORRECT: Handle exceptions
flow {
    emit(fetchData())
}.catch { e ->
    println("Error: ${e.message}")
}.collect { data ->
    println(data)
}
```

```kotlin
// WRONG: Cold flow not collected
fun fetchData(): Flow<Data> = flow {
    emit(networkCall())  // Never executed without collector
}

// CORRECT: Always collect cold flows
fetchData().collect { data ->
    println(data)
}
```

```swift
// WRONG: Wrong dispatcher
viewModelScope.launch {
    flow.collect { data ->
        // May block main thread
    }
}

// CORRECT: Use appropriate dispatcher
viewModelScope.launch {
    flow.flowOn(Dispatchers.IO).collect { data ->
        _state.value = data
    }
}
```

## Examples

```kotlin
// Example 1: Basic Flow
fun numbers(): Flow<Int> = flow {
    for (i in 1..5) {
        delay(100)
        emit(i)
    }
}

numbers().collect { println(it) }

// Example 2: Flow operators
numbers()
    .map { it * 2 }
    .filter { it > 4 }
    .catch { e -> println("Error: $e") }
    .collect { println(it) }

// Example 3: StateFlow
val _state = MutableStateFlow<List<User>>(emptyList())
val state: StateFlow<List<User>> = _state.asStateFlow()
```

## Related Errors

- [kotlinx.coroutines error](kotlinx-coroutines-error) — coroutine error
- [Channel send/receive error](channel-error) — Channel error
- [CoroutineScope cancelled error](coroutine-scope-error) — scope cancelled

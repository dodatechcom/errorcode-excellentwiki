---
title: "Concurrent Collection Error"
description: "Fix Kotlin concurrent collection and thread-safe data structure errors in coroutines"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Shared mutable collections cause ConcurrentModificationException in coroutines

## Common Causes

- MutableList accessed from multiple coroutines
- HashMap not synchronized between coroutines
- ConcurrentModificationException during iteration
- State not properly shared between collectors

## Fixes

- Use thread-safe collections: CopyOnWriteArrayList
- Protect access with Mutex or synchronized
- Use Channel for inter-coroutine communication
- Use StateFlow for thread-safe state sharing

## Code Example

```kotlin
// WRONG: not thread-safe
val items = mutableListOf<Item>()

// CORRECT: thread-safe options:
val items = CopyOnWriteArrayList<Item>()

// Or with Mutex:
val mutex = Mutex()
val items = mutableListOf<Item>()

suspend fun addItem(item: Item) = mutex.withLock {
    items.add(item)
}

// Or use StateFlow:
private val _items = MutableStateFlow<List<Item>>(emptyList())
val items: StateFlow<List<Item>> = _items.asStateFlow()

suspend fun addItem(item: Item) {
    _items.value = _items.value + item
}
```

# CopyOnWriteArrayList: read-heavy collections
# Mutex: when you need synchronized access
# StateFlow: thread-safe reactive state
# Channel: inter-coroutine communication

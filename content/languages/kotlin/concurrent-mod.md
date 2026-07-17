---
title: "[Solution] Kotlin ConcurrentModificationException — Concurrent Access Fix"
description: "Fix Kotlin ConcurrentModificationException when collections are modified during iteration. Learn thread-safe collection patterns."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# ConcurrentModificationException — Concurrent Collection Modification

A `ConcurrentModificationException` occurs when a collection is modified while being iterated or accessed from multiple threads.

## Description

Kotlin collections are not thread-safe by default. Modifying a collection during iteration or from multiple threads without synchronization causes this exception.

Common causes:

- **Modification during iteration** — adding/removing while looping
- **Multi-threaded access** — concurrent modification from different threads
- **Shared mutable state** — collections shared across coroutines
- **Missing synchronization** — no lock on shared collection

## Common Causes

```kotlin
// Cause 1: Modification during iteration
val list = mutableListOf(1, 2, 3)
for (item in list) {
    list.remove(item)  // ConcurrentModificationException
}

// Cause 2: Multi-threaded access
val list = mutableListOf<Int>()
thread {
    repeat(1000) { list.add(it) }
}
thread {
    repeat(1000) { list.removeAt(0) }
}

// Cause 3: Shared mutable state
class Cache {
    val data = mutableMapOf<String, Any>()
}
// Multiple coroutines accessing data

// Cause 4: Iterator invalidation
val map = mutableMapOf("a" to 1, "b" to 2)
for ((key, value) in map) {
    map.remove(key)  // ConcurrentModificationException
}
```

## How to Fix

### Fix 1: Copy before iteration

```kotlin
// Wrong
val list = mutableListOf(1, 2, 3)
for (item in list) {
    list.remove(item)  // Exception
}

// Correct
val list = mutableListOf(1, 2, 3)
val copy = list.toList()
for (item in copy) {
    list.remove(item)
}
```

### Fix 2: Use concurrent collections

```kotlin
// Wrong
val list = mutableListOf<Int>()

// Correct
val list = ConcurrentLinkedQueue<Int>()
// Or use synchronized list
val list = Collections.synchronizedList(mutableListOf<Int>())
```

### Fix 3: Use removeIf

```kotlin
// Wrong
val list = mutableListOf(1, 2, 3, 4, 5)
for (item in list) {
    if (item % 2 == 0) list.remove(item)  // Exception
}

// Correct
val list = mutableListOf(1, 2, 3, 4, 5)
list.removeIf { it % 2 == 0 }
```

### Fix 4: Use locks for synchronization

```kotlin
// Wrong
val cache = mutableMapOf<String, Any>()

// Correct
val lock = ReentrantLock()
val cache = mutableMapOf<String, Any>()

fun update(key: String, value: Any) {
    lock.lock()
    try {
        cache[key] = value
    } finally {
        lock.unlock()
    }
}
```

## Examples

```kotlin
// Example 1: Thread-safe map
class ThreadSafeCache<K, V> {
    private val lock = ReentrantReadWriteLock()
    private val cache = mutableMapOf<K, V>()
    
    fun get(key: K): V? {
        lock.readLock().lock()
        try {
            return cache[key]
        } finally {
            lock.readLock().unlock()
        }
    }
    
    fun put(key: K, value: V) {
        lock.writeLock().lock()
        try {
            cache[key] = value
        } finally {
            lock.writeLock().unlock()
        }
    }
}

// Example 2: Coroutine-safe collection
class CoroutineCache<K, V> {
    private val cache = mutableMapOf<K, V>()
    
    suspend fun get(key: K): V? = withContext(Dispatchers.Default) {
        cache[key]
    }
    
    suspend fun put(key: K, value: V) = withContext(Dispatchers.Default) {
        cache[key] = value
    }
}
```

## Related Errors

- [IllegalStateException]({{< relref "/languages/kotlin/illegal-state" >}}) — invalid object state
- [CancellationException]({{< relref "/languages/kotlin/cancellation-exception" >}}) — coroutine cancellation
- [StackOverflowError]({{< relref "/languages/kotlin/stack-overflow" >}}) — infinite recursion

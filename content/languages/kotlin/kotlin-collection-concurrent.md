---
title: "[Solution] Kotlin ConcurrentModificationException in Collection Iteration"
description: "Fix Kotlin ConcurrentModificationException. Learn fail-fast iterator behavior and thread-safe collection strategies."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1003
---

## What This Error Means

ConcurrentModificationException is thrown when a collection is structurally modified during iteration (except through the iterator's own `remove` method). Kotlin collections inherit Java's fail-fast iterator behavior.

## Common Causes

- Adding or removing elements inside a `for` loop
- One thread iterating while another modifies the collection
- Calling `addAll`/`removeAll` during active iteration
- Using index-based access in a `forEach` while removing elements

```kotlin
val map = mutableMapOf("a" to 1, "b" to 2)
for ((k, v) in map) {
    map.remove(k)  // ConcurrentModificationException
}
```

## How to Fix

**1. Use iterator.remove() for conditional removal**

```kotlin
val list = mutableListOf(1, 2, 3, 4)
val iter = list.iterator()
while (iter.hasNext()) {
    if (iter.next() % 2 == 0) iter.remove()
}
```

**2. Use removeIf or removeAll**

```kotlin
val list = mutableListOf(1, 2, 3, 4, 5)
list.removeIf { it % 2 == 0 }
```

**3. Use concurrent collections for multi-threaded access**

```kotlin
import java.util.concurrent.ConcurrentHashMap
import java.util.concurrent.CopyOnWriteArrayList

val map = ConcurrentHashMap<String, Int>()
val list = CopyOnWriteArrayList<Int>()
```

**4. Build a new collection instead of mutating**

```kotlin
val original = listOf(1, 2, 3, 4, 5)
val filtered = original.filter { it > 2 }  // New list
```

**5. Snapshot before iteration**

```kotlin
val list = mutableListOf(1, 2, 3)
for (item in list.toList()) {  // Iterate over snapshot
    if (item == 2) list.remove(item)
}
```

## Examples

```kotlin
// Example 1: Safe map iteration
val map = mutableMapOf("a" to 1, "b" to 2, "c" to 3)
val toRemove = map.filter { it.value < 2 }.keys
toRemove.forEach { map.remove(it) }

// Example 2: Thread-safe iteration with synchronized block
val list = mutableListOf<Int>()
Collections.synchronizedList(list).also { syncList ->
    synchronized(syncList) {
        syncList.forEach { println(it) }
    }
}

// Example 3: Coroutine-safe collection with mutex
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock

val mutex = Mutex()
val sharedList = mutableListOf<Int>()

suspend fun safeAdd(item: Int) = mutex.withLock { sharedList.add(item) }
suspend fun safeIterate(): List<Int> = mutex.withLock { sharedList.toList() }
```

## Related Errors

- [UnsupportedOperationException](unsupportedoperationexception) — operation not supported
- [CancellationException](cancellationexception-kotlin) — coroutine cancelled
- [Channel error](kotlin-channel-error) — channel communication error

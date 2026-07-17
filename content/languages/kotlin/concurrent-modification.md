---
title: "[Solution] Kotlin ConcurrentModificationException — Collection Iteration Fix"
description: "Fix Kotlin ConcurrentModificationException when modifying a collection while iterating. Use iterators, concurrent collections, or copy-on-write patterns."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# ConcurrentModificationException — Collection Iteration Fix

A `ConcurrentModificationException` is thrown when a collection is structurally modified while being iterated. This detects concurrent access that could cause unpredictable behavior.

## Description

Kotlin's standard collections use fail-fast iterators. If a collection is modified (add/remove elements) while an iterator is active, the iterator detects the modification and throws `ConcurrentModificationException`. This can happen in single-threaded code too.

Common scenarios:

- **Removing elements during for-each loop** — modifying the collection directly.
- **Multi-threaded collection access** — threads reading/writing simultaneously.
- **Modifying collection in callback** — callback triggered during iteration.
- **Adding elements during iteration** — `list.add()` inside a for loop.

## Common Causes

```kotlin
// Cause 1: Removing during for-each loop
val list = mutableListOf(1, 2, 3, 4, 5)
for (item in list) {
    if (item % 2 == 0) {
        list.remove(item)  // ConcurrentModificationException
    }
}

// Cause 2: Multi-threaded access
val sharedList = mutableListOf<Int>()
// Thread 1
for (item in sharedList) {
    process(item)
}
// Thread 2 (simultaneously)
sharedList.add(42)  // ConcurrentModificationException

// Cause 3: Modifying in callback
val listeners = mutableListOf<() -> Unit>()
listeners.add { listeners.clear() }  // Clears during iteration
for (listener in listeners) {
    listener()  // ConcurrentModificationException
}

// Cause 4: Using iterator incorrectly
val iterator = list.iterator()
while (iterator.hasNext()) {
    list.remove(iterator.next())  // ConcurrentModificationException
}
```

## Solutions

### Fix 1: Use iterator.remove()

```kotlin
// Wrong
for (item in list) {
    if (item % 2 == 0) {
        list.remove(item)
    }
}

// Correct — use iterator
val iterator = list.iterator()
while (iterator.hasNext()) {
    val item = iterator.next()
    if (item % 2 == 0) {
        iterator.remove()  // Safe removal via iterator
    }
}
```

### Fix 2: Use removeAll or filter

```kotlin
// Wrong
for (item in list) {
    if (item % 2 == 0) {
        list.remove(item)
    }
}

// Correct
list.removeAll { it % 2 == 0 }

// Or create new list
val filtered = list.filter { it % 2 != 0 }
```

### Fix 3: Use concurrent collections for multi-threaded access

```kotlin
// Wrong — not thread-safe
val list = mutableListOf<Int>()

// Correct — use CopyOnWriteArrayList
val list = java.util.concurrent.CopyOnWriteArrayList<Int>()

// Or use synchronized access
val list = mutableListOf<Int>()
synchronized(list) {
    for (item in list) {
        process(item)
    }
}
```

### Fix 4: Collect changes and apply after iteration

```kotlin
// Wrong
val toRemove = mutableListOf<Int>()
for (item in list) {
    if (item % 2 == 0) {
        list.remove(item)  // ConcurrentModificationException
    }
}

// Correct — collect first, remove after
val toRemove = list.filter { it % 2 == 0 }
list.removeAll(toRemove.toSet())
```

## Examples

```kotlin
fun main() {
    val numbers = mutableListOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    // Safe: filter to create new list
    val evenNumbers = numbers.filter { it % 2 == 0 }
    println("Even: $evenNumbers")

    // Safe: removeAll
    numbers.removeAll { it % 2 == 0 }
    println("After removal: $numbers")
}
```

## Related Errors

- [UnsupportedOperationException]({{< relref "/languages/kotlin/unsupported-operation" >}}) — modifying immutable collection.
- [IndexOutOfBoundsException]({{< relref "/languages/kotlin/index-out-of-bounds" >}}) — accessing invalid index.
- [CancellationException]({{< relref "/languages/kotlin/cancellation-exception" >}}) — coroutine cancelled.

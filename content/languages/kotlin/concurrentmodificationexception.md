---
title: "[Solution] Kotlin ConcurrentModificationException Fix"
description: "Fix Kotlin ConcurrentModificationException when modifying collections during iteration. Learn why concurrent modification fails."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["concurrentmodification", "collection", "iteration", "kotlin"]
weight: 5
---

## What This Error Means

A ConcurrentModificationException is thrown when a collection is modified while being iterated. This is a fail-fast mechanism to detect concurrent access to non-synchronized collections.

## Common Causes

- Adding/removing elements during for loop
- Modifying collection in iterator
- Multiple threads accessing same collection
- Using iterator.remove() incorrectly

## How to Fix

```kotlin
// WRONG: Modifying during iteration
val list = mutableListOf(1, 2, 3)
for (item in list) {
    if (item == 2) list.remove(item)  // ConcurrentModificationException
}

// CORRECT: Use iterator with remove
val iterator = list.iterator()
while (iterator.hasNext()) {
    if (iterator.next() == 2) iterator.remove()
}
```

```kotlin
// WRONG: Removing during for-each
val list = mutableListOf("a", "b", "c")
for (item in list) {
    if (item == "b") list.remove(item)  // Exception
}

// CORRECT: Use filter or filterNot
val list = mutableListOf("a", "b", "c")
list.removeAll { it == "b" }
```

```kotlin
// WRONG: Thread-unsafe collection
val list = mutableListOf<Int>()
// Thread 1: list.add(1)
// Thread 2: list.remove(0)  // ConcurrentModificationException

// CORRECT: Use thread-safe collection
val list = Collections.synchronizedList(mutableListOf<Int>())
// Or use CopyOnWriteArrayList
```

## Examples

```kotlin
// Example 1: Safe removal
val list = mutableListOf(1, 2, 3, 4, 5)
list.removeAll { it % 2 == 0 }  // Remove even numbers

// Example 2: Build new list
val original = listOf(1, 2, 3, 4, 5)
val filtered = original.filter { it % 2 != 0 }

// Example 3: Iterator pattern
val list = mutableListOf(1, 2, 3)
val iter = list.iterator()
while (iter.hasNext()) {
    val item = iter.next()
    if (item == 2) iter.remove()
}
```

## Related Errors

- [UnsupportedOperationException](unsupportedoperationexception) — operation not supported
- [IllegalArgumentException](illegalargumentexception) — invalid argument
- [CancellationException](cancellationexception-kotlin) — coroutine cancelled

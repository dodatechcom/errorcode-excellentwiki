---
title: "[Solution] Kotlin IndexOutOfBoundsException — Array/List Index Fix"
description: "Fix Kotlin IndexOutOfBoundsException when accessing invalid indices on arrays and lists. Check bounds, use safe access, and handle empty collections."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# IndexOutOfBoundsException — Array/List Index Fix

An `IndexOutOfBoundsException` is thrown when you access an index that is outside the valid range of an array, list, or string. Kotlin collections are zero-indexed.

## Description

Kotlin lists and arrays use zero-based indexing. A list of size 3 has valid indices 0, 1, 2. Accessing index 3 or higher, or a negative index (unless using `getOrNull`), throws this exception.

Common scenarios:

- **Off-by-one errors in loops** — iterating past the last valid index.
- **Accessing index 0 of an empty list** — assuming a collection has elements.
- **Stale index after modification** — removing elements while iterating by index.
- **Confusing size with last index** — `size` is count, last index is `size - 1`.

## Common Causes

```kotlin
// Cause 1: Off-by-one in loop
val items = listOf("a", "b", "c")
for (i in 0..items.size) {
    println(items[i])  // IndexOutOfBoundsException when i == 3
}

// Cause 2: Accessing empty list
val empty = emptyList<Int>()
println(empty[0])  // IndexOutOfBoundsException

// Cause 3: String index out of bounds
val text = "hello"
println(text[10])  // StringIndexOutOfBoundsException

// Cause 4: Array access with invalid index
val arr = IntArray(5)
arr[5] = 10  // ArrayIndexOutOfBoundsException
```

## Solutions

### Fix 1: Use `indices` for safe iteration

```kotlin
// Wrong
val items = listOf("a", "b", "c")
for (i in 0..items.size) {
    println(items[i])
}

// Correct
for (i in items.indices) {
    println(items[i])
}

// Even better
for (item in items) {
    println(item)
}
```

### Fix 2: Use `getOrNull` for safe access

```kotlin
// Wrong
val items = listOf("a", "b", "c")
val value = items[5]  // IndexOutOfBoundsException

// Correct
val value = items.getOrNull(5)  // Returns null
val value = items.getOrElse(5) { "default" }  // Returns "default"
```

### Fix 3: Check size before accessing

```kotlin
// Wrong
val list = getList()
val first = list[0]  // IndexOutOfBoundsException if empty

// Correct
val first = list.firstOrNull()  // Returns null if empty
```

### Fix 4: Don't modify list while iterating by index

```kotlin
// Wrong
val data = mutableListOf(10, 20, 30, 40, 50)
for (i in data.indices) {
    if (data[i] == 20) {
        data.removeAt(i)  // Indices shift, causes out-of-bounds
    }
}

// Correct — filter to create a new list
val data = mutableListOf(10, 20, 30, 40, 50)
val filtered = data.filter { it != 20 }
```

## Examples

```kotlin
fun main() {
    val list = listOf(1, 2, 3)

    // These throw IndexOutOfBoundsException:
    // val a = list[3]
    // val b = list[-1]

    // Safe alternatives
    println(list.getOrNull(3))      // null
    println(list.getOrElse(3) { 0 }) // 0
    println(list.getOrNull(0))       // 1
}
```

## Related Errors

- [ArrayIndexOutOfBoundsException]({{< relref "/languages/kotlin/index-out-of-bounds" >}}) — same concept for arrays.
- [NoSuchElementException]({{< relref "/languages/kotlin/no-such-method" >}}) — element not found in collection.
- [ConcurrentModificationException]({{< relref "/languages/kotlin/concurrent-modification" >}}) — modifying collection while iterating.

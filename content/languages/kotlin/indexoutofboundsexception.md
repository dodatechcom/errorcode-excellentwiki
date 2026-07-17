---
title: "[Solution] Kotlin IndexOutOfBoundsException Fix"
description: "Fix Kotlin IndexOutOfBoundsException when accessing invalid indices. Learn why index access fails and how to check bounds."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["indexoutofboundsexception", "index", "bounds", "kotlin"]
weight: 5
---

## What This Error Means

An IndexOutOfBoundsException is thrown when you access a collection element at an index that is outside the valid range. This is one of the most common runtime errors.

## Common Causes

- Accessing index >= size
- Off-by-one errors in loops
- Empty list access
- String index out of range

## How to Fix

```kotlin
// WRONG: Index beyond bounds
val list = listOf(1, 2, 3)
val value = list[5]  // IndexOutOfBoundsException

// CORRECT: Check bounds
if (list.indices.contains(5)) {
    val value = list[5]
}
```

```kotlin
// WRONG: Accessing first on empty list
val empty = emptyList<Int>()
val first = empty[0]  // IndexOutOfBoundsException

// CORRECT: Use firstOrNull
val first = empty.firstOrNull()  // null
```

```kotlin
// WRONG: Off-by-one in loop
val items = listOf("a", "b", "c")
for (i in 0..items.size) {  // items.size is 3, indices are 0,1,2
    println(items[i])  // Crashes at i=3
}

// CORRECT: Use proper range
for (i in 0 until items.size) {
    println(items[i])
}
// Or better:
for (item in items) {
    println(item)
}
```

## Examples

```kotlin
// Example 1: Safe access
val list = listOf(1, 2, 3)
val value = list.getOrNull(5)  // null

// Example 2: Substring bounds
val str = "Hello"
val sub = str.substring(0, 5)  // "Hello"
val sub2 = str.substring(0, 10)  // IndexOutOfBoundsException

// Example 3: Array bounds
val arr = IntArray(10)
arr[9] = 42  // OK
arr[10] = 42  // IndexOutOfBoundsException
```

## Related Errors

- [NullPointerException](nullpointerexception-kotlin) — null access
- [IllegalArgumentException](illegalargumentexception) — invalid argument
- [ClassCastException](classcastexception-kotlin) — type cast failed

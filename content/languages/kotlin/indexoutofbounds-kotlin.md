---
title: "[Solution] Kotlin IndexOutOfBoundsException — Index Out of Range Fix"
description: "Fix Kotlin IndexOutOfBoundsException when accessing collections beyond bounds. Learn safe indexing patterns in Kotlin."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# IndexOutOfBoundsException — Index Out of Range

An `IndexOutOfBoundsException` occurs when you access a collection element at an index outside its valid range.

## Description

Kotlin collections are zero-indexed. Accessing an index beyond `size - 1` or a negative index throws `IndexOutOfBoundsException`. String indices work similarly with `get()`.

Common causes:

- **Off-by-one error** — accessing index equal to size
- **Empty collection access** — trying to access elements in empty list
- **Dynamic index** — computed index exceeds bounds
- **String index** — invalid character position

## Common Causes

```kotlin
// Cause 1: Off-by-one error
val list = listOf(1, 2, 3)
println(list[3])  // IndexOutOfBoundsException

// Cause 2: Empty collection
val empty = emptyList<Int>()
println(empty[0])  // IndexOutOfBoundsException

// Cause 3: Dynamic index
val items = listOf("a", "b", "c")
val index = items.size
println(items[index])  // IndexOutOfBoundsException

// Cause 4: String index
val str = "Hello"
println(str[10])  // StringIndexOutOfBoundsException
```

## How to Fix

### Fix 1: Check bounds before access

```kotlin
// Wrong
val list = listOf(1, 2, 3)
println(list[5])  // Exception

// Correct
if (index < list.size) {
    println(list[index])
}
```

### Fix 2: Use `getOrNull`

```kotlin
// Wrong
val list = listOf(1, 2, 3)
println(list[5])  // Exception

// Correct
println(list.getOrNull(5))  // null
```

### Fix 3: Use `elementAtOrNull`

```kotlin
// Wrong
val list = listOf(1, 2, 3)
println(list[5])  // Exception

// Correct
println(list.elementAtOrNull(5))  // null
```

### Fix 4: Use safe extension

```kotlin
// Wrong
val list = listOf(1, 2, 3)
println(list[5])  // Exception

// Correct
fun <T> List<T>.getOrNull(index: Int): T? {
    return if (index in indices) this[index] else null
}
```

## Examples

```kotlin
// Example 1: Safe list access
val numbers = listOf(10, 20, 30)
val first = numbers.getOrNull(0)  // 10
val fifth = numbers.getOrNull(4)  // null

// Example 2: Safe string access
val str = "Hello"
val char = str.getOrNull(1)  // 'e'
val missing = str.getOrNull(10)  // null
```

## Related Errors

- [NullPointerException]({{< relref "/languages/kotlin/nullpointer-kotlin" >}}) — null dereference
- [NoSuchElementException]({{< relref "/languages/kotlin/nosuchelement-kotlin" >}}) — element not found
- [ClassCastException]({{< relref "/languages/kotlin/typecast-kotlin" >}}) — wrong type cast

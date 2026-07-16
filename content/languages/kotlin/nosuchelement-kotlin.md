---
title: "[Solution] Kotlin NoSuchElementException — Element Not Found Fix"
description: "Fix Kotlin NoSuchElementException when retrieving elements from collections. Learn safe element access patterns."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["nosuchelementexception", "element-not-found", "collection", "kotlin"]
weight: 5
---

# NoSuchElementException — Element Not Found

A `NoSuchElementException` occurs when you try to access an element that doesn't exist in a collection or iterator.

## Description

Kotlin collections throw `NoSuchElementException` when you use methods like `first()`, `last()`, `elementAt()` on empty collections or when the element isn't found.

Common causes:

- **Empty collection access** — calling `first()` on empty list
- **Missing iterator element** — accessing beyond iterator bounds
- **Map key not found** — `map.getValue()` with missing key
- **Set element missing** — `set.element()` with non-existent element

## Common Causes

```kotlin
// Cause 1: Empty collection
val empty = emptyList<Int>()
empty.first()  // NoSuchElementException

// Cause 2: Iterator bounds
val list = listOf(1, 2, 3)
val iterator = list.iterator()
iterator.next()  // 1
iterator.next()  // 2
iterator.next()  // 3
iterator.next()  // NoSuchElementException

// Cause 3: Map key not found
val map = mapOf("a" to 1, "b" to 2)
map.getValue("c")  // NoSuchElementException

// Cause 4: Single element on empty
val empty = emptyList<Int>()
empty.single()  // NoSuchElementException
```

## How to Fix

### Fix 1: Use `firstOrNull` / `lastOrNull`

```kotlin
// Wrong
val empty = emptyList<Int>()
empty.first()  // Exception

// Correct
val first = empty.firstOrNull()  // null
```

### Fix 2: Use `elementAtOrNull`

```kotlin
// Wrong
val list = listOf(1, 2, 3)
list.elementAt(5)  // Exception

// Correct
list.elementAtOrNull(5)  // null
```

### Fix 3: Use `getOrElse` for maps

```kotlin
// Wrong
val map = mapOf("a" to 1)
map.getValue("c")  // Exception

// Correct
val value = map.getOrElse("c") { 0 }  // 0
```

### Fix 4: Check before access

```kotlin
// Wrong
val list = listOf(1, 2, 3)
list.first()  // Works, but risky if empty

// Correct
if (list.isNotEmpty()) {
    val first = list.first()
}
```

## Examples

```kotlin
// Example 1: Safe element access
val numbers = listOf(10, 20, 30)
val first = numbers.firstOrNull()  // 10
val missing = numbers.firstOrNull { it > 100 }  // null

// Example 2: Safe map access
val config = mapOf("host" to "localhost")
val port = config["port"]?.toIntOrNull() ?: 8080
```

## Related Errors

- [IndexOutOfBoundsException]({{< relref "/languages/kotlin/index-out-of-bounds" >}}) — index beyond bounds
- [NullPointerException]({{< relref "/languages/kotlin/nullpointer-kotlin" >}}) — null dereference
- [IllegalArgumentException]({{< relref "/languages/kotlin/illegal-argument" >}}) — invalid argument

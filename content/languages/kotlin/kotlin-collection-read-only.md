---
title: "[Solution] Kotlin Modifying Read-Only Collection Error"
description: "Fix Kotlin UnsupportedOperationException when modifying a read-only collection. Learn the difference between List and MutableList."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1002
---

## What This Error Means

An UnsupportedOperationException is thrown when attempting to modify a collection that was returned as a read-only type (`List`, `Set`, `Map`). Kotlin's `listOf()`, `setOf()`, `mapOf()` return immutable views backed by read-only collection types.

## Common Causes

- Using `listOf()` then calling `add()` or `remove()` on it
- Assigning `mutableListOf()` to a `List` variable and later trying to modify through the `List` reference
- Returning `List` from a function and expecting caller to modify it
- Java interop returning unmodifiable collections typed as `List`

```kotlin
// UnsupportedOperationException at runtime
val names: List<String> = listOf("Alice", "Bob")
(names as MutableList).add("Charlie")  // May throw
```

## How to Fix

**1. Use mutableListOf for mutable collections**

```kotlin
// WRONG: Can't modify
val items = listOf("a", "b")
items.add("c")  // Error

// CORRECT: Use mutableListOf
val items = mutableListOf("a", "b")
items.add("c")  // Works
```

**2. Create mutable copies when needed**

```kotlin
val readOnly = listOf(1, 2, 3)
val mutable = readOnly.toMutableList()
mutable.add(4)  // Safe
```

**3. Return MutableList when mutation is needed**

```kotlin
// WRONG: Function returns immutable view
fun getItems(): List<String> = listOf("a", "b")

// CORRECT: Return mutable if callers need to modify
fun getItems(): MutableList<String> = mutableListOf("a", "b")
```

**4. Use copy-on-write pattern**

```kotlin
fun addItem(list: List<String>, item: String): List<String> {
    return list + item  // Returns new list
}
```

## Examples

```kotlin
// Example 1: toList() returns new immutable list
val original = mutableListOf(1, 2, 3)
val snapshot = original.toList()
original.add(4)
println(snapshot)  // [1, 2, 3] unchanged

// Example 2: Java interop returning unmodifiable list
val javaList: List<String> = Collections.unmodifiableList(mutableListOf("a"))
// javaList is already read-only

// Example 3: KDoc type hints for mutability
interface Repository {
    fun getAll(): List<User>       // Read-only
    fun getAllMutable(): MutableList<User>  // Mutable
}
```

## Related Errors

- [UnsupportedOperationException](unsupportedoperationexception) — operation not supported
- [ConcurrentModificationException](concurrentmodificationexception) — concurrent access
- [IllegalStateException](illegalstateexception-kotlin) — invalid state

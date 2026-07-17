---
title: "[Solution] Kotlin UnsupportedOperationException — Operation Not Supported Fix"
description: "Fix Kotlin UnsupportedOperationException when calling a method that is not supported by the implementation. Check API contracts and use mutable variants."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# UnsupportedOperationException — Operation Not Supported Fix

An `UnsupportedOperationException` is thrown when an operation is not supported by the current object. This typically occurs when attempting to modify an immutable collection or calling an abstract method.

## Description

This exception signals that the object doesn't implement the requested operation. The most common cause is trying to modify an immutable collection returned by Kotlin stdlib functions.

Common scenarios:

- **Modifying an immutable list** — `listOf()` returns a read-only list.
- **Adding to an empty list** — `emptyList()` is immutable.
- **Calling unsupported abstract methods** — interface method not implemented.
- **Using platform-specific APIs** — operation not available on current platform.

## Common Causes

```kotlin
// Cause 1: Modifying an immutable list
val list = listOf(1, 2, 3)
list.add(4)  // UnsupportedOperationException

// Cause 2: Modifying empty list
val empty = emptyList<Int>()
empty.add(1)  // UnsupportedOperationException

// Cause 3: Modifying list returned by stdlib functions
val mapped = listOf(1, 2, 3).map { it * 2 }
mapped.toMutableList().add(4)  // OK
mapped.add(4)  // UnsupportedOperationException

// Cause 4: Calling abstract interface method
interface Shape {
    fun area(): Double
}
// Cannot instantiate interface directly
```

## Solutions

### Fix 1: Use mutable collection builders

```kotlin
// Wrong
val list = listOf(1, 2, 3)
list.add(4)  // UnsupportedOperationException

// Correct
val list = mutableListOf(1, 2, 3)
list.add(4)  // Works

// Or build a new list
val list = buildList {
    add(1)
    add(2)
    add(3)
}
```

### Fix 2: Convert to mutable before modifying

```kotlin
// Wrong
val result = listOf(1, 2, 3).map { it * 2 }
result.add(4)  // UnsupportedOperationException

// Correct
val result = listOf(1, 2, 3).map { it * 2 }.toMutableList()
result.add(4)
```

### Fix 3: Use `ArrayList` or `mutableListOf` for dynamic collections

```kotlin
// Wrong — returns immutable
fun getItems(): List<String> = listOf("a", "b", "c")

// Correct — returns mutable
fun getItems(): MutableList<String> = mutableListOf("a", "b", "c")

// Best — return read-only, let caller decide
fun getItems(): List<String> = listOf("a", "b", "c")
fun getMutableItems(): MutableList<String> = mutableListOf("a", "b", "c")
```

### Fix 4: Implement interface methods properly

```kotlin
// Wrong — missing implementation
interface Cache<K, V> {
    fun get(key: K): V?
    fun put(key: K, value: V)
}

// Correct — implement all methods
class InMemoryCache<K, V> : Cache<K, V> {
    private val map = mutableMapOf<K, V>()
    override fun get(key: K): V? = map[key]
    override fun put(key: K, value: V) { map[key] = value }
}
```

## Examples

```kotlin
fun main() {
    val immutable = listOf(1, 2, 3)
    // immutable.add(4)  // UnsupportedOperationException

    val mutable = immutable.toMutableList()
    mutable.add(4)
    println(mutable)  // [1, 2, 3, 4]
}
```

## Related Errors

- [ConcurrentModificationException]({{< relref "/languages/kotlin/concurrent-modification" >}}) — modifying collection while iterating.
- [IndexOutOfBoundsException]({{< relref "/languages/kotlin/index-out-of-bounds" >}}) — accessing invalid index.
- [IllegalStateException]({{< relref "/languages/kotlin/illegal-state" >}}) — object in wrong state.

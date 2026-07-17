---
title: "[Solution] Kotlin Destructuring Iterator Error Fix"
description: "Fix Kotlin destructuring iterator errors. Learn why iterator destructuring fails and how to iterate with destructuring."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A destructuring iterator error occurs when iterating over a collection with destructuring and the iterator does not provide the expected number of values.

## Common Causes

- Iterator does not support destructuring
- Wrong number of values from iterator
- Missing iterator function
- Wrong collection type

## How to Fix

```kotlin
// WRONG: Iterator without destructuring support
class SimpleList(val items: List<Int>) {
    fun iterator() = items.iterator()
}
val list = SimpleList(listOf(1, 2, 3))
for ((index, value) in list) {  // Error: iterator returns Int, not Pair
    println("$index: $value")
}

// CORRECT: Use indexed access
val list = SimpleList(listOf(1, 2, 3))
for ((index, value) in list.items.withIndex()) {
    println("$index: $value")
}
```

```kotlin
// WRONG: Wrong number of destructuring variables
val pairs = listOf(Pair("a", 1), Pair("b", 2))
for ((key, value, extra) in pairs) {  // Error: only 2 components
    println("$key: $value")
}

// CORRECT: Match component count
for ((key, value) in pairs) {
    println("$key: $value")
}
```

## Examples

```kotlin
// Example 1: withIndex
val list = listOf("a", "b", "c")
for ((index, value) in list.withIndex()) {
    println("$index: $value")
}

// Example 2: Map destructuring
val map = mapOf("a" to 1, "b" to 2)
for ((key, value) in map) {
    println("$key: $value")
}

// Example 3: Custom iterator
class Counter(val max: Int) : Iterator<Int> {
    private var current = 0
    override fun hasNext() = current < max
    override fun next() = current++
}
for (i in Counter(5)) {
    println(i)
}
```

## Related Errors

- [Destructuring declaration error](destructuring-error) — destructuring issue
- [Destructuring component error](destructuring-component-error) — component issue
- [IndexOutOfBoundsException](indexoutofboundsexception) — index out of range

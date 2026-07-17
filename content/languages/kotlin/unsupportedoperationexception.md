---
title: "[Solution] Kotlin UnsupportedOperationException Fix"
description: "Fix Kotlin UnsupportedOperationException when operations are not supported. Learn why operations fail and how to handle unsupported operations."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

An UnsupportedOperationException is thrown when an operation is not supported for a particular object or collection. This commonly happens when trying to modify immutable collections.

## Common Causes

- Modifying immutable list (listOf)
- Adding to read-only collection
- Unsupported iterator operation
- Platform type limitations

## How to Fix

```kotlin
// WRONG: Modifying immutable list
val list = listOf(1, 2, 3)
list.add(4)  // UnsupportedOperationException

// CORRECT: Use mutable list
val list = mutableListOf(1, 2, 3)
list.add(4)  // OK
```

```kotlin
// WRONG: Modifying empty list
val empty = emptyList<Int>()
empty.add(1)  // UnsupportedOperationException

// CORRECT: Use mutableListOf
val list = mutableListOf<Int>()
list.add(1)  // OK
```

```kotlin
// WRONG: SubList modification
val list = mutableListOf(1, 2, 3)
val subList = list.subList(0, 2)
subList.add(4)  // May throw if not supported

// CORRECT: Create new list from subList
val subList = list.subList(0, 2).toMutableList()
subList.add(4)
```

## Examples

```kotlin
// Example 1: Immutable vs mutable
val immutable = listOf(1, 2, 3)  // Cannot modify
val mutable = mutableListOf(1, 2, 3)  // Can modify

// Example 2: Collection operations
val set = setOf(1, 2, 3)  // Sets are immutable by default
val mutableSet = mutableSetOf(1, 2, 3)

// Example 3: List transformation
val original = listOf(1, 2, 3)
val new = original + 4  // Creates new list
```

## Related Errors

- [IllegalArgumentException](illegalargumentexception) — invalid argument
- [ClassCastException](classcastexception-kotlin) — type cast failed
- [ConcurrentModificationException](concurrentmodificationexception) — concurrent modification

---
title: "[Solution] Kotlin Collection Capacity Exceeded — Grow Buffer Error"
description: "Fix Kotlin collection capacity exceeded errors. Learn why list/set buffer overflow occurs and how to pre-allocate or resize collections."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1001
---

## What This Error Means

A collection capacity exceeded error occurs when the internal grow buffer of a Kotlin collection (ArrayList, HashSet, etc.) cannot expand to accommodate more elements. This typically happens due to memory pressure or integer overflow on extremely large collections.

## Common Causes

- Attempting to add elements beyond array-backed list capacity
- Integer overflow in capacity calculation for very large collections
- Insufficient heap memory for buffer reallocation
- Misuse of initial capacity in `mutableListOf` or `ArrayList`

```kotlin
// Capacity exceeded during bulk add
val list = ArrayList<Int>()
for (i in 0..Int.MAX_VALUE) {
    list.add(i)  // OutOfMemoryError or capacity overflow
}
```

## How to Fix

**1. Pre-allocate with estimated capacity**

```kotlin
// WRONG: No initial capacity hint
val list = mutableListOf<Int>()
repeat(1_000_000) { list.add(it) }  // Multiple reallocations

// CORRECT: Pre-allocate
val list = ArrayList<Int>(1_000_000)
repeat(1_000_000) { list.add(it) }
```

**2. Use chunked processing for large datasets**

```kotlin
// WRONG: Load everything into memory
val hugeList = database.selectAll().toMutableList()

// CORRECT: Process in chunks
database.selectAll()
    .chunked(10_000) { chunk ->
        processBatch(chunk)
    }
```

**3. Use sequence for lazy evaluation**

```kotlin
// WRONG: Materializing large intermediate list
val results = (1..Int.MAX_VALUE).toList().map { it * 2 }

// CORRECT: Use sequence for lazy pipeline
val results = (1..Int.MAX_VALUE).asSequence().map { it * 2 }
```

**4. Catch capacity-related memory errors**

```kotlin
try {
    val list = ArrayList<Int>(requestedSize)
    list.addAll(elements)
} catch (e: OutOfMemoryError) {
    // Reduce batch size or switch to streaming
    processInSmallerBatches(elements)
}
```

## Examples

```kotlin
// Example 1: Appending to list with capacity check
fun <T> safeAdd(list: MutableList<T>, element: T): Boolean {
    return try {
        list.add(element)
        true
    } catch (e: OutOfMemoryError) {
        false
    }
}

// Example 2: Building string with StringBuilder capacity
val sb = StringBuilder(estimatedLength)
for (item in items) {
    sb.append(item).append('\n')
}

// Example 3: Using linked data structures for huge collections
val linkedList = LinkedList<Int>()
repeat(5_000_000) { linkedList.add(it) }
```

## Related Errors

- [OutOfMemoryError](outofmemory-kotlin) — heap memory exhausted
- [IndexOutOfBoundsException](indexoutofboundsexception) — index out of range
- [StackOverflowError](stackoverflow-kotlin) — stack overflow

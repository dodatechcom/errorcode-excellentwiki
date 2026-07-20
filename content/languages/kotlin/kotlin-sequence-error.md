---
title: "[Solution] Kotlin Sequence Terminal Operation Misuse"
description: "Fix Kotlin sequence errors including terminal operation misuse and infinite sequence issues. Learn lazy evaluation pitfalls."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1006
---

## Common Causes

- Calling multiple terminal operations on a sequence (`first()` then `toList()`)
- Infinite sequence without `take()` or `takeWhile()`
- `concurrentModificationException` when sequence source is modified during evaluation
- Using `iterator()` directly then losing the iterator reference

```kotlin
val seq = listOf(1, 2, 3).asSequence().filter { it > 1 }
println(seq.first())   // 2
println(seq.toList())  // May behave unexpectedly in some chain patterns
```

## How to Fix

**1. Collect to a variable before reusing**

```kotlin
// WRONG: Multiple terminals on single sequence
val result = generateSequence(1) { it + 1 }.filter { it % 2 == 0 }
println(result.first())      // 2
println(result.take(5).toList())  // May recompute

// CORRECT: Materialize once
val result = generateSequence(1) { it + 1 }.filter { it % 2 == 0 }.take(100).toList()
```

**2. Always bound infinite sequences**

```kotlin
// WRONG: Infinite loop
val naturals = generateSequence(1) { it + 1 }
naturals.forEach { println(it) }  // Never stops

// CORRECT: Bound with take
val naturals = generateSequence(1) { it + 1 }
naturals.take(100).forEach { println(it) }
```

**3. Use sequenceOf for one-shot pipelines**

```kotlin
// One-shot terminal operation
val result = sequenceOf(1, 2, 3, 4, 5)
    .map { it * it }
    .filter { it > 5 }
    .toList()
// [9, 25]
```

**4. Handle exceptions in sequence chains**

```kotlin
val result = sequence {
    yieldAll(listOf(1, 2, 3))
    throw IllegalStateException("boom")
}.catch { e -> println("Caught: ${e.message}") }
 .toList()
```

## Examples

```kotlin
// Example 1: generateSequence with seed
val fibs = generateSequence(Pair(0L, 1L)) { Pair(it.second, it.first + it.second) }
    .map { it.first }
    .take(20)
    .toList()

// Example 2: sequence builder
fun <T> sequenceFromIterable(source: Iterable<T>): Sequence<T> = sequence {
    for (item in source) {
        yield(item)
    }
}

// Example 3: Chunked sequences for memory efficiency
val hugeData = (1..1_000_000).asSequence()
val chunks = hugeData.chunked(1000)
chunks.take(5).forEach { chunk ->
    println("Chunk size: ${chunk.size}")
}
```

## Related Errors

- [OutOfMemoryError](outofmemory-kotlin) — heap memory exhausted
- [CancellationException](cancellationexception-kotlin) — coroutine cancelled
- [Flow backpressure error](kotlin-flow-backpressure) — flow emission issue

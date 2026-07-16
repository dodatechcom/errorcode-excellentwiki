---
title: "[Solution] Kotlin OutOfMemoryError — Heap Memory Fix"
description: "Fix Kotlin OutOfMemoryError when the JVM runs out of heap memory. Process data in chunks, use sequences, and optimize data structures."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["outofmemoryerror", "heap", "memory", "oom", "gc"]
weight: 5
---

# OutOfMemoryError — Heap Memory Fix

An `OutOfMemoryError` is thrown when the JVM cannot allocate an object because it is out of memory, and the garbage collector cannot free enough space.

## Description

The JVM has a limited heap size (default varies by platform, typically 256MB–1GB). When objects accumulate faster than they are collected, the heap fills up and the JVM throws `OutOfMemoryError`. This is an `Error`, not an exception, indicating a serious problem.

Common scenarios:

- **Loading large datasets into memory** — reading entire files into lists.
- **Creating excessive objects** — string concatenation in loops.
- **Memory leaks** — references held longer than needed.
- **Large bitmap/image processing** — loading high-resolution images.

## Common Causes

```kotlin
// Cause 1: Creating a massive list
val hugeList = (0..1_000_000_000).toList()  // OutOfMemoryError

// Cause 2: String concatenation in loop
var result = ""
for (i in 0..1_000_000) {
    result += "item $i "  // Creates millions of intermediate strings
}

// Cause 3: Loading entire file into memory
val largeFile = File("huge.bin").readBytes()  // OutOfMemoryError for large files

// Cause 4: Retaining references unnecessarily
class Cache {
    private val entries = mutableListOf<ByteArray>()
    fun add(data: ByteArray) {
        entries.add(data)  // Never released
    }
}
```

## Solutions

### Fix 1: Use sequences for lazy evaluation

```kotlin
// Wrong — creates entire list in memory
val squares = (0..1_000_000).map { it * it }
squares.forEach { process(it) }

// Correct — sequences process one item at a time
val squares = (0..1_000_000).asSequence().map { it * it }
squares.forEach { process(it) }
```

### Fix 2: Process large files in chunks

```kotlin
// Wrong — loads entire file
val lines = File("huge.txt").readLines()

// Correct — process line by line
File("huge.txt").bufferedReader().useLines { lines ->
    lines.forEach { line ->
        process(line)
    }
}

// Correct — read in fixed-size chunks
File("huge.bin").inputStream().use { stream ->
    val buffer = ByteArray(8192)
    while (true) {
        val bytesRead = stream.read(buffer)
        if (bytesRead == -1) break
        process(buffer.copyOf(bytesRead))
    }
}
```

### Fix 3: Use StringBuilder for string operations

```kotlin
// Wrong — creates millions of intermediate strings
var result = ""
for (i in 0..1_000_000) {
    result += "item $i "
}

// Correct — StringBuilder reuses buffer
val sb = StringBuilder()
for (i in 0..1_000_000) {
    sb.append("item $i ")
}
val result = sb.toString()
```

### Fix 4: Release references when done

```kotlin
// Wrong — references held indefinitely
class DataProcessor {
    private var largeData: ByteArray? = null

    fun process() {
        largeData = loadHugeData()
        analyze(largeData!!)
        // largeData still referenced
    }
}

// Correct — release after use
class DataProcessor {
    fun process() {
        val data = loadHugeData()
        analyze(data)
        // data goes out of scope, eligible for GC
    }
}
```

## Examples

```kotlin
fun main() {
    // Process data lazily with sequences
    val processed = (1..10_000_000).asSequence()
        .filter { it % 2 == 0 }
        .map { it * it }
        .take(10)

    processed.forEach { println(it) }
}
```

## Related Errors

- [StackOverflowError]({{< relref "/languages/kotlin/stack-overflow" >}}) — stack memory exhausted from recursion.
- [RuntimeException]({{< relref "/languages/kotlin/runtime-exception" >}}) — general runtime error.
- [IOException]({{< relref "/languages/kotlin/io-exception" >}}) — I/O operation failed.

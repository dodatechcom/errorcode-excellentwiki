---
title: "[Solution] Kotlin OutOfMemoryError — Heap Memory Fix"
description: "Fix Kotlin OutOfMemoryError when heap memory is exhausted. Learn how to identify and resolve memory leaks and excessive allocation."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["outofmemoryerror", "heap-memory", "memory-leak", "kotlin"]
weight: 5
---

# OutOfMemoryError — Heap Memory Exhausted

An `OutOfMemoryError` occurs when the JVM cannot allocate more objects because the heap is full.

## Description

The JVM heap stores all objects. When too many objects are created and not garbage collected, the heap fills up. This is common with large collections, memory leaks, or excessive allocation.

Common causes:

- **Large collections** — loading too much data into memory
- **Memory leaks** — objects not being garbage collected
- **Bitmap/Image processing** — large image buffers
- **String concatenation** — building huge strings inefficiently

## Common Causes

```kotlin
// Cause 1: Large collection
val hugeList = (1..Int.MAX_VALUE).toList()  // OutOfMemoryError

// Cause 2: Memory leak
class Cache {
    companion object {
        val data = mutableMapOf<String, Any>()  // Never cleared
    }
}
Cache.data["key"] = ByteArray(1024 * 1024)  // 1MB

// Cause 3: String concatenation in loop
var result = ""
repeat(1000000) {
    result += "a"  // Creates many intermediate strings
}

// Cause 4: Large array allocation
val array = IntArray(Int.MAX_VALUE / 2)  // OutOfMemoryError
```

## How to Fix

### Fix 1: Use lazy loading

```kotlin
// Wrong
val hugeList = loadAllData()  // Loads everything

// Correct
val data = loadPage(pageNumber)  // Load only what's needed
```

### Fix 2: Clear collections

```kotlin
// Wrong
class Cache {
    val data = mutableMapOf<String, Any>()
}

// Correct
class Cache {
    val data = mutableMapOf<String, Any>()
    fun clear() = data.clear()
}
```

### Fix 3: Use StringBuilder

```kotlin
// Wrong
var result = ""
repeat(1000000) {
    result += "a"
}

// Correct
val sb = StringBuilder()
repeat(1000000) {
    sb.append("a")
}
val result = sb.toString()
```

### Fix 4: Use streams for large data

```kotlin
// Wrong
val list = (1..10000000).toList()  // Large list in memory

// Correct
val sum = (1..10000000).sum()  // Process without storing
```

## Examples

```kotlin
// Example 1: Memory-efficient processing
fun processLargeFile(path: String) {
    File(path).bufferedReader().useLines { lines ->
        lines.forEach { line ->
            process(line)
        }
    }
}

// Example 2: Proper cleanup
class ImageCache {
    private val cache = mutableMapOf<String, Bitmap>()
    
    fun get(key: String): Bitmap? {
        return cache[key]
    }
    
    fun put(key: String, bitmap: Bitmap) {
        if (cache.size > 100) {
            cache.clear()  // Simple eviction
        }
        cache[key] = bitmap
    }
    
    fun clear() = cache.clear()
}
```

## Related Errors

- [StackOverflowError]({{< relref "/languages/kotlin/stack-overflow" >}}) — infinite recursion
- [ConcurrentModificationException]({{< relref "/languages/kotlin/concurrent-modification" >}}) — concurrent access
- [IOException]({{< relref "/languages/kotlin/io-exception" >}}) — I/O operation failed

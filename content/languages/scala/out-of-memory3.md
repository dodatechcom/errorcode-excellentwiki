---
title: "OutOfMemoryException"
description: "An OutOfMemoryException occurs when the JVM cannot allocate enough memory."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["memory", "out-of-memory", "allocation", "outofmemoryexception"]
weight: 5
---

## What This Error Means

An `OutOfMemoryException` is thrown when the Java Virtual Machine cannot allocate sufficient memory for an operation. This commonly happens when creating very large collections or when there's a memory leak.

## Common Causes

- Creating very large arrays or collections
- Accumulating data in memory without cleanup
- Memory leaks from unreleased resources
- Loading large files into memory

## How to Fix

```scala
// WRONG: Creating huge collection
val huge = (1 to Int.MaxValue).toList  // OutOfMemoryException

// CORRECT: Process in chunks or use streams
val huge = (1 to 1000000).iterator  // lazy evaluation
huge.foreach(println)
```

```scala
// WRONG: Building huge string
val sb = new StringBuilder()
for (i <- 1 to 100000000) sb.append("x")  // may cause OOM

// CORRECT: Use buffered approach or limit size
val sb = new StringBuilder()
for (i <- 1 to 1000000) sb.append("x")
val result = sb.toString
```

## Examples

```scala
// Example 1: Infinite stream
val stream = Stream.continually(1)  // infinite, but lazy
val list = stream.take(1000000000).toList  // OutOfMemoryException

// Example 2: Large array
val arr = new Array[Int](Int.MaxValue / 2)  // OutOfMemoryException

// Example 3: Recursive list building
def buildList(n: Int): List[Int] = n :: buildList(n + 1)
buildList(0)  // StackOverflow or OutOfMemory
```

## Related Errors

- [StackOverflowException](/languages/scala/stack-overflow3)
- [IndexOutOfBoundsException](/languages/scala/index-out-of-bound)

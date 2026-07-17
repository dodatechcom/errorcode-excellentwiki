---
title: "[Solution] Scala OutOfMemoryError"
description: "Fix Scala OutOfMemoryError. Learn about heap space issues and memory management in Scala applications."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `OutOfMemoryError` occurs when the JVM cannot allocate more memory for an object because the heap is full and garbage collection cannot free enough space.

## Common Causes

- Loading too much data into memory at once
- Memory leaks (retained references to unused objects)
- Large collection operations without streaming
- Insufficient JVM heap space configuration
- Recursive functions without base case

## How to Fix

Increase JVM heap space:

```bash
scala -J-Xmx4g MyApplication
# or
java -Xmx4g -Xms2g -cp myapp.jar Main
```

Process data in chunks:

```scala
import scala.io.Source

def processLargeFile(path: String): Unit = {
  val source = Source.fromFile(path)
  try {
    for (line <- source.getLines()) {
      processLine(line)
    }
  } finally {
    source.close()
  }
}
```

Use lazy collections:

```scala
// Wrong: loads all into memory
val data = (1 to 10000000).map(computeExpensiveValue)

// Correct: lazy evaluation
val data = (1 to 10000000).view.map(computeExpensiveValue)
data.take(100).foreach(println)
```

Fix memory leaks:

```scala
// Wrong: retaining reference
class Cache {
  private val data = scala.collection.mutable.Map.empty[String, Any]
  def put(key: String, value: Any): Unit = data(key) = value
}

// Correct: use WeakHashMap or limit size
import java.util.WeakHashMap
```

## Examples

```scala
object OomExample extends App {
  val array = new Array[Int](Int.MaxValue) // OutOfMemoryError
}
```

## Related Errors

- [stackoverflow] — stack overflow from recursion
- [nullpointer] — null pointer access

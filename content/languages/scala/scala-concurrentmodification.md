---
title: "[Solution] Scala ConcurrentModificationException"
description: "Fix Scala ConcurrentModificationException. Learn about thread-safe collections and iterator invalidation in Scala."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `ConcurrentModificationException` occurs when a collection is modified while being iterated, or when multiple threads access a non-thread-safe collection concurrently.

## Common Causes

- Modifying collection during foreach/iterator loop
- Multiple threads accessing shared mutable collection
- Removing elements while iterating
- Adding elements during iteration

## How to Fix

Use `synchronized` blocks:

```scala
val list = scala.collection.mutable.ListBuffer(1, 2, 3)

synchronized {
  list.foreach { item =>
    if (item == 2) list += 4 // Safe with synchronized
  }
}
```

Use thread-safe collections:

```scala
import java.util.concurrent.ConcurrentHashMap

val map = new ConcurrentHashMap[String, Int]()
map.put("key", 1)
// Multiple threads can safely modify
```

Create new collection during iteration:

```scala
val list = List(1, 2, 3, 4, 5)
val filtered = list.filter(_ > 2) // Returns new list
```

Use `toList` snapshot:

```scala
val buffer = scala.collection.mutable.ArrayBuffer(1, 2, 3)
buffer.toList.foreach { item =>
  // Iterating over immutable copy
  println(item)
}
```

## Examples

```scala
object ConcurrentExample extends App {
  val list = scala.collection.mutable.ArrayBuffer(1, 2, 3)
  for (item <- list) {
    list += item * 2 // ConcurrentModificationException
  }
}
```

## Related Errors

- [unsupportedoperation] — operation not supported
- [oom] — out of memory

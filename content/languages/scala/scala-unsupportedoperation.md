---
title: "[Solution] Scala UnsupportedOperationException"
description: "Fix Scala UnsupportedOperationException. Learn about immutable collection operations and when this error occurs."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["unsupported", "operation", "collection", "immutable", "mutable"]
weight: 5
---

## What This Error Means

An `UnsupportedOperationException` occurs when attempting an operation on a collection or object that does not support it. This commonly happens when trying to modify an immutable collection or calling a method not implemented by the concrete class.

## Common Causes

- Calling `add` or `remove` on an immutable collection
- Using mutable methods on Java `unmodifiable` collections
- Attempting unsupported operation on empty collection
- Calling abstract method without implementation

## How to Fix

Use mutable collections for modification:

```scala
import scala.collection.mutable

// Wrong: immutable List
val list = List(1, 2, 3)
list.add(4) // UnsupportedOperationException

// Correct: mutable ArrayBuffer
val buffer = mutable.ArrayBuffer(1, 2, 3)
buffer.addOne(4) // Works
```

Transform immutable collections instead:

```scala
val list = List(1, 2, 3)
val newList = list :+ 4 // Returns new list with 4 appended
val filtered = list.filter(_ > 1)
```

Check collection type before modification:

```scala
def addItem(collection: scala.collection.mutable.Collection[Int], item: Int): Unit = {
  collection.addOne(item)
}
```

## Examples

```scala
object UnsupportedExample extends App {
  import java.util.Arrays
  val list = Arrays.asList(1, 2, 3) // Java unmodifiable
  list.add(4) // UnsupportedOperationException
}
```

## Related Errors

- [nosuchelement] — missing element access
- [matcherror] — pattern match fails

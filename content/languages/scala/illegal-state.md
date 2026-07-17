---
title: "IllegalStateException"
description: "An IllegalStateException occurs when a method is invoked at an illegal or inappropriate time for the object's state."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `IllegalStateException` is thrown when a method is called on an object that isn't in the appropriate state for that operation. This is common with iterators, streams, and objects with stateful lifecycles.

## Common Causes

- Using iterator after collection is modified
- Calling methods on disposed/closed resources
- Operating on objects in wrong lifecycle state
- Thread safety issues

## How to Fix

```scala
// WRONG: Modifying during iteration
val list = scala.collection.mutable.ListBuffer(1, 2, 3)
val iter = list.iterator
while (iter.hasNext) {
  val item = iter.next()
  if (item == 2) list -= item  // IllegalStateException
}

// CORRECT: Collect first, then modify
val list = scala.collection.mutable.ListBuffer(1, 2, 3)
val toRemove = list.filter(_ == 2)
list --= toRemove
```

```scala
// WRONG: Using closed stream
val stream = new java.io.FileInputStream("file.txt")
stream.close()
stream.read()  // ObjectDisposedException (similar to IllegalStateException)

// CORRECT: Check state before using
val stream = new java.io.FileInputStream("file.txt")
if (stream.available() > 0) {
  stream.read()
}
```

## Examples

```scala
// Example 1: Iterator invalidation
val set = scala.collection.mutable.Set(1, 2, 3)
val it = set.iterator
while (it.hasNext) {
  set.add(it.next() + 10)  // IllegalStateException
}

// Example 2: Stream already consumed
val s = Stream(1, 2, 3)
s.foreach(println)
s.foreach(println)  // works for Stream, but List would be empty

// Example 3: Future already completed
val promise = Promise[Int]()
promise.success(1)
promise.success(2)  // IllegalStateException
```

## Related Errors

- [UnsupportedOperationException](/languages/scala/unsupported-operation)
- [IndexOutOfBoundsException](/languages/scala/index-out-of-bound)

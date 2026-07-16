---
title: "UnsupportedOperationException"
description: "An UnsupportedOperationException occurs when an operation is not supported by the collection or object."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["unsupported", "operation", "collection", "unsupportedoperationexception"]
weight: 5
---

## What This Error Means

An `UnsupportedOperationException` is thrown when you try to perform an operation that isn't supported by the object. This is common with read-only collections, abstract types, or when calling methods on immutable structures.

## Common Causes

- Modifying immutable collections
- Calling methods on abstract types
- Unsupported operation for the collection type
- Platform-specific operations

## How to Fix

```scala
// WRONG: Modifying immutable collection
val list = List(1, 2, 3)
list += 4  // UnsupportedOperationException (or compile error)

// CORRECT: Create new collection
val list = List(1, 2, 3)
val newList = list :+ 4  // List(1, 2, 3, 4)
```

```scala
// WRONG: Calling unsupported method
val empty = Nil
empty.head  // UnsupportedOperationException

// CORRECT: Pattern match or use headOption
val empty = Nil
empty match {
  case head :: _ => println(head)
  case Nil => println("Empty list")
}
// Or
empty.headOption  // None
```

## Examples

```scala
// Example 1: head on empty list
List.empty.head  // UnsupportedOperationException

// Example 2: tail on empty list
List.empty.tail  // UnsupportedOperationException

// Example 3: readOnlyBuffer
val buffer = scala.collection.mutable.ListBuffer(1, 2, 3)
val readOnly = buffer.toList
readOnly.asInstanceOf[scala.collection.mutable.Buffer[Int]].append(4)
// UnsupportedOperationException
```

## Related Errors

- [IndexOutOfBoundsException](/languages/scala/index-out-of-bound)
- [IllegalStateException](/languages/scala/illegal-state)

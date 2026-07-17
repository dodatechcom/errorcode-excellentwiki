---
title: "IndexOutOfBoundsException"
description: "An IndexOutOfBoundsException occurs when accessing a collection with an index outside its valid range."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `IndexOutOfBoundsException` is thrown when you try to access an element of a collection using an index that is less than zero or greater than or equal to the collection's size.

## Common Causes

- Off-by-one errors in loops
- Using negative indices
- Accessing beyond collection length
- Incorrect index calculation

## How to Fix

```scala
// WRONG: Accessing beyond bounds
val arr = Array(1, 2, 3)
val x = arr(3)  // IndexOutOfBoundsException

// CORRECT: Use valid index
val arr = Array(1, 2, 3)
val x = arr(2)  // 3
```

```scala
// WRONG: No bounds check
def getElement(idx: Int, arr: Array[Int]): Int = arr(idx)

// CORRECT: Check bounds first
def getElement(idx: Int, arr: Array[Int]): Option[Int] =
  if (idx >= 0 && idx < arr.length) Some(arr(idx))
  else None
```

## Examples

```scala
// Example 1: Off by one
val list = List(10, 20, 30)
list(3)  // IndexOutOfBoundsException

// Example 2: Negative index
val arr = Array(1, 2, 3)
arr(-1)  // IndexOutOfBoundsException

// Example 3: Empty collection
val empty = List.empty[Int]
empty(0)  // IndexOutOfBoundsException
```

## Related Errors

- [UnsupportedOperationException](/languages/scala/unsupported-operation)
- [NullPointerException](/languages/scala/null-pointer6)

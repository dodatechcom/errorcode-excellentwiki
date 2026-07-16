---
title: "[Solution] Scala NoSuchElementException — Iterator or Collection Error"
description: "Fix Scala NoSuchElementException. Learn why calling .next() or .head on an empty collection throws this error and how to handle it safely."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nosuchelement", "iterator", "collection", "empty", "runtime"]
weight: 5
---

# NoSuchElementException — Iterator or Collection Error

A `NoSuchElementException` occurs when you try to access an element that doesn't exist — typically calling `.next()` on an exhausted iterator or `.head` / `.last` on an empty collection.

## Description

In Scala, `NoSuchElementException` is thrown when you request an element from a collection or iterator that has no more elements. This is a common runtime error when working with streams, iterators, or collection methods that assume non-empty input.

Common scenarios:

- **Iterator exhausted** — calling `.next()` after the iterator has been consumed.
- **Empty collection head/last** — calling `.head` or `.last` on an empty `List` or `Seq`.
- **Map key missing** — using `.apply` on a `Map` with a key that doesn't exist.
- **Empty option unwrap** — calling `.get` on a `None`.

## Common Causes

```scala
// Cause 1: Calling .next() on exhausted iterator
val it = List(1, 2, 3).iterator
it.next() // 1
it.next() // 2
it.next() // 3
it.next() // NoSuchElementException

// Cause 2: Head of empty list
val empty: List[Int] = List.empty
empty.head // NoSuchElementException

// Cause 3: Map key not found with .apply
val map = Map("a" -> 1, "b" -> 2)
map("c") // NoSuchElementException

// Cause 4: Option.get on None
val maybeValue: Option[Int] = None
maybeValue.get // NoSuchElementException
```

## How to Fix

### Fix 1: Check hasNext before calling next

```scala
// Wrong
val it = data.iterator
val first = it.next()

// Correct
val it = data.iterator
if (it.hasNext) {
  val first = it.next()
} else {
  println("Iterator is empty")
}
```

### Fix 2: Use headOption instead of head

```scala
// Wrong
val first = list.head

// Correct
val first = list.headOption
first match {
  case Some(value) => println(value)
  case None        => println("List is empty")
}
```

### Fix 3: Use getOrElse or getOrDefault for maps

```scala
// Wrong
val value = map("missing-key")

// Correct
val value = map.getOrElse("missing-key", defaultValue)

// Or with Option
val value: Option[Int] = map.get("missing-key")
```

### Fix 4: Use pattern matching instead of .get on Option

```scala
// Wrong
val value = maybeOption.get

// Correct
maybeOption match {
  case Some(value) => println(value)
  case None        => println("No value available")
}

// Or more concisely
val result = maybeOption.getOrElse(defaultValue)
```

## Examples

```scala
object NoSuchElementExample extends App {
  val emptyList: List[Int] = List.empty

  // This triggers: java.util.NoSuchElementException: next on empty iterator
  val first = emptyList.head
  println(first)
}
```

## Related Errors

- [match-error] — pattern match fails because no case handles the value.
- [IndexOutOfBoundsException] — index is out of range for a sequence.
- [UnsupportedOperationException] — calling an unsupported operation on a collection.

---
title: "[Solution] Scala NoSuchElementException - Map Access"
description: "Fix Scala NoSuchElementException. Learn why accessing a missing key in a Map throws this error."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nosuchelement", "map", "key", "access", "collection"]
weight: 5
---

## What This Error Means

A `NoSuchElementException` occurs when accessing a Map key that does not exist using `map(key)` instead of `map.get(key)`. It also occurs when calling `.head` on an empty collection or `.next()` on an exhausted iterator.

## Common Causes

- Accessing non-existent Map key with `map(key)` syntax
- Calling `.head` on an empty collection
- Using `.next()` on an empty iterator
- Missing key in configuration map

## How to Fix

Use `get` for safe map access:

```scala
val map = Map("a" -> 1, "b" -> 2)

// Wrong: throws NoSuchElementException
val value = map("c")

// Correct: returns Option
val value = map.get("c") // None
val value = map.getOrElse("c", 0) // 0
```

Check before accessing head:

```scala
val list = List.empty[Int]

// Wrong
val first = list.head // NoSuchElementException

// Correct
if (list.nonEmpty) {
  val first = list.head
}

// Or use headOption
val first = list.headOption // None
```

Handle missing keys gracefully:

```scala
def getValue(map: Map[String, Int], key: String): Int = {
  map.getOrElse(key, {
    println(s"Key '$key' not found, using default")
    0
  })
}
```

## Examples

```scala
object NosuchElementExample extends App {
  val scores = Map("Alice" -> 95, "Bob" -> 87)
  val charlieScore = scores("Charlie")
  // NoSuchElementException: key not found: Charlie
}
```

## Related Errors

- [matcherror] — pattern match fails on value
- [unsupportedoperation] — collection operation not supported

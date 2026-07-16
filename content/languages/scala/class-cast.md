---
title: "ClassCastException"
description: "A ClassCastException occurs when attempting to cast an object to a type it is not compatible with."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["cast", "class", "type", "classcastexception"]
weight: 5
---

## What This Error Means

A `ClassCastException` is thrown when you try to cast an object to a type that it isn't. This happens with explicit `asInstanceOf` calls or when the compiler infers the wrong type due to type erasure.

## Common Causes

- Explicit cast with `asInstanceOf` to wrong type
- Type erasure in generic collections
- Incorrect assumption about collection element types
- Java interop returning unexpected types

## How to Fix

```scala
// WRONG: Unsafe cast
val x: Any = "hello"
val n: Int = x.asInstanceOf[Int]  // ClassCastException

// CORRECT: Use pattern matching or isInstanceOf check
val x: Any = "hello"
x match {
  case n: Int => println(n)
  case s: String => println(s)
}
```

```scala
// WRONG: Type erasure issue
val list: List[Any] = List(1, "two", 3.0)
val strings: List[String] = list.asInstanceOf[List[String]]  // ClassCastException

// CORRECT: Use collect or filter
val strings: List[String] = list.collect { case s: String => s }
```

## Examples

```scala
// Example 1: Direct cast
val obj: Any = "hello"
val num = obj.asInstanceOf[Int]  // ClassCastException

// Example 2: Generic type erasure
val map = Map("a" -> List(1, 2))
val wrong = map.asInstanceOf[Map[String, List[String]]]  // may fail

// Example 3: Java interop
import java.util.Collections
val javaList = Collections.emptyList[String]()
val scalaList = javaList.asInstanceOf[List[String]]  // ClassCastException
```

## Related Errors

- [NullPointerException](/languages/scala/null-pointer6)
- [MatchError](/languages/scala/match-error4)

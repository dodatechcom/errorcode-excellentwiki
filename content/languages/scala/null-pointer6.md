---
title: "NullPointerException"
description: "A NullPointerException occurs when attempting to access a method or field on a null reference."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `NullPointerException` is thrown when you try to call a method or access a field on a null object reference. While Scala encourages using `Option` instead of null, interoperating with Java libraries can still produce null references.

## Common Causes

- Java methods returning null
- Uninitialized nullable variables
- Not handling Option properly
- Forgetting that a method might return null

## How to Fix

```scala
// WRONG: Not handling null from Java
val name: String = javaMethod()  // might be null
println(name.toUpperCase)  // NullPointerException

// CORRECT: Use Option or null check
val name: String = javaMethod()
Option(name) match {
  case Some(n) => println(n.toUpperCase)
  case None => println("No name")
}
```

```scala
// WRONG: Using get on None
val opt: Option[Int] = None
val value = opt.get  // NoSuchElementException

// CORRECT: Use getOrElse or pattern match
val opt: Option[Int] = None
val value = opt.getOrElse(0)  // 0
```

## Examples

```scala
// Example 1: Null from Java library
import java.util._
val list: ArrayList[String] = new ArrayList()
val item = list.get(0)  // null
println(item.length)    // NullPointerException

// Example 2: Uninitialized var
var s: String = null
println(s.toUpperCase)  // NullPointerException

// Example 3: Option.get on None
val map = Map("a" -> 1)
map.get("b").get  // NoSuchElementException
```

## Related Errors

- [ClassCastException](/languages/scala/class-cast)
- [MatchError](/languages/scala/match-error4)

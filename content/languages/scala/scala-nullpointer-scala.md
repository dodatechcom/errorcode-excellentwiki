---
title: "[Solution] Scala NullPointerException"
description: "Fix Scala NullPointerException. Learn about null handling, Option types, and safe references in Scala."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["null", "pointer", "option", "reference", "nullpointer"]
weight: 5
---

## What This Error Means

A `NullPointerException` occurs when attempting to dereference a null reference. While Scala discourages null usage, it can still arise from Java interop, uninitialized fields, or explicit null assignments.

## Common Causes

- Explicitly assigned `null` values
- Java interop returning null
- Uninitialized mutable fields
- Missing values in collections

## How to Fix

Use `Option` instead of null:

```scala
// Wrong
val name: String = null
val length = name.length // NullPointerException

// Correct
val name: Option[String] = None
val length = name.map(_.length).getOrElse(0)
```

Use pattern matching on Option:

```scala
def greet(name: Option[String]): String = name match {
  case Some(n) => s"Hello, $n"
  case None => "Hello, stranger"
}
```

Handle Java interop nulls:

```scala
val javaResult: String = javaMethod() // Might return null
val safeResult = Option(javaResult).getOrElse("default")
```

Use `getOrElse` for defaults:

```scala
val map = Map("a" -> 1)
val value = map.get("b").getOrElse(0)
```

## Examples

```scala
object NullExample extends App {
  val x: String = null
  println(x.length) // NullPointerException
}
```

## Related Errors

- [classcasterror] — invalid type cast
- [nosuchelement] — missing map key

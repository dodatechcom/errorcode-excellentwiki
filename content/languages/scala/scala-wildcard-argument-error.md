---
title: "[Solution] Scala Wildcard Argument Error"
description: "Fix Scala wildcard argument errors when using _ as type or value argument."
languages: ["scala"]
error-types: ["syntax-error"]
severities: ["error"]
---

Wildcard argument errors occur when _ is used incorrectly as type or value argument.

## Common Causes

- _ used where specific type needed
- Wildcard in pattern matching
- _ for ignored parameter
- Wildcard causing type inference failure

## How to Fix

### 1. Use _ for type parameters

```scala
val list: List[_] = List(1, 2, 3)  // List[Any]
```

### 2. Use _ for value ignore

```scala
List(1, 2, 3).foreach(_ => println("hello"))  // ignore element
List(1, 2, 3).map(_ * 2)  // use _ as parameter
```

## Examples

```scala
val numbers = List(1, 2, 3, 4, 5)

// Wildcard for ignore
numbers.foreach(_ => print("* "))
println()

// Wildcard as parameter
val doubled = numbers.map(_ * 2)
println(s"Doubled: $doubled")

// Wildcard in pattern
val maybeValue: Option[Int] = Some(42)
maybeValue match {
  case Some(_) => println("Has value")
  case None => println("Empty")
}
```

## Related Errors

- [Type error](/languages/scala/scala-type-mismatch)
- [Match error](/languages/scala/scala-match-error)
- [Compilation error](/languages/scala/scala-type-inference-error)

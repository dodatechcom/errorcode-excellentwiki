---
title: "[Solution] Scala ClassCastException Error"
description: "Fix Scala ClassCastException when runtime type casts fail. Handle type checking, pattern matching, and variance correctly."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `ClassCastException` occurs when you attempt to cast an object to a type it is not. This is a runtime error that happens with `asInstanceOf` or implicit conversions.

## Common Causes

- Incorrect `asInstanceOf` cast
- Type erasure in generics (e.g., `List[String]` at runtime)
- Mixing incompatible types in collections
- Incorrect variance in generic types

## How to Fix

```scala
// WRONG: Unsafe cast
val x: Any = 42
val s: String = x.asInstanceOf[String]  // ClassCastException

// CORRECT: Use pattern matching
x match {
  case s: String => println(s)
  case i: Int => println(i.toString)
  case _ => println("Unknown type")
}
```

```scala
// WRONG: Casting generic list (type erasure)
val list: List[Any] = List(1, 2, 3)
val strings: List[String] = list.asInstanceOf[List[String]]  // Compiles but fails!

// CORRECT: Use collect or map
val strings: List[String] = list.collect { case s: String => s }
```

```scala
// WRONG: Unsafe head on typed list
def firstElement(list: List[_]): String = list.head.asInstanceOf[String]

// CORRECT: Safe extraction
def firstElement(list: List[_]): Option[String] = list.headOption.collect {
  case s: String => s
}
```

## Examples

```scala
// Example 1: Safe type checking with match
def describe(x: Any): String = x match {
  case s: String => s"String: $s"
  case i: Int => s"Int: $i"
  case d: Double => s"Double: $d"
  case _ => s"Unknown: ${x.getClass}"
}

// Example 2: Using ClassTag for generic type checks
import scala.reflect.ClassTag
def isType[T: ClassTag](value: Any): Boolean = implicitly[ClassTag[T]].runtimeClass.isInstance(value)

// Example 3: Safe downcast
implicit class SafeCast(val value: Any) extends AnyVal {
  def safeCast[T]: Option[T] = value match {
    case t: T => Some(t)
    case _ => None
  }
}
```

## Related Errors

- [scala-matcherror]({{< relref "/languages/scala/scala-matcherror" >}}) — pattern match failed
- [scala-nullpointer]({{< relref "/languages/scala/scala-nullpointer" >}}) — null pointer
- [scala-type-mismatch]({{< relref "/languages/scala/scala-type-mismatch" >}}) — type mismatch

---
title: "[Solution] Scala ClassCastException"
description: "Fix Scala ClassCastException. Learn about invalid type casting and safe type checking in Scala."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `ClassCastException` occurs when attempting to cast an object to a type that is not compatible with its actual runtime type. This commonly happens with `asInstanceOf` calls on incorrect types.

## Common Causes

- Incorrect `asInstanceOf` type cast
- Type erasure hiding generic type mismatches
- Pattern match on wrong type
- Collection contains mixed types

## How to Fix

Use pattern matching instead of `asInstanceOf`:

```scala
// Wrong
val str: String = obj.asInstanceOf[String]

// Correct
obj match {
  case s: String => println(s"String: $s")
  case i: Int => println(s"Int: $i")
  case _ => println("Unknown type")
}
```

Use `isInstanceOf` check before casting:

```scala
if (obj.isInstanceOf[String]) {
  val str = obj.asInstanceOf[String]
  println(str)
}
```

Handle type erasure with ClassTag:

```scala
import scala.reflect.ClassTag

def process[T: ClassTag](list: List[T]): Unit = {
  list.foreach {
    case s: String => println(s"String: $s")
    case i: Int => println(s"Int: $i")
    case _ => println("Other")
  }
}
```

## Examples

```scala
object ClassCastExample extends App {
  val obj: Any = 42
  val str: String = obj.asInstanceOf[String]
  // ClassCastException: java.lang.Integer cannot be cast to java.lang.String
}
```

## Related Errors

- [matcherror] — pattern match fails on value
- [nullpointer] — null pointer exception

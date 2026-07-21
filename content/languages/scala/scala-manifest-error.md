---
title: "[Solution] Scala Using Manifest Error"
description: "Fix Scala manifest and ClassTag errors when runtime type information is needed."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Manifest/ClassTag errors occur when type information is erased and runtime type checks fail.

## Common Causes

- Type erasure losing runtime type info
- Missing ClassTag or TypeTag
- Pattern matching on generic types
- Array creation with generic type

## How to Fix

### 1. Use ClassTag for array creation

```scala
import scala.reflect.ClassTag

def createArray[T: ClassTag](size: Int): Array[T] = new Array[T](size)
```

### 2. Use TypeTag for type information

```scala
import scala.reflect.runtime.universe._

def typeName[T: TypeTag](x: T): String = typeOf[T].toString
```

## Examples

```scala
import scala.reflect.ClassTag

def filterByType[T: ClassTag](list: List[Any]): List[T] = {
  list.collect { case x: T => x }
}

val mixed: List[Any] = List(1, "hello", 2, "world", 3)
val ints = filterByType[Int](mixed)
println(s"Integers: $ints") // List(1, 2, 3)
```

## Related Errors

- [Type erasure error](/languages/scala/scala-type-erasure-error)
- [Class cast error](/languages/scala/scala-classcasterror-scala)
- [Type mismatch](/languages/scala/scala-type-mismatch)

---
title: "[Solution] Scala TypeErasureError - Brief Description"
description: "Fix generic type erasure errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1073
---

A type erasure error occurs when generic type parameters are erased at runtime.

## Common Causes

- Pattern matching on generic types
- Using `isInstanceOf[T]` with generic T
- Missing ClassTag

## How to Fix

Use ClassTag:

```scala
import scala.reflect.ClassTag
def isInstanceOf[T: ClassTag](value: Any): Boolean = {
  implicitly[ClassTag[T]].runtimeClass.isInstance(value)
}
```

Avoid pattern matching on generics:

```scala
def check[T: ClassTag](value: Any): Boolean = {
  implicitly[ClassTag[T]].runtimeClass.isInstance(value)
}
```

## Examples

```scala
import scala.reflect.ClassTag
def first[T: ClassTag](list: List[T]): Option[T] = list.headOption
```

## Related Errors

- [Scala TypeMismatch](/languages/scala/scala-type-mismatch)
- [Scala ClassCastException](/languages/scala/class-cast)

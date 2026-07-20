---
title: "[Solution] Scala ArrayListListError - Brief Description"
description: "Fix ArrayList vs List confusion."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1052
---

An ArrayList vs List error occurs when confusing Java ArrayList with Scala List.

## Common Causes

- Using `java.util.ArrayList` where `List` is expected
- Missing conversion between Java and Scala collections

## How to Fix

Use correct collection types:

```scala
val list: List[Int] = List(1, 2, 3)
```

Convert when interfacing:

```scala
import scala.jdk.CollectionConverters._
def processJavaList(javaList: java.util.List[Int]): List[Int] = {
  javaList.asScala.toList
}
```

## Examples

```scala
val javaList = new java.util.ArrayList[String]()
javaList.add("hello")
val scalaList = javaList.asScala.toList
val result = scalaList.map(_.toUpperCase)
```

## Related Errors

- [Scala JavaInteropError](/languages/scala/scala-java-interop-error)
- [Scala CollectionError](/languages/scala/scala-collection-error)

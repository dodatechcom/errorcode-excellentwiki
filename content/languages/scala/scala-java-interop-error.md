---
title: "[Solution] Scala JavaInteropError - Brief Description"
description: "Fix Scala-Java interop errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1051
---

A Java interop error occurs when calling Java code from Scala.

## Common Causes

- Java returning null where Scala expects non-null
- Missing SAM conversion
- Java generic type erasure

## How to Fix

Handle null returns:

```scala
import scala.jdk.OptionConverters._
val javaResult: java.lang.String = javaMethod()
val scalaOption: Option[String] = javaResult.toScala
```

Convert collections:

```scala
import scala.jdk.CollectionConverters._
val scalaList = List(1, 2, 3)
val javaList: java.util.List[Int] = scalaList.asJava
```

## Examples

```scala
import scala.jdk.CollectionConverters._
val javaMap = new java.util.HashMap[String, Int]()
javaMap.put("a", 1)
val scalaMap = javaMap.asScala.toMap
```

## Related Errors

- [Scala NullPointerError](/languages/scala/null-pointer6)
- [Scala ClassCastException](/languages/scala/class-cast)

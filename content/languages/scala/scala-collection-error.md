---
title: "[Solution] Scala Collection Conversion Error — How to Fix"
description: "Fix Scala collection conversion errors. Learn why Java and Scala collections differ and how to convert between them safely and efficiently."
languages: ["scala"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

Scala has its own rich collection library that is distinct from Java's `java.util` collections. When you try to pass a Scala collection where a Java collection is expected (or vice versa), the compiler raises a type mismatch error because the types are fundamentally different.

The most common cause is forgetting that `java.util.List` and `scala.collection.immutable.List` are completely different types with the same name. Importing `scala.collection.JavaConverters` or `scala.jdk.CollectionConverters` is necessary to bridge them.

Another frequent cause is mutability differences. Scala immutable collections cannot be directly assigned to Java mutable collection interfaces, and Scala mutable collections have different API contracts than their Java counterparts.

Collection wrapper methods like `.asJava` and `.asScala` create view types that may not match the expected Java collection type exactly. For example, `.asJava` on a `scala.collection.mutable.Buffer` returns a `java.util.List`, but `.asScala` on a `java.util.ArrayList` returns a `mutable.Buffer`, not an `immutable.List`.

Performance-related conversions can fail at runtime. Converting a lazy Scala collection to a Java collection forces evaluation, which may throw exceptions if the lazy computation fails.

Finally, generic type parameters on collections interact with variance. Java collections use raw types for generics while Scala enforces generic types, leading to type mismatches during conversion.

## Common Error Messages

```
Error: (line, col) type mismatch;
  found   : scala.collection.immutable.List[Int]
  required : java.util.List[Int]
```

```
Error: (line, col) value asJava is not a member of scala.collection.immutable.List[Int]
```

```
Error: (line, col) type mismatch;
  found   : java.util.ArrayList[String]
  required : scala.collection.mutable.Buffer[String]
```

```
Error: (line, col) implicit not found: Conversion[scala.collection.Map[K,V], java.util.Map[K,V]]
```

## How to Fix It

### Import the correct conversion bridge

```scala
// Scala 2.13+ and Scala 3
import scala.jdk.CollectionConverters._

val scalaList = List(1, 2, 3)
val javaList: java.util.List[Int] = scalaList.asJava
val backToScala: List[Int] = javaList.asScala.toList
```

### Use explicit conversion methods

```scala
import scala.jdk.CollectionConverters._

// Convert Java collection to Scala
val javaMap = new java.util.HashMap[String, Int]()
javaMap.put("one", 1)
val scalaMap: Map[String, Int] = javaMap.asScala.toMap

// Convert Scala collection to Java
val scalaSet = Set(1, 2, 3)
val javaSet: java.util.Set[Int] = scalaSet.asJava
```

### Use factory methods for precise collection types

```scala
import scala.jdk.CollectionConverters._

// Instead of asJava which returns a wrapper, create exact type
val scalaList = List(1, 2, 3)
val arrayList = new java.util.ArrayList[Int](scalaList.size)
scalaList.foreach(arrayList.add)

// Or use JavaConverters with specific target
val linkedList: java.util.LinkedList[Int] = 
  new java.util.LinkedList[Int](scalaList.asJava)
```

### Handle mutable vs immutable carefully

```scala
import scala.jdk.CollectionConverters._

// Scala immutable to Java — wrapper is read-only
val immutableMap = Map("a" -> 1, "b" -> 2)
val javaMapView: java.util.Map[String, Int] = immutableMap.asJava
// javaMapView.put("c", 3) // Would throw UnsupportedOperationException

// Scala mutable to Java — wrapper supports mutation
val mutableMap = scala.collection.mutable.Map("a" -> 1)
val javaMutableMap: java.util.Map[String, Int] = mutableMap.asJava
javaMutableMap.put("c", 3) // Works — modifies the underlying mutable map
```

### Use parallel conversion for large collections

```scala
import scala.jdk.CollectionConverters._

val largeScalaList = (1 to 1000000).toList
// Use .par for parallel conversion if needed
val javaList = largeScalaList.par.asJava.toList
```

## Common Scenarios

- Interoperating with a Java library that expects `java.util.List` or `java.util.Map`
- Reading data from a Java framework that returns Java collections into Scala code
- Converting between Scala mutable and immutable collections during refactoring

## Prevent It

- Always import `scala.jdk.CollectionConverters._` when working with Java interop
- Use `.toList`, `.toMap`, or `.toSet` after `.asScala` to get concrete Scala collection types
- Test collection conversions with the specific collection types you need, not just the generic interfaces

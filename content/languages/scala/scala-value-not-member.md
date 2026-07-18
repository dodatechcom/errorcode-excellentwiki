---
title: "[Solution] Scala Value Is Not a Member Of — Missing Member Access"
description: "Fix Scala value is not a member errors. Learn why member access fails on types, imports, path-dependent types, and type projections."
languages: ["scala"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A "value Y is not a member of X" compile error means the compiler cannot find the specified member (method, field, or type) on the given type. The error shows both the member name and the type it was accessed on, such as "value map is not a member of Int".

## Why It Happens

The most common cause is accessing a method or field that does not exist on the given type. For example, calling `.map` on an `Int` without converting it to a collection first, or calling `.head` on a type that does not have a `head` method.

Import errors are another frequent source. If you import a type but not the methods defined in its companion object or extension methods, the compiler will not find those methods.

Path-dependent types can cause this error when you try to access a member through a value that does not have the expected path. For instance, accessing `obj.InnerType` when `obj` is not the correct class that defines `InnerType`.

Type projection errors occur when using `#` syntax to access nested types incorrectly. The type may not exist in the specified scope.

Finally, missing implicit conversions that should add methods to a type will produce this error. If the implicit is not in scope, the method simply does not exist on the type.

## How to Fix It

### Check the type and its available members

```scala
// Wrong — Int has no map method
val x: Int = 42
x.map(_ + 1)

// Correct — convert to collection first
val x: Int = 42
List(x).map(_ + 1)
```

### Import extension methods and syntax

```scala
// Wrong — missing import
val result = "hello".capitalize

// Correct — import the syntax
import scala.util.matching.Regex
val pattern: Regex = "\\d+".r
```

### Verify path-dependent type access

```scala
class Database {
  class Connection
  def connect(): Connection = new Connection
}

val db = new Database
val conn: db.Connection = db.connect() // Works
val wrong: Database#Connection = db.connect() // Also works but different type
```

### Add missing imports for library methods

```scala
import scala.concurrent.duration._
val duration = 5.seconds

import scala.language.postfixOps
val result = List(1, 2, 3) map (_ * 2)
```

### Check for typos in member names

```scala
val list = List(1, 2, 3)
list.lenght // error: value lenght is not a member of List[Int]
list.length // correct
```

## Common Mistakes

- Forgetting that operators like `::` are methods on the collection, not the element
- Not importing syntax extensions from libraries like Cats or ScalaZ
- Confusing `#` type projection with `.` path-dependent access
- Assuming a parent type's methods are available on a type that does not inherit them
- Mixing up value members and type members on a class

## Related Pages

- [Scala Type Mismatch](/languages/scala/scala-type-mismatch/)
- [Scala Implicit Not Found](/languages/scala/scala-implicit-not-found/)
- [Scala Abstract Type](/languages/scala/scala-abstract-type/)

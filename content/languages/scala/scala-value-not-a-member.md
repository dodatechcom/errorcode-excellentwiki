---
title: "[Solution] Scala Value Is Not a Member Error"
description: "Fix Scala 'value X is not a member of Y' error when accessing non-existent members. Check imports, types, and available methods."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["value", "not-member", "member", "method", "import", "scala"]
weight: 5
---

## What This Error Means

The error `value X is not a member of Y` occurs when you try to access a method or field that doesn't exist on a type. This is a compile-time error indicating the type doesn't have the requested member.

## Common Causes

- Typo in method or field name
- Missing import for extension methods
- Wrong type (accessing members of wrong class)
- Method exists in different version of library
- Implicit conversions not available

## How to Fix

```scala
// WRONG: Typo in method name
val list = List(1, 2, 3)
list.lenght  // Error: value 'lenght' is not a member of List[Int]

// CORRECT: Use correct method name
list.length
```

```scala
// WRONG: Missing import for extension method
val result = "hello".reverse  // May need import

// CORRECT: Import required implicit conversions
import scala.collection.JavaConverters._
// Or for newer Scala:
import scala.jdk.CollectionConverters._
```

```scala
// WRONG: Accessing member on wrong type
case class Person(name: String, age: Int)
val person = Person("Alice", 30)
person.salary  // Error: value 'salary' is not a member of Person

// CORRECT: Check available members
// Use IDE auto-complete or documentation
person.name   // "Alice"
person.age    // 30
```

```scala
// WRONG: Accessing package member without import
val result = Duration.fromNanos(1000)  // Error without import

// CORRECT: Import the package
import scala.concurrent.duration._
val result = Duration.fromNanos(1000)
```

## Examples

```scala
// Example 1: Find available members
// In REPL, type: val x = List(1,2,3)
// Then type: x. and press Tab to see all members

// Example 2: Extension methods pattern
implicit class StringOps(s: String) {
  def isPalindrome: Boolean = s == s.reverse
}
"racecar".isPalindrome  // true

// Example 3: Check library documentation
// val r = scala.util.Random
// r.nextInt    // Available
// r.nextString // Check if available in your version
```

## Related Errors

- [scala-type-mismatch]({{< relref "/languages/scala/scala-type-mismatch" >}}) — type mismatch
- [scala-implicit-not-found]({{< relref "/languages/scala/scala-implicit-not-found" >}}) — implicit not found
- [scala-not-type]({{< relref "/languages/scala/scala-not-type" >}}) — not a type error

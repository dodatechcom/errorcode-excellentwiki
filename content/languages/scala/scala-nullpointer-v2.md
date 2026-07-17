---
title: "[Solution] Scala NullPointerException"
description: "Fix Scala NullPointerException when calling methods on null values. Use Option, safe calls, and null-checking patterns."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["null", "pointer", "option", "nullcheck", "jvm", "scala"]
weight: 5
---

## What This Error Means

A `NullPointerException` occurs when you call a method or access a field on a `null` reference. Although Scala encourages using `Option` instead of null, Java interop and legacy code can still produce nulls.

## Common Causes

- Interacting with Java libraries that return null
- Uninitialized `var` fields
- Using `null` directly instead of `Option`
- Forgetting to handle `Option` values

## How to Fix

```scala
// WRONG: Calling method on potentially null value
def process(s: String): Int = s.length  // NPE if s is null

// CORRECT: Use Option
def process(s: String): Int = Option(s).map(_.length).getOrElse(0)
```

```scala
// WRONG: Using null directly
var name: String = null
println(name.length)  // NullPointerException

// CORRECT: Use Option or default value
var name: Option[String] = None
println(name.map(_.length).getOrElse(0))
```

```scala
// WRONG: Java interop returning null
import java.util.Optional
val javaOpt: java.util.Optional[String] = getFromJava()
val value = javaOpt.get()  // May throw if empty

// CORRECT: Convert to Scala Option
val scalaOpt: Option[String] = Option(javaOpt.orElse(null))
val value = scalaOpt.getOrElse("default")
```

```scala
// WRONG: Pattern matching on null
val x: String = getSomething()
x match {
  case "hello" => "greeting"
  case s => s  // s could be null
}

// CORRECT: Handle null case
x match {
  case null => "empty"
  case "hello" => "greeting"
  case s => s
}
```

## Examples

```scala
// Example 1: Safe navigation operator alternative
implicit class SafeOps[T](val obj: T) extends AnyVal {
  def safeMap[U](f: T => U): Option[U] = Option(obj).map(f)
}
val result = null.safeMap(_.toString)  // None

// Example 2: Option from nullable Java method
val javaList = new java.util.ArrayList[String]()
javaList.add("hello")
// javaList.get(0) is fine, but javaList.get(1) returns null
val item: Option[String] = Option(javaList.get(1))

// Example 3: Require non-null with message
def process(name: String): String = {
  require(name != null, "Name cannot be null")
  require(name.nonEmpty, "Name cannot be empty")
  s"Hello, $name"
}
```

## Related Errors

- [scala-classcasterror]({{< relref "/languages/scala/scala-classcasterror" >}}) — invalid type cast
- [scala-matcherror]({{< relref "/languages/scala/scala-matcherror" >}}) — pattern match failed
- [scala-nosuchelement]({{< relref "/languages/scala/scala-nosuchelement" >}}) — key not found

---
title: "[Solution] Scala Match Guard Error"
description: "Fix Scala pattern match guard errors when using if conditions in match cases."
languages: ["scala"]
error-types: ["syntax-error"]
severities: ["error"]
---

Match guard errors occur when guards have incorrect syntax or when the guard condition causes type issues.

## Common Causes

- Wrong syntax for match guard
- Guard condition always true/false
- Guard with wrong variable scope
- Guard causing exhaustive match warning

## How to Fix

### 1. Use correct guard syntax

```scala
val x = 42
x match {
  case n if n > 0 => println("Positive")
  case n if n < 0 => println("Negative")
  case _ => println("Zero")
}
```

### 2. Use guards for complex conditions

```scala
def describe(x: Any): String = x match {
  case s: String if s.isEmpty => "Empty string"
  case s: String if s.length > 10 => "Long string"
  case s: String => s"String: $s"
  case n: Int if n > 0 => s"Positive int: $n"
  case n: Int => s"Int: $n"
  case _ => "Other"
}
```

## Examples

```scala
val age = 25

val category = age match {
  case a if a < 0 => "Invalid"
  case a if a < 13 => "Child"
  case a if a < 18 => "Teenager"
  case a if a < 65 => "Adult"
  case _ => "Senior"
}

println(s"Age $age is: $category")
```

## Related Errors

- [Match error](/languages/scala/scala-match-error)
- [Syntax error](/languages/scala/scala-type-inference-error)
- [Compilation error](/languages/scala/scala-type-inference-error)

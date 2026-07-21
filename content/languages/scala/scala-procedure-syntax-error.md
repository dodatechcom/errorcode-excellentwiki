---
title: "[Solution] Scala Procedure Syntax Error"
description: "Fix Scala procedure syntax errors when defining methods without equals sign."
languages: ["scala"]
error-types: ["syntax-error"]
severities: ["error"]
---

Procedure syntax errors occur when the deprecated procedure syntax is used or when methods are defined without proper return type.

## Common Causes

- Using deprecated procedure syntax (def foo() { ... })
- Missing equals sign for value methods
- Procedure syntax confusing with block expressions
- Implicit Unit return type issues

## How to Fix

### 1. Use proper method syntax

```scala
// WRONG: Deprecated procedure syntax
// def greet() { println("Hello") }

// CORRECT
def greet(): Unit = println("Hello")
```

### 2. Always use equals sign

```scala
// WRONG: Procedure syntax
// def compute() { 42 }

// CORRECT
def compute(): Int = 42
```

## Examples

```scala
class Greeter {
  def greet(name: String): Unit = {
    println(s"Hello, $name!")
  }

  def farewell(name: String): String = {
    s"Goodbye, $name!"
  }
}

val g = new Greeter()
g.greet("Alice")
println(g.farewell("Bob"))
```

## Related Errors

- [Syntax error](/languages/scala/scala-type-inference-error)
- [Compilation error](/languages/scala/scala-type-inference-error)
- [Match error](/languages/scala/scala-match-error)

---
title: "[Solution] Scala Context Function Error"
description: "Fix Scala 3 context function errors when using ?=> syntax for implicit function types."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Context function errors occur when context functions are used incorrectly or when the context parameter is not properly provided.

## Common Causes

- Context function type not provided implicit
- Wrong syntax for context function
- Context function capturing wrong scope
- Missing context function in type inference

## How to Fix

### 1. Use correct context function syntax

```scala
type Logging[T] ?=> T

def greet(name: String): Logging[String] = {
  println(s"Hello, $name")
  name
}
```

### 2. Provide context implicitly

```scala
trait Context {
  def env: String
}

type WithContext[T] ?=> Context ?=> T

def run(): WithContext[String] = {
  summon[Context].env
}
```

## Examples

```scala
trait Theme {
  def color: String
}

type Themed[T] ?=> Theme ?=> T

def styledText(text: String): Themed[String] = {
  val theme = summon[Theme]
  s"[${theme.color}] $text"
}

given darkTheme: Theme with { val color = "dark" }

val result = styledText("Hello")
println(result)
```

## Related Errors

- [Given using error](/languages/scala/scala-given-using-error)
- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)

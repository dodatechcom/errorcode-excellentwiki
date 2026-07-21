---
title: "[Solution] Scala Braceless Syntax Error"
description: "Fix Scala 3 braceless syntax errors when using indentation-based syntax instead of curly braces."
languages: ["scala"]
error-types: ["syntax-error"]
severities: ["error"]
---

Braceless syntax errors occur when indentation-based syntax is used incorrectly or when mixing brace and braceless styles.

## Common Causes

- Inconsistent indentation in braceless blocks
- Mixing brace and braceless syntax
- Missing indentation for braceless if/else
- Braceless syntax with wrong operator

## How to Fix

### 1. Use consistent indentation

```scala
def process(x: Int): Int =
  if x > 0 then
    x * 2
  else
    -x
```

### 2. Do not mix styles

```scala
// WRONG: Mixing styles
def bad() =
  if true then {
    println("yes")
  }

// CORRECT: Consistent braceless
def good() =
  if true then
    println("yes")
```

## Examples

```scala
def fibonacci(n: Int): BigInt =
  if n <= 1 then
    BigInt(n)
  else
    fibonacci(n - 1) + fibonacci(n - 2)

@main def run() =
  val result = fibonacci(10)
  println(s"Fibonacci(10) = $result")
```

## Related Errors

- [Syntax error](/languages/scala/scala-type-inference-error)
- [Compilation error](/languages/scala/scala-type-inference-error)
- [Match error](/languages/scala/scala-match-error)

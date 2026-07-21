---
title: "[Solution] Scala SAM Type Error"
description: "Fix Scala Single Abstract Method (SAM) type errors when using functional interface conversions."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

SAM type errors occur when attempting to use SAM conversion on types that do not have a single abstract method.

## Common Causes

- Type has more than one abstract method
- SAM conversion not enabled
- Wrong lambda syntax for SAM type
- SAM conversion on Java interface with default methods

## How to Fix

### 1. Ensure type has single abstract method

```scala
trait Processor {
  def process(input: String): String
}

val p: Processor = (s: String) => s.toUpperCase  // SAM conversion OK
```

### 2. Use SAM annotation if needed

```scala
import scala.scalajs.js.annotation.JSExportTopLevel

trait Callback {
  def run(): Unit
}

val cb: Callback = () => println("callback")
```

## Examples

```scala
trait Validator {
  def isValid(s: String): Boolean
}

val emailValidator: Validator = (s: String) => s.contains("@")
println(emailValidator.isValid("test@example.com"))
println(emailValidator.isValid("invalid"))
```

## Related Errors

- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
- [Match error](/languages/scala/scala-match-error)

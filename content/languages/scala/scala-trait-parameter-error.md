---
title: "[Solution] Scala Trait Parameter Error"
description: "Fix Scala 3 trait parameter errors when traits have constructor parameters."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Trait parameter errors occur when traits with constructor parameters are used incorrectly or when they conflict with class inheritance.

## Common Causes

- Trait with parameters cannot extend another trait with parameters
- Missing argument when mixing in trait
- Trait parameter used before initialization
- Conflict between trait and class parameters

## How to Fix

### 1. Provide trait parameters at mixin

```scala
trait Logger(prefix: String) {
  def log(msg: String): Unit = println(s"[$prefix] $msg")
}

class App extends Logger("APP") {
  def start(): Unit = log("Starting")
}
```

### 2. Use trait parameters correctly

```scala
trait Validator(pattern: String) {
  def validate(input: String): Boolean = input.matches(pattern)
}

class EmailValidator extends Validator(""".*@.*\..*""")
```

## Examples

```scala
trait Named(name: String) {
  def greet(): String = s"Hello, $name"
}

trait Aged(age: Int) {
  def describe(): String = s"Age: $age"
}

class Person(n: String, a: Int) extends Named(n) with Aged(a)

val p = new Person("Alice", 30)
println(p.greet())
println(p.describe())
```

## Related Errors

- [Type error](/languages/scala/scala-type-mismatch)
- [Class cast error](/languages/scala/scala-classcast-error)
- [Compilation error](/languages/scala/scala-type-inference-error)

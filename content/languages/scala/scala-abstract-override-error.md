---
title: "[Solution] Scala Abstract Override Error"
description: "Fix Scala abstract override errors when using super in trait linearization."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Abstract override errors occur when super is used incorrectly in traits or when the linearization chain is broken.

## Common Causes

- super call in trait without concrete implementation
- Wrong linearization order
- Missing abstract override keyword
- Circular trait inheritance

## How to Fix

### 1. Use abstract override correctly

```scala
trait Logger {
  def log(msg: String): Unit
}

trait ConsoleLogger extends Logger {
  override def log(msg: String): Unit = println(msg)
}

trait TimestampLogger extends Logger {
  abstract override def log(msg: String): Unit = {
    super.log(s"[${System.currentTimeMillis()}] $msg")
  }
}
```

### 2. Ensure proper linearization

```scala
class App extends TimestampLogger with ConsoleLogger {
  // super goes to TimestampLogger, then ConsoleLogger
}
```

## Examples

```scala
trait Base {
  def greet(): String = "Hello"
}

trait Upper extends Base {
  abstract override def greet(): String = super.greet().toUpperCase
}

trait Exclaim extends Base {
  abstract override def greet(): String = super.greet() + "!"
}

class MyApp extends Upper with Exclaim

val app = new MyApp()
println(app.greet()) // "HELLO!"
```

## Related Errors

- [Trait parameter error](/languages/scala/scala-trait-parameter-error)
- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)

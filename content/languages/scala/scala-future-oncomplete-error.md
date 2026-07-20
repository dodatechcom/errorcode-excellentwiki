---
title: "[Solution] Scala FutureOnCompleteError - Brief Description"
description: "Fix Future.onComplete errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1056
---

A Future.onComplete error occurs when callbacks throw or access shared state unsafely.

## Common Causes

- Exception in callback
- Callback blocking on IO
- Forgetting ExecutionContext

## How to Fix

Handle exceptions:

```scala
future.onComplete {
  case Success(value) => try { processResult(value) } catch { case e: Exception => log.error("Callback failed", e) }
  case Failure(e) => log.error("Future failed", e)
}
```

Use `foreach` for simple effects:

```scala
future.foreach(value => println(s"Got: $value"))
```

## Examples

```scala
import scala.util.{Success, Failure}
val f = Future { computeAnswer() }
f.onComplete {
  case Success(answer) => println(s"Answer: $answer")
  case Failure(ex) => println(s"Error: ${ex.getMessage}")
}
```

## Related Errors

- [Scala FutureMapError](/languages/scala/scala-future-map-error)
- [Scala FutureFailure](/languages/scala/scala-future-failure)

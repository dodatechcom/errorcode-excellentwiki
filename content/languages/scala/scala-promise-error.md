---
title: "[Solution] Scala Promise Error"
description: "Fix Scala Promise errors when creating and completing promises for asynchronous computation."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
---

Promise errors occur when a Promise is completed more than once or when the Promise is not properly connected to a Future.

## Common Causes

- Completing a Promise more than once
- Forgetting to complete a Promise
- Promise completed with failure not handled
- Mixing up Promise and Future semantics

## How to Fix

### 1. Complete Promise exactly once

```scala
import scala.concurrent.Promise

val p = Promise[Int]()
val f: Future[Int] = p.future
p.success(42)  // complete once
// p.success(100)  // ERROR: already completed
```

### 2. Handle both success and failure

```scala
val p = Promise[String]()
try {
  p.success("done")
} catch {
  case _: IllegalStateException => println("Already completed")
}
```

## Examples

```scala
import scala.concurrent.{Promise, Future}
import scala.util.{Success, Failure}
import scala.concurrent.ExecutionContext.Implicits.global

val p = Promise[Int]()
val f: Future[Int] = p.future

f.onComplete {
  case Success(v) => println(s"Got: $v")
  case Failure(e) => println(s"Error: ${e.getMessage}")
}

p.success(100)
Thread.sleep(1000)
```

## Related Errors

- [Future failure error](/languages/scala/scala-future-failure)
- [Execution context error](/languages/scala/scala-execution-context-error)
- [Runtime error](/languages/scala/scala-out-of-memory)

---
title: "[Solution] Scala Concurrency Execution Context Error"
description: "Fix Scala ExecutionContext errors when using concurrent execution contexts for futures and promises."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
---

ExecutionContext errors occur when the implicit execution context is not available or when the wrong context is used for concurrent operations.

## Common Causes

- Missing implicit ExecutionContext
- Using global context when custom context needed
- ExecutionContext thread pool exhausted
- Blocking on ExecutionContext threads

## How to Fix

### 1. Import appropriate ExecutionContext

```scala
import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

val f: Future[Int] = Future { 1 + 1 }
```

### 2. Create custom ExecutionContext

```scala
import java.util.concurrent.Executors
import scala.concurrent.ExecutionContext

val pool = Executors.newFixedThreadPool(10)
implicit val ec: ExecutionContext = ExecutionContext.fromExecutor(pool)
```

## Examples

```scala
import scala.concurrent.{Future, ExecutionContext}
import scala.concurrent.ExecutionContext.Implicits.global
import scala.util.{Success, Failure}

val futureResult: Future[Int] = Future {
  Thread.sleep(1000)
  42
}

futureResult.onComplete {
  case Success(value) => println(s"Result: $value")
  case Failure(ex) => println(s"Failed: ${ex.getMessage}")
}
Thread.sleep(2000)
```

## Related Errors

- [Future failure error](/languages/scala/scala-future-failure)
- [Thread pool error](/languages/scala/scala-concurrentmodification)
- [Runtime error](/languages/scala/scala-out-of-memory)

---
title: "[Solution] Scala AwaitResultError - Brief Description"
description: "Fix Await.result errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1057
---

An Await.result error occurs when blocking on a Future that fails or times out.

## Common Causes

- Timeout exceeded
- Deadlock from shared thread pool
- Using Await in actors

## How to Fix

Use appropriate timeouts:

```scala
import scala.concurrent.Await
import scala.concurrent.duration._
val result = Await.result(future, 5.seconds)
```

Prefer non-blocking:

```scala
future.map(result => process(result))
```

## Examples

```scala
import scala.concurrent.Await
import scala.concurrent.duration._
val result = Await.result(Future { expensiveComputation() }, 30.seconds)
```

## Related Errors

- [Scala FutureMapError](/languages/scala/scala-future-map-error)
- [Scala AkkaTimeout](/languages/scala/scala-akka-timeout)

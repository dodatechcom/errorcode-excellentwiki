---
title: "[Solution] Scala FutureMapError - Brief Description"
description: "Fix Scala Future.map/flatMap errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1055
---

A Future.map/flatMap error occurs when the transformation throws or Future fails.

## Common Causes

- Exception in map/flatMap callback
- Missing implicit ExecutionContext
- Future failure not handled

## How to Fix

Provide ExecutionContext:

```scala
import scala.concurrent.ExecutionContext.Implicits.global
val result = Future(42).map(_ * 2)
```

Handle failures:

```scala
val result = Future { riskyOperation() }.recover {
  case e: Exception => fallbackValue
}
```

## Examples

```scala
val result = for {
  user <- getUser(1)
  orders <- getOrders(user)
  total <- calculateTotal(orders)
} yield total
```

## Related Errors

- [Scala FutureFailure](/languages/scala/scala-future-failure)
- [Scala AwaitResult](/languages/scala/scala-await-result-error)

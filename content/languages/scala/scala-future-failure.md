---
title: "[Solution] Scala Future Completed With Exception — Async Error Handling"
description: "Fix Scala Future failures with proper exception handling. Learn recover, fallbackTo, and error handling patterns for concurrent code."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `Future` completed with an exception means the asynchronous computation failed. The exception is captured inside the `Future` and propagated to any callback (`.map`, `.flatMap`, `.onComplete`) or when you call `.await` or `.result` to block for the value. The underlying exception is wrapped in a `Future.failure`.

## Why It Happens

The most common cause is an unhandled exception inside the `Future` body. If the code block passed to `Future { ... }` throws any exception, the `Future` is completed with that exception rather than a value.

Another frequent cause is calling `.get` or `.result` on a failed `Future`, which re-throws the original exception. This is especially common when using blocking database calls or HTTP requests inside a `Future`.

Timeout errors from Akka or other concurrency frameworks also complete `Future`s with exceptions. When a `Future` does not complete within the specified time, it is failed with a `TimeoutException`.

Network failures, file I/O errors, and database connection issues are all common sources of exceptions inside `Future` blocks.

Finally, uncaught exceptions in `.map` or `.flatMap` callbacks are captured and wrapped in the resulting `Future`, which can be surprising if you are not expecting the callback to fail.

## How to Fix It

### Handle exceptions inside the Future block

```scala
import scala.concurrent.Future
import scala.concurrent.ExecutionContext.Implicits.global

// Wrong — exception kills the Future
val result = Future {
  riskyOperation()
}

// Correct — catch and convert to Either
val result: Future[Either[String, Result]] = Future {
  Right(riskyOperation())
}.recover {
  case e: Exception => Left(e.getMessage)
}
```

### Use recover and recoverWith

```scala
val result = fetchData().recover {
  case _: TimeoutException => defaultData
  case e: IOException      => fallbackData
}

val result = fetchData().recoverWith {
  case _: TimeoutException => retryFetch()
}
```

### Use fallbackTo for alternative sources

```scala
val primary   = fetchFromPrimary()
val secondary = fetchFromSecondary()

val result = primary.fallbackTo(secondary)
```

### Pattern match on Future results

```scala
import scala.util.{Success, Failure}

result.onComplete {
  case Success(value)    => println(s"Got: $value")
  case Failure(exception) => println(s"Failed: ${exception.getMessage}")
}
```

### Use Try for synchronous error handling

```scala
import scala.util.{Try, Success, Failure}

val result = Try {
  riskyOperation()
}

result match {
  case Success(value) => println(value)
  case Failure(e)     => println(s"Error: ${e.getMessage}")
}
```

## Common Mistakes

- Not providing a recovery handler for Futures that can fail
- Blocking on a Future with `.result` or `.await` instead of using callbacks
- Swallowing exceptions with `.recover { case _ => }` without logging
- Forgetting that `.map` callbacks can also throw exceptions
- Not using `ExecutionContext` properly, leading to exceptions being swallowed

## Related Pages

- [Scala Akka Timeout](/languages/scala/scala-akka-timeout/)
- [Scala OutOfMemoryError](/languages/scala/scala-out-of-memory/)
- [Scala StackOverflowError](/languages/scala/stack-overflow3/)

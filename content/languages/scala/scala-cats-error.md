---
title: "[Solution] Scala Cats MonadError — Unhandled Effect Failure"
description: "Fix Cats MonadError and ApplicativeError failures. Learn error handling with Either, MonadError, and effect types in Cats."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A Cats `MonadError` failure occurs when an effectful computation raises an error that is not handled by the error channel. In Cats, `MonadError[F, E]` abstracts over error handling in effect types like `Either`, `Try`, and `IO`. When an error is raised and not recovered, it propagates as an unhandled failure.

## Why It Happens

The most common cause is raising an error with `MonadError[F, E].raiseError` or `.asLeft` without providing a corresponding `.recover` or `.handleErrorWith` handler. The error is embedded in the effect but never consumed.

Another frequent cause is using `.getOrRaise` or `.rethrow` on an `Either` that contains `Left` without handling the `Left` case. Cats operations that convert between error types can silently propagate errors if the calling code does not handle them.

Using `ApplicativeError` with `IO` or `ZIO` without a `try-catch` or `attempt` wrapper means any thrown exception becomes a defect rather than a typed error. This is especially common when integrating Java libraries that throw checked exceptions.

Finally, forgetting to import `cats.implicits._` or `cats.syntax.all._` can cause extension methods like `.attempt` or `.handleErrorWith` to not be available, leading to compiler errors or accidental use of unsafe operations.

## How to Fix It

### Use attempt to capture errors as values

```scala
import cats.implicits._

val result: IO[Either[Throwable, Result]] = IO {
  riskyOperation()
}.attempt
```

### Handle errors with handleErrorWith

```scala
import cats.implicits._

val safeResult: IO[Result] = riskyIO.handleErrorWith {
  case e: TimeoutException => IO.pure(defaultResult)
  case e: IOException      => retryIO()
}
```

### Use ApplicativeError for typed error handling

```scala
import cats.{ApplicativeError, MonadError}

def process[F[_], E](input: String)(implicit F: MonadError[F, E]): F[Result] =
  if (input.isEmpty) F.raiseError(invalidInputError)
  else F.pure(parseResult(input))
```

### Convert thrown exceptions to typed errors

```scala
import cats.implicits._

val result: IO[Either[AppError, Data]] = IO {
  javaLibrary.call()
}.attempt.map {
  case Left(e: IllegalArgumentException) => Left(InvalidInput(e.getMessage))
  case Left(e)                           => Left(UnexpectedError(e.getMessage))
  case Right(data)                       => Right(data)
}
```

### Use recover for partial error handling

```scala
val result = computation.recover {
  case _: NonFatal(e) => fallbackValue
}
```

## Common Mistakes

- Using `.unsafeRunSync()` without handling the error channel first
- Mixing Cats error handling with raw `try-catch` blocks
- Forgetting that `IO.raiseError` short-cuits the entire for-comprehension
- Not distinguishing between expected errors (`E`) and defects (`Throwable`)
- Using `ApplicativeError` methods without the correct import for extension methods

## Related Pages

- [Scala ZIO Error](/languages/scala/scala-zio-error/)
- [Scala Future Failure](/languages/scala/scala-future-failure/)
- [Scala Implicit Not Found](/languages/scala/scala-implicit-not-found/)

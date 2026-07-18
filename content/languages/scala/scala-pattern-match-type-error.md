---
title: "[Solution] Scala Pattern Match Type Exhaustiveness — How to Fix"
description: "Fix Scala pattern match exhaustiveness warnings and errors. Learn how to handle all cases in match expressions and avoid MatchError at runtime."
languages: ["scala"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

Scala's pattern matching is exhaustive at compile time when using sealed hierarchies. When a `match` expression does not cover all possible cases of a sealed trait or class, the compiler raises a warning or error depending on compiler settings.

The most common cause is forgetting to add a wildcard case (`case _ =>`) at the end of a match expression. While this suppresses the exhaustiveness warning, it is often better to handle each case explicitly.

Another frequent cause is a sealed hierarchy that has been extended in a different file or module. If you add a new case class extending a sealed trait, all existing match expressions that reference that trait must be updated.

Type-based pattern matching with extractors can miss cases. When you use custom extractors (like `unapply` methods), the compiler may not be able to verify exhaustiveness because it does not know what the extractor can return.

Match expressions on values of type `Any` or `AnyRef` cannot be exhaustive because there are infinitely many possible types. The compiler warns about this.

Finally, nested pattern matches can create non-exhaustive combinations even when each individual match appears complete. The compiler only checks exhaustiveness at the top level of each match expression.

## Common Error Messages

```
Warning: (line, col) match may not be exhaustive.
  It would fail on the following inputs: Red, Blue
```

```
Error: (line, col) match may not be exhaustive. It would fail on: Nil
```

```
Warning: (line, col) selector value is unchecked
```

```
Error: (line, col) pattern match type error: missing case for type Nothing
```

## How to Fix It

### Add cases for all variants of a sealed hierarchy

```scala
sealed trait Color
case object Red extends Color
case object Green extends Color
case object Blue extends Color

def describe(c: Color): String = c match {
  case Red   => "red"
  case Green => "green"
  case Blue  => "blue"
  // No wildcard needed — compiler knows all cases are covered
}
```

### Use a wildcard fallback for extensible hierarchies

```scala
sealed trait Result
case class Success(value: String) extends Result
case class Failure(error: String) extends Result

def process(r: Result): String = r match {
  case Success(v) => s"Got: $v"
  case Failure(e) => s"Error: $e"
  case _          => "Unknown result" // Safety net for future cases
}
```

### Handle nested patterns exhaustively

```scala
sealed trait Tree
case class Leaf(value: Int) extends Tree
case class Node(left: Tree, right: Tree) extends Tree

def sum(tree: Tree): Int = tree match {
  case Leaf(v)         => v
  case Node(l, r)      => sum(l) + sum(r)
  // Both cases covered — exhaustiveness verified
}
```

### Use @unchecked to suppress warnings intentionally

```scala
import scala.annotation.unchecked.uncheckedStable

// When you are certain the match is complete but the compiler cannot verify
@unchecked def process(result: Result): String = result match {
  case Success(v) => v
  case Failure(e) => e
}
```

### Extract values in match patterns

```scala
sealed trait Config
case class DatabaseConfig(host: String, port: Int) extends Config
case class CacheConfig(ttl: Int) extends Config

def applyConfig(config: Config): Unit = config match {
  case DatabaseConfig(host, port) => connect(host, port)
  case CacheConfig(ttl)           => setTtl(ttl)
  // Exhaustive — both cases handled with extraction
}
```

## Common Scenarios

- Adding a new variant to a sealed trait and forgetting to update all pattern matches
- Working with a match expression on a type that the compiler cannot determine is sealed
- Using extractors that do not guarantee exhaustiveness checking

## Prevent It

- Always use sealed hierarchies for types that will be pattern matched
- Enable `-Wconf:cat=match-exhaustive:w` to treat exhaustiveness warnings as errors
- Review all pattern matches when adding new variants to a sealed hierarchy

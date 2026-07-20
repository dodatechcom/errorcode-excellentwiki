---
title: "[Solution] Scala WartRemoverError - Brief Description"
description: "Fix WartRemover lint errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1071
---

A wartremover error occurs when code violates configured wart rules.

## Common Causes

- Using null
- Using mutable collections
- Using var
- AsInstanceOf usage

## How to Fix

Fix flagged warts:

```scala
// WRONG: NullWart
def find(id: Int): User = if (exists(id)) getUser(id) else null

// CORRECT: Return Option
def find(id: Int): Option[User] = if (exists(id)) Some(getUser(id)) else None
```

Configure:

```scala
wartremoverErrors ++= Warts.Unused
wartremoverWarnings ++= Warts.Any
```

## Examples

```scala
wartremoverErrors ++= Seq(Wart.Null, Wart.Return, Wart.Throw)
```

## Related Errors

- [Scala ScoverageError](/languages/scala/scala-scoverage-error)
- [Scala ScaladocError](/languages/scala/scala-scaladoc-error)

---
title: "[Solution] Scala ViewBoundError - Brief Description"
description: "Fix Scala view bound errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1048
---

A view bound error occurs when using deprecated `<%` syntax in Scala 2.13+.

## Common Causes

- Using deprecated view bound syntax
- Missing implicit conversion

## How to Fix

Replace view bounds with context bounds:

```scala
// DEPRECATED
def sorted[T <% Ordered[T]](list: List[T]): List[T] = list.sorted

// CORRECT
def sorted[T: Ordering](list: List[T]): List[T] = list.sorted
```

## Examples

```scala
def findMax[T: Ordering](list: List[T]): T = list.max
def findMin[T](list: List[T])(implicit ord: Ordering[T]): T = list.min(ord)
```

## Related Errors

- [Scala ContextBoundError](/languages/scala/scala-context-bound-error)
- [Scala ImplicitNotFound](/languages/scala/scala-implicit-not-found)

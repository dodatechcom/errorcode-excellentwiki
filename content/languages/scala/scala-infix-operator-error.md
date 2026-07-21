---
title: "[Solution] Scala Infix Operator Error"
description: "Fix Scala 3 infix operator errors when using operator-style method calls."
languages: ["scala"]
error-types: ["syntax-error"]
severities: ["error"]
---

Infix operator errors occur when operators are used with wrong precedence or when the infix notation conflicts with other syntax.

## Common Causes

- Wrong operator precedence
- Infix operator with more than one argument
- Infix operator name conflict
- Using infix on side-effecting methods

## How to Fix

### 1. Understand operator precedence

```scala
val a = 1 + 2 * 3  // 7, not 9
val b = (1 + 2) * 3  // 9
```

### 2. Use infix correctly

```scala
// WRONG: Infix on multi-argument method
// list map (x => x * 2) toList

// CORRECT
list.map(x => x * 2).toList
```

## Examples

```scala
case class Money(amount: Double) {
  def +(other: Money): Money = Money(amount + other.amount)
  def *(times: Int): Money = Money(amount * times)
}

val price = Money(10.0)
val total = price * 3 + Money(5.0)
println(s"Total: $$${total.amount}")
```

## Related Errors

- [Syntax error](/languages/scala/scala-type-inference-error)
- [Compilation error](/languages/scala/scala-type-inference-error)
- [Match error](/languages/scala/scala-match-error)

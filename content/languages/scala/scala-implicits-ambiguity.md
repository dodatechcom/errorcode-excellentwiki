---
title: "[Solution] Scala Ambiguous Implicit Resolution — How to Fix"
description: "Fix Scala ambiguous implicit resolution errors. Learn why the compiler finds multiple implicits and how to disambiguate them effectively."
languages: ["scala"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

Scala's implicit resolution mechanism searches for matching implicit values in a deterministic order. When the compiler finds two or more implicits of the same type that are equally specific, it cannot decide which one to use and raises an ambiguous implicit resolution error.

The most common cause is defining implicit values in both a companion object and an import that have the same type. When both are equally visible to the compiler, neither takes priority.

Another frequent cause is having implicit definitions in two different traits that are mixed into the same class. If both traits define an implicit of the same type, mixing them together creates ambiguity.

Implicit conversions from different packages or objects that target the same type also cause ambiguity. When two conversion implicits apply to the same expression, the compiler reports the conflict.

Type class instances defined in overlapping scopes (such as an imported instance and a locally defined one) create this error. The local scope usually wins, but when both are at the same scope level, ambiguity results.

Finally, implicit chains that resolve to the same type through different paths can create diamond-shaped ambiguity where the compiler finds two routes to the same implicit type.

## Common Error Messages

```
Error: (line, col) ambiguous implicit values:
  both value intOrdering in object Ordering of type => Ordering[Int]
  and value customOrdering in object MyOrderings of type => Ordering[Int]
  match expected type Ordering[Int]
```

```
Error: (line, col) implicit ambiguity;
  most specific instance is implicit value jsonCodecInt in object Codecs
  but there is also implicit value intCodec in object DefaultCodecs
```

```
Error: (line, col) diverging implicit expansion for type Show[A]
  starting with method showList in object ShowInstances
```

```
Error: (line, col) ambiguous implicit values: conversionA and conversionB both match type A => B
```

## How to Fix It

### Use explicit priority through trait linearization

```scala
trait LowPriorityImplicits {
  implicit val fallbackOrdering: Ordering[CustomType] = ???
}

trait HighPriorityImplicits extends LowPriorityImplicits {
  implicit val preferredOrdering: Ordering[CustomType] = ???
}

object Implicits extends HighPriorityImplicits
// preferredOrdering takes priority due to linearization
```

### Import implicits selectively to avoid conflicts

```scala
import Codecs.intCodec // Only import what you need
// Instead of import Codecs._ which brings in everything
```

### Use named implicits for clarity

```scala
trait JsonCodec[A] {
  def encode(a: A): String
  def decode(s: String): Either[String, A]
}

given intCodec: JsonCodec[Int] = ???
given stringCodec: JsonCodec[String] = ???

// Use summon by name to disambiguate
val codec = summon[JsonCodec[Int]]
```

### Move conflicting implicits to separate objects

```scala
object StandardImplicits {
  implicit val standardShow: Show[User] = ???
}

object CustomImplicits {
  implicit val customShow: Show[User] = ???
}

// Import only one at a time
import CustomImplicits.customShow
```

### Remove duplicate implicit definitions

```scala
// Before — two definitions cause ambiguity
// object A { implicit val x: Foo = ??? }
// object B { implicit val x: Foo = ??? }

// After — keep only one
object A { implicit val x: Foo = ??? }
// Remove from B or rename to something different
```

## Common Scenarios

- Mixing in multiple traits that each provide an implicit for the same type class
- Importing a library's implicits alongside your own custom implementations
- Upgrading a library and discovering new implicit definitions conflict with existing ones

## Prevent It

- Design implicit hierarchies with clear priority levels using trait linearization
- Avoid wildcard imports of objects that define implicits
- Test that implicits resolve correctly by using `summon` or `implicitly` in compile-time tests

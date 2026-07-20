---
title: "[Solution] Scala ExtractorObjectError - Brief Description"
description: "Fix Scala extractor object errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1042
---

An extractor object error occurs when `unapply` returns `None` during pattern matching.

## Common Causes

- `unapply` returning None for valid inputs
- Wrong return type from unapply
- Mismatched tuple arity

## How to Fix

Implement unapply correctly:

```scala
object EmailExtractor {
  def unapply(email: String): Option[(String, String)] = {
    email.split("@") match {
      case Array(local, domain) => Some((local, domain))
      case _ => None
    }
  }
}

"alice@example.com" match {
  case EmailExtractor(local, domain) => s"User: $local at $domain"
  case _ => "Invalid email"
}
```

## Examples

```scala
object PositiveInt {
  def unapply(s: String): Option[Int] = {
    try {
      val n = s.toInt
      if (n > 0) Some(n) else None
    } catch {
      case _: NumberFormatException => None
    }
  }
}
```

## Related Errors

- [Scala MatchError](/languages/scala/scala-match-error)
- [Scala OptionGetError](/languages/scala/scala-option-get-error)

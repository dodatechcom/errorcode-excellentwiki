---
title: "[Solution] Scala Option.get Error — Calling .get on None Value"
description: "Fix Scala Option.get on None errors. Learn safe alternatives to .get including pattern matching, getOrElse, and for-comprehensions."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

Calling `.get` on a `None` value throws a `NoSuchElementException` with the message "None.get". The `Option` type in Scala represents an optional value — `Some(value)` for present values and `None` for missing ones. Calling `.get` bypasses the safety that `Option` provides.

## Why It Happens

The most common cause is using `.get` on an `Option` that is `None` at runtime. This typically happens when a `Map.get()` returns `None` because the key does not exist, or when a database lookup finds no matching record.

Another frequent cause is chaining `.get` calls on optional values without checking for `None` at each step. Even if one step returns `Some`, a later step may return `None`, and the `.get` call will fail.

Code that uses `Option` but treats it like a nullable value (using `.get` everywhere instead of safe combinators) is prone to this error. The whole purpose of `Option` is to force you to handle the missing case.

Finally, converting from Java code that returns `null` into Scala's `Option` can be tricky. If the conversion is done incorrectly, you may end up with `None` when you expected `Some`.

## How to Fix It

### Use getOrElse for default values

```scala
// Wrong — throws NoSuchElementException if key missing
val value = map("key").get

// Correct — provides a default
val value = map.getOrElse("key", "default")
```

### Use pattern matching

```scala
option match {
  case Some(value) => process(value)
  case None        => handleMissing()
}
```

### Use for-comprehensions for chained options

```scala
for {
  user    <- findUser(id)
  profile <- findProfile(user.id)
  settings <- findSettings(profile.id)
} yield settings
```

### Use map/flatMap/filter combinators

```scala
val result = option
  .map(value => value * 2)
  .filter(value => value > 10)
  .getOrElse(0)
```

### Use foreach for side effects only

```scala
option.foreach { value =>
  println(s"Found: $value")
}
```

## Common Mistakes

- Using `.get` in production code instead of safe alternatives
- Chaining `.get` calls without checking for `None` at each step
- Using `.isDefined` followed by `.get` instead of pattern matching
- Not realizing that `Map.get` returns `Option` while `Map(key)` throws an exception
- Converting `Option` to `null` with `.orNull` and then accessing it unsafely

## Related Pages

- [Scala MatchError](/languages/scala/match-error/)
- [Scala NoSuchElementException](/languages/scala/nosuchelement/)
- [Scala NullPointerException](/languages/scala/null-pointer6/)

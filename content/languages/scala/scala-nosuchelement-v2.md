---
title: "[Solution] Scala NoSuchElementException Key Not Found"
description: "Fix Scala NoSuchElementException when accessing Map keys that don't exist. Use getOrElse, contains, or Pattern matching."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nosuchelement", "map", "key", "option", "lookup", "scala"]
weight: 5
---

## What This Error Means

A `java.util.NoSuchElementException: key not found` occurs when you access a Map using `()` or `.get()` on a key that doesn't exist. The Map's `apply` method throws this exception.

## Common Causes

- Accessing Map with `()` on non-existent key
- Not checking if key exists before access
- Key name typo
- Case sensitivity differences in keys

## How to Fix

```scala
// WRONG: Direct access without check
val map = Map("a" -> 1, "b" -> 2)
val value = map("c")  // NoSuchElementException

// CORRECT: Use getOrElse for safe access
val value = map.getOrElse("c", 0)
```

```scala
// WRONG: Using apply on Optional Map
val maybeMap: Map[String, Int] = Map.empty
val v = maybeMap("key")  // Error

// CORRECT: Use get which returns Option
maybeMap.get("key") match {
  case Some(v) => println(v)
  case None => println("Key not found")
}
```

```scala
// WRONG: Forcing value from Optional
val optValue: Option[Int] = map.get("missing")
val forced = optValue.get  // NoSuchElementException if None

// CORRECT: Pattern match or use methods
optValue match {
  case Some(v) => use(v)
  case None => handleMissing()
}
// Or: optValue.getOrElse(default)
// Or: optValue.foreach(use)
```

## Examples

```scala
// Example 1: Safe map access
val config = Map("host" -> "localhost", "port" -> "8080")
val timeout = config.getOrElse("timeout", "30")

// Example 2: Contains check
if (config.contains("host")) {
  println(config("host"))
}

// Example 3: WithDefault for missing keys
val mapWithDefault = Map("a" -> 1).withDefaultValue(0)
println(mapWithDefault("b"))  // 0

// Example 4: Collect for conditional extraction
val names = Map(1 -> "Alice", 2 -> "Bob")
val validNames = names.collect {
  case (id, name) if id > 0 => name
}
```

## Related Errors

- [scala-matcherror]({{< relref "/languages/scala/scala-matcherror" >}}) — pattern match failed
- [scala-nullpointer]({{< relref "/languages/scala/scala-nullpointer" >}}) — null pointer
- [scala-outofmemory]({{< relref "/languages/scala/scala-outofmemory" >}}) — out of memory

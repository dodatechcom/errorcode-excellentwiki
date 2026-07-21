---
title: "[Solution] Deprecated Function Migration: let/run confusion to clear intent"
description: "Migrate from unclear let/run usage to clear intent-based selection."
deprecated_function: "obj.let { ... }"
replacement_function: "obj.apply { ... } or obj.run { ... }"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.0+"
---

# [Solution] Deprecated Function Migration: let/run confusion to clear intent

The `obj.let { ... }` has been deprecated in favor of `obj.apply { ... } or obj.run { ... }`.

## Migration Guide

Choose the right scope function for clarity

let, run, apply, also, with each have different purposes. Use the right one.

## Before (Deprecated)

```kotlin
// Confusing: what does this do?
user?.let {
    it.name = "Bob"
    it.age = 25
}

// Better: use apply for configuration
user?.apply {
    name = "Bob"
    age = 25
}
```

## After (Modern)

```kotlin
// apply: configure object (this)
user?.apply {
    name = "Bob"
    age = 25
}

// let: transform (it)
val upper = user?.let { it.name.uppercase() }

// run: transform + context (this)
val result = user?.run { "$name is $age" }

// also: side effect (it)
user?.also { println(it) }
```

## Key Differences

- apply: configure object (this, returns this)
- let: transform (it, returns result)
- run: transform + context (this)
- also: side effect (it, returns this)
- with: existing object (this)

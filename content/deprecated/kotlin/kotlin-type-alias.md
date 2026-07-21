---
title: "[Solution] Deprecated Function Migration: complex generic types to typealias"
description: "Migrate from complex type declarations to typealias."
deprecated_function: "Map<String, List<Pair<Int, String>>>"
replacement_function: "typealias"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.4+"
---

# [Solution] Deprecated Function Migration: complex generic types to typealias

The `Map<String, List<Pair<Int, String>>>` has been deprecated in favor of `typealias`.

## Migration Guide

typealias makes complex types readable

Complex type signatures are hard to read.

## Before (Deprecated)

```kotlin
fun process(data: Map<String, List<Pair<Int, String>>>) { }
```

## After (Modern)

```kotlin
typealias ItemPair = Pair<Int, String>
typealias ItemMap = Map<String, List<ItemPair>>

fun process(data: ItemMap) { }
```

## Key Differences

- typealias creates a name alias
- Improves readability
- No runtime overhead

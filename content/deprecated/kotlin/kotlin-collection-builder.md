---
title: "[Solution] Deprecated Function Migration: manual list building to buildList/buildMap"
description: "Migrate from deprecated manual collection building to buildList."
deprecated_function: "val list = mutableListOf(); list.add(x)"
replacement_function: "val list = buildList { add(x) }"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.6+"
---

# [Solution] Deprecated Function Migration: manual list building to buildList/buildMap

The `val list = mutableListOf(); list.add(x)` has been deprecated in favor of `val list = buildList { add(x) }`.

## Migration Guide

buildList is more concise.

## Before (Deprecated)

```kotlin
val list = mutableListOf<String>()
list.add("a")
list.add("b")
```

## After (Modern)

```kotlin
val list = buildList {
    add("a")
    add("b")
}
```

## Key Differences

- buildList is concise

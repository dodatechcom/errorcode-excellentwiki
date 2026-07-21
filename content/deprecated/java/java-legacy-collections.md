---
title: "[Solution] Deprecated Function Migration: synchronized wrappers to concurrent collections"
description: "Migrate from deprecated synchronized wrappers to concurrent collections."
deprecated_function: "Collections.synchronizedList"
replacement_function: "CopyOnWriteArrayList / ConcurrentHashMap"
languages: ["java"]
deprecated_since: "Java 5+"
---

# [Solution] Deprecated Function Migration: synchronized wrappers to concurrent collections

The `Collections.synchronizedList` has been deprecated in favor of `CopyOnWriteArrayList / ConcurrentHashMap`.

## Migration Guide

Concurrent collections are more efficient

Synchronized wrappers block on every access.

## Before (Deprecated)

```java
List<String> list = Collections.synchronizedList(new ArrayList<>());
```

## After (Modern)

```java
List<String> list = new CopyOnWriteArrayList<>();
```

## Key Differences

- CopyOnWriteArrayList for read-heavy
- ConcurrentHashMap for concurrent maps

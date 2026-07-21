---
title: "[Solution] Deprecated Function Migration: Vector to ArrayList"
description: "Migrate from deprecated Vector to ArrayList."
deprecated_function: "Vector<T>"
replacement_function: "ArrayList<T>"
languages: ["java"]
deprecated_since: "Java 1.2+"
---

# [Solution] Deprecated Function Migration: Vector to ArrayList

The `Vector<T>` has been deprecated in favor of `ArrayList<T>`.

## Migration Guide

ArrayList is not synchronized.

## Before (Deprecated)

```java
Vector<Integer> v = new Vector<>();
```

## After (Modern)

```java
ArrayList<Integer> list = new ArrayList<>();
```

## Key Differences

- ArrayList is faster

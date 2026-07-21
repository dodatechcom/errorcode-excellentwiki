---
title: "[Solution] Deprecated Function Migration: Hashtable to HashMap"
description: "Migrate from deprecated Hashtable to HashMap for non-synchronized map operations in Java."
deprecated_function: "Hashtable"
replacement_function: "HashMap (or ConcurrentHashMap)"
languages: ["java"]
deprecated_since: "Java 1.2+"
---

# [Solution] Deprecated Function Migration: Hashtable to HashMap

The `Hashtable` has been deprecated in favor of `HashMap (or ConcurrentHashMap)`.

## Migration Guide

Hashtable synchronizes every method. HashMap is faster for single-threaded use.

## Before (Deprecated)

```java
import java.util.Hashtable;

Hashtable<String, Integer> scores = new Hashtable<>();
scores.put("Alice", 100);
scores.put("Bob", 85);
```

## After (Modern)

```java
import java.util.HashMap;

HashMap<String, Integer> scores = new HashMap<>();
scores.put("Alice", 100);
scores.put("Bob", 85);

// For concurrent access
import java.util.concurrent.ConcurrentHashMap;
ConcurrentHashMap<String, Integer> concurrent = new ConcurrentHashMap<>();
```

## Key Differences

- HashMap is not synchronized -- faster
- Use ConcurrentHashMap for thread safety
- Hashtable does not allow null keys/values

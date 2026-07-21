---
title: "[Solution] Deprecated Function Migration: Hashtable to ConcurrentHashMap"
description: "Migrate from deprecated Hashtable to ConcurrentHashMap."
deprecated_function: "Hashtable<K,V>"
replacement_function: "ConcurrentHashMap<K,V>"
languages: ["java"]
deprecated_since: "Java 5+"
---

# [Solution] Deprecated Function Migration: Hashtable to ConcurrentHashMap

The `Hashtable<K,V>` has been deprecated in favor of `ConcurrentHashMap<K,V>`.

## Migration Guide

ConcurrentHashMap is more efficient.

## Before (Deprecated)

```java
Hashtable<String, Integer> ht = new Hashtable<>();
```

## After (Modern)

```java
ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();
```

## Key Differences

- ConcurrentHashMap is more efficient

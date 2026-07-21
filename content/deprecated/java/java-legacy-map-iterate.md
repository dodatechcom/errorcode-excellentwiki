---
title: "[Solution] Deprecated Function Migration: keySet iteration to entrySet"
description: "Migrate from deprecated keySet iteration to entrySet."
deprecated_function: "for (K key : map.keySet()) { V val = map.get(key); }"
replacement_function: "for (Map.Entry<K,V> entry : map.entrySet()) { }"
languages: ["java"]
deprecated_since: "Java 5+"
---

# [Solution] Deprecated Function Migration: keySet iteration to entrySet

The `for (K key : map.keySet()) { V val = map.get(key); }` has been deprecated in favor of `for (Map.Entry<K,V> entry : map.entrySet()) { }`.

## Migration Guide

entrySet avoids double lookup.

## Before (Deprecated)

```java
for (String key : map.keySet()) {
    Integer value = map.get(key);
}
```

## After (Modern)

```java
for (Map.Entry<String, Integer> entry : map.entrySet()) {
    String key = entry.getKey();
    Integer value = entry.getValue();
}
```

## Key Differences

- entrySet avoids double lookup

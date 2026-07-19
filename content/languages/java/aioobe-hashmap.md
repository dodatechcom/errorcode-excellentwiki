---
title: "[Solution] Java ArrayIndexOutOfBoundsException — concurrent access corrupts HashMap internal bucket array"
description: "Fix Java ArrayIndexOutOfBoundsException when concurrent access corrupts hashmap internal bucket array with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ArrayIndexOutOfBoundsException — concurrent access corrupts HashMap internal bucket array

A `ArrayIndexOutOfBoundsException` occurs when Map<String,Integer> map = new HashMap<>();
// Thread1: map.put("a",1); Thread2: map.get("a"); // AIOOBE.

## Common Causes

```java
Map<String,Integer> map = new HashMap<>();
// Thread1: map.put("a",1); Thread2: map.get("a"); // AIOOBE
```

## Solutions

```java
// Fix: ConcurrentHashMap
Map<String,Integer> map = new ConcurrentHashMap<>();

// Fix: synchronize
synchronized (map) { map.put("key", value); }

// Fix: immutable for read-only
Map<String,Integer> map = Map.of("k1",1,"k2",2);
```

## Prevention Checklist

- Never use HashMap from multiple threads without sync.
- Use ConcurrentHashMap for concurrent access.
- Use Map.of() for immutable maps.

## Related Errors

ConcurrentModificationException, NullPointerException

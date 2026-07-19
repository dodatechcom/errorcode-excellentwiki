---
title: "[Solution] Java UnsupportedOperationException — attempting put/remove/clear on Map.of or unmodifiableMap"
description: "Fix Java UnsupportedOperationException when attempting put/remove/clear on map.of or unmodifiablemap with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# UnsupportedOperationException — attempting put/remove/clear on Map.of or unmodifiableMap

A `UnsupportedOperationException` occurs when Map<String,Integer> map = Map.of("a",1);
map.put("b",2);  // UOE.

## Common Causes

```java
Map<String,Integer> map = Map.of("a",1);
map.put("b",2);  // UOE
```

## Solutions

```java
// Fix: mutable map
Map<String,Integer> map = new HashMap<>(Map.of("a",1));
map.put("b",2);

// Fix: Collectors.toMap
Map<String,Integer> result = Stream.of("a","b")
    .collect(Collectors.toMap(Function.identity(), String::length));

// Fix: ConcurrentHashMap
Map<String,Integer> map = new ConcurrentHashMap<>(Map.of("a",1));
map.put("b",2);
```

## Prevention Checklist

- Use Map.of() only for constants.
- Use new HashMap<>(immutableMap) for mutable.
- Use Collectors.toMap() for mutable.

## Related Errors

UnsupportedOperationException, NullPointerException

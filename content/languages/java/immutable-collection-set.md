---
title: "[Solution] Java UnsupportedOperationException — attempting to set/replace elements in immutable collection"
description: "Fix Java UnsupportedOperationException when attempting to set/replace elements in immutable collection with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# UnsupportedOperationException — attempting to set/replace elements in immutable collection

A `UnsupportedOperationException` occurs when ImmutableMap<String,Integer> map = ImmutableMap.of("a",1);
map.put("b",2);  // UnsupportedOperationException.

## Common Causes

```java
ImmutableMap<String,Integer> map = ImmutableMap.of("a",1);
map.put("b",2);  // UnsupportedOperationException
```

## Solutions

```java
// Fix: builder
ImmutableMap<String,Integer> map = ImmutableMap.<String,Integer>builder()
    .put("a",1).put("b",2).build();

// Fix: mutable copy
Map<String,Integer> mutable = new HashMap<>(map);
mutable.put("b",2);

// Fix: stream collect
ImmutableMap<String,Integer> map2 = Stream.of(Map.entry("a",1), Map.entry("b",2))
    .collect(ImmutableMap.toImmutableMap(Map.Entry::getKey, Map.Entry::getValue));
```

## Prevention Checklist

- Use ImmutableMap.builder() for construction.
- Create mutable copies before modification.
- Use Collectors.toImmutableMap() from streams.

## Related Errors

UnsupportedOperationException, NullPointerException

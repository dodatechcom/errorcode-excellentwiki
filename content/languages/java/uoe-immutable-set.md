---
title: "[Solution] Java UnsupportedOperationException — attempting add/remove on Set.of or unmodifiableSet"
description: "Fix Java UnsupportedOperationException when attempting add/remove on set.of or unmodifiableset with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# UnsupportedOperationException — attempting add/remove on Set.of or unmodifiableSet

A `UnsupportedOperationException` occurs when Set<String> set = Set.of("a","b");
set.add("c");  // UOE.

## Common Causes

```java
Set<String> set = Set.of("a","b");
set.add("c");  // UOE
```

## Solutions

```java
// Fix: mutable set
Set<String> set = new HashSet<>(Set.of("a","b"));
set.add("c");

// Fix: Collectors.toSet()
Set<String> result = Stream.of("a","b").collect(Collectors.toSet());

// Fix: EnumSet
Set<Color> colors = EnumSet.of(Color.RED, Color.GREEN);
colors.add(Color.BLUE);
```

## Prevention Checklist

- Know Set.of() vs new HashSet<>().
- Use Collectors.toSet() for mutable.
- Use EnumSet for enum sets.

## Related Errors

UnsupportedOperationException, NullPointerException

---
title: "[Solution] Java UnsupportedOperationException — modifying subList view from immutable or unmodifiable list"
description: "Fix Java UnsupportedOperationException when modifying sublist view from immutable or unmodifiable list with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# UnsupportedOperationException — modifying subList view from immutable or unmodifiable list

A `UnsupportedOperationException` occurs when List<String> list = List.of("a","b","c","d");
List<String> sub = list.subList(1,3);
sub.add("x");  // UOE.

## Common Causes

```java
List<String> list = List.of("a","b","c","d");
List<String> sub = list.subList(1,3);
sub.add("x");  // UOE
```

## Solutions

```java
// Fix: mutable copy
List<String> sub = new ArrayList<>(list.subList(1,3));
sub.add("x");

// Fix: streams
List<String> result = list.stream().skip(1).limit(2).collect(Collectors.toArrayList());

// Fix: modify parent list directly
List<String> list = new ArrayList<>(List.of("a","b","c"));
list.add(2, "x");
```

## Prevention Checklist

- Never modify subList view unless parent is mutable.
- Use new ArrayList<>(list.subList(...)) for copy.
- Use streams for safe slicing.

## Related Errors

UnsupportedOperationException, ConcurrentModificationException

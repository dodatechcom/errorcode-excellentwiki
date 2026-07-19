---
title: "[Solution] Java UnsupportedOperationException — attempting to add to ImmutableList, ImmutableSet, or ImmutableMap from Guava"
description: "Fix Java UnsupportedOperationException when attempting to add to immutablelist, immutableset, or immutablemap from guava with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# UnsupportedOperationException — attempting to add to ImmutableList, ImmutableSet, or ImmutableMap from Guava

A `UnsupportedOperationException` occurs when ImmutableList<String> list = ImmutableList.of("a","b");
list.add("c");  // UnsupportedOperationException.

## Common Causes

```java
ImmutableList<String> list = ImmutableList.of("a","b");
list.add("c");  // UnsupportedOperationException
```

## Solutions

```java
// Fix: use builder
ImmutableList<String> list = ImmutableList.<String>builder()
    .add("a").add("b").add("c")
    .build();

// Fix: mutable copy
List<String> mutable = new ArrayList<>(list);
mutable.add("c");

// Fix: use copyOf with new element
ImmutableList<String> list2 = ImmutableList.copyOf(
    Stream.concat(list.stream(), Stream.of("c")).collect(toList()));
```

## Prevention Checklist

- Use ImmutableList.builder() for dynamic construction.
- Create mutable copies before modification.
- Use Stream.concat() to create new immutable lists.

## Related Errors

UnsupportedOperationException, NullPointerException

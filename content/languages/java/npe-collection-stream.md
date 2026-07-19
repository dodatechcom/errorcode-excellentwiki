---
title: "[Solution] Java NullPointerException"
description: "Stream Pipeline Null Elements"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# null elements in collections causing NPE in stream map, filter, or reduce

A `null` is thrown when list<string> names = arrays.aslist("alice", null, "bob");.

## Common Causes

```java
List<String> names = Arrays.asList("Alice", null, "Bob");
names.stream().map(String::length)  // NPE on null
```

## Solutions

```java
// Fix: filter nulls first
names.stream().filter(Objects::nonNull).map(String::length).collect(toList());

// Fix: null-safe groupingBy
people.stream().collect(Collectors.groupingBy(
    p -> Optional.ofNullable(p.getCity()).orElse("Unknown")));
```

## Prevention Checklist

- Filter nulls with .filter(Objects::nonNull).
- Use null-safe mapping functions.
- Configure Collectors.toMap with merge function.

## Related Errors

[NullPointerException](nullpointerexception), [ConcurrentModificationException](concurrentmodificationexception)

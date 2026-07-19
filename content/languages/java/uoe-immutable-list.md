---
title: "[Solution] Java UnsupportedOperationException — attempting add/remove/set on List.of or unmodifiableList"
description: "Fix Java UnsupportedOperationException when attempting add/remove/set on list.of or unmodifiablelist with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# UnsupportedOperationException — attempting add/remove/set on List.of or unmodifiableList

A `UnsupportedOperationException` occurs when List<String> list = List.of("a","b");
list.add("c");  // UOE.

## Common Causes

```java
List<String> list = List.of("a","b");
list.add("c");  // UOE
```

## Solutions

```java
// Fix: mutable copy
List<String> list = new ArrayList<>(List.of("a","b"));
list.add("c");

// Fix: concat with streams
List<String> result = Stream.concat(
    List.of("a").stream(), Stream.of("b")).collect(toList());
```

## Prevention Checklist

- Know which lists are mutable vs immutable.
- Use new ArrayList<>(immutableList) for mutable copy.
- Use List.of() only for constants.

## Related Errors

UnsupportedOperationException, NullPointerException

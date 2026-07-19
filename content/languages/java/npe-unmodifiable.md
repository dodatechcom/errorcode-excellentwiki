---
title: "[Solution] Java NullPointerException"
description: "Unmodifiable Collection Null Handling"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# attempting to add null elements to List.of, Set.of, or Map.of

A `attempting` is thrown when list<string> list = list.of("a", "b", null);  // npe.

## Common Causes

```java
List<String> list = List.of("a", "b", null);  // NPE
Set<String> set = Set.of("a", null);  // NPE
```

## Solutions

```java
// Fix: use Arrays.asList for null-safe
List<String> list = Arrays.asList("a", "b", null);

// Fix: filter before immutable
List<String> result = Stream.of("a",null,"b")
    .filter(Objects::nonNull).collect(Collectors.toUnmodifiableList());
```

## Prevention Checklist

- Never pass null to List.of/Set.of/Map.of.
- Filter nulls before creating immutable collections.
- Use Arrays.asList for fixed-size lists with nulls.

## Related Errors

[NullPointerException](nullpointerexception), [UnsupportedOperationException](unsupportedoperation-immutable-list)

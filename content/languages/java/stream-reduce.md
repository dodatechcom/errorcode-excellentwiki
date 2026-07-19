---
title: "[Solution] Java UnsupportedOperationException — reduce without identity on empty stream, or collect to unmodifiable with null"
description: "Fix Java UnsupportedOperationException when reduce without identity on empty stream, or collect to unmodifiable with null with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# UnsupportedOperationException — reduce without identity on empty stream, or collect to unmodifiable with null

A `UnsupportedOperationException` occurs when Stream.<Integer>empty().reduce(Integer::sum);  // Optional.empty.

## Common Causes

```java
Stream.<Integer>empty().reduce(Integer::sum);  // Optional.empty
```

## Solutions

```java
// Fix: provide identity
int sum = list.stream().mapToInt(Integer::intValue).sum();

// Fix: filter nulls for unmodifiable
List<String> result = list.stream().filter(Objects::nonNull)
    .collect(Collectors.toUnmodifiableList());

// Fix: Collectors.toList() for mutable
List<String> result = list.stream().collect(Collectors.toList());
```

## Prevention Checklist

- Always provide identity for reduce().
- Filter nulls before unmodifiable collect.
- Use Collectors.toList() for mutable results.

## Related Errors

NullPointerException, NoSuchElementException

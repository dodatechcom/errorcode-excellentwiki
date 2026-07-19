---
title: "[Solution] Java NullPointerException"
description: "Generic Type Bound Violations"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# type erasure prevents null checks, bounded types allow null

A `type` is thrown when public <t> t findfirst(list<t> list) {.

## Common Causes

```java
public <T> T findFirst(List<T> list) {
    return list.isEmpty() ? null : list.get(0);
}
```

## Solutions

```java
// Fix: return Optional
public <T> Optional<T> findFirst(List<T> list) {
    return list.isEmpty() ? Optional.empty() : Optional.of(list.get(0));
}

// Fix: filter nulls
public <T extends Number> double sum(List<T> numbers) {
    return numbers.stream().filter(Objects::nonNull)
        .mapToDouble(Number::doubleValue).sum();
}
```

## Prevention Checklist

- Never return null from generic methods.
- Filter nulls before operating on generic collections.
- Use Objects.requireNonNull in generic constructors.

## Related Errors

[NullPointerException](nullpointerexception), [ClassCastException](classcastexception)

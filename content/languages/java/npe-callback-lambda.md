---
title: "[Solution] Java NullPointerException"
description: "Lambda and Callback Null Returns"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# lambda or callback returning null when callers expect non-null

A `lambda` is thrown when function<string,integer> parser = s -> {.

## Common Causes

```java
Function<String,Integer> parser = s -> {
    try { return Integer.parseInt(s); }
    catch (NumberFormatException e) { return null; }
};
int v = parser.apply("abc") + 1;  // NPE auto-unboxing
```

## Solutions

```java
// Fix: return Optional
Function<String,Optional<Integer>> parser = s -> {
    try { return Optional.of(Integer.parseInt(s)); }
    catch (NumberFormatException e) { return Optional.empty(); }
};
int v = parser.apply("abc").orElse(0) + 1;

// Fix: Objects.requireNonNullElse
User u = Optional.ofNullable(userFactory.get()).orElse(new DefaultUser());
```

## Prevention Checklist

- Document when lambda returns can be null.
- Return Optional instead of null from functional interfaces.
- Callers should handle potential null returns.

## Related Errors

[NullPointerException](nullpointerexception), [NoSuchElementException](optional-nosuchelement)

---
title: "[Solution] Java NullPointerException"
description: "Incorrect Optional Usage"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# returning null from Optional.map() or chaining orElse incorrectly

A `returning` is thrown when opt.map(s -> { if (s.equals("hello")) return null; return s.length(); });.

## Common Causes

```java
opt.map(s -> { if (s.equals("hello")) return null; return s.length(); });
```

## Solutions

```java
// Fix: use filter instead of map returning null
Optional<Integer> result = opt.filter(s -> !s.equals("hello")).map(String::length);

// Fix: use flatMap for nested Optionals
Optional<Result> result = Optional.ofNullable(getConfig())
    .flatMap(c -> findSetting(c, "timeout"))
    .map(Setting::parse);
```

## Prevention Checklist

- Never return null from Optional.map() lambdas.
- Use flatMap() for nested Optionals.
- Never call Optional.get() without isPresent().

## Related Errors

[NullPointerException](nullpointerexception), [NoSuchElementException](optional-nosuchelement)

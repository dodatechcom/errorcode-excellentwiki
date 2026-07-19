---
title: "[Solution] Java NoSuchElementException — calling findFirst().get() on empty or filtered-out stream"
description: "Fix Java NoSuchElementException when calling findfirst().get() on empty or filtered-out stream with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NoSuchElementException — calling findFirst().get() on empty or filtered-out stream

A `NoSuchElementException` occurs when String first = list.stream().filter(s -> s.length()>5).findFirst().get();.

## Common Causes

```java
String first = list.stream().filter(s -> s.length()>5).findFirst().get();
```

## Solutions

```java
// Fix: orElse
String first = list.stream().filter(s -> s.length()>5).findFirst().orElse("default");

// Fix: orElseThrow
String first = list.stream().filter(s -> s.length()>5).findFirst()
    .orElseThrow(() -> new ISE("No match"));

// Fix: ifPresent
list.stream().filter(s -> s.length()>5).findFirst().ifPresent(s -> process(s));
```

## Prevention Checklist

- Never call Optional.get() without isPresent().
- Use orElse(), orElseThrow(), or ifPresent().
- Use reduce() with identity for accumulation.

## Related Errors

NoSuchElementException, IllegalStateException

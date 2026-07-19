---
title: "[Solution] Java NoSuchElementException — min, max, or reduce expecting elements on empty stream"
description: "Fix Java NoSuchElementException when min, max, or reduce expecting elements on empty stream with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NoSuchElementException — min, max, or reduce expecting elements on empty stream

A `NoSuchElementException` occurs when String s = list.stream().min(Comparator.comparing(String::length)).get();.

## Common Causes

```java
String s = list.stream().min(Comparator.comparing(String::length)).get();
```

## Solutions

```java
// Fix: orElse
String s = list.stream().min(Comparator.comparing(String::length)).orElse("default");

// Fix: orElseThrow with message
String s = list.stream().min(Comparator.comparing(String::length))
    .orElseThrow(() -> new ISE("No elements"));

// Fix: Collectors.joining
String joined = list.stream().map(Object::toString).collect(Collectors.joining(", "));
```

## Prevention Checklist

- Never call Optional.get() without checking.
- Use orElse() or orElseThrow().
- Use Collectors.joining() for string accumulation.

## Related Errors

NoSuchElementException, IllegalStateException

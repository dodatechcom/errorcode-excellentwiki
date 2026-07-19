---
title: "[Solution] Java NoSuchElementException — calling Optional.get() on empty Optional without checking isPresent()"
description: "Fix Java NoSuchElementException when calling optional.get() on empty optional without checking ispresent() with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NoSuchElementException — calling Optional.get() on empty Optional without checking isPresent()

A `NoSuchElementException` occurs when Optional<String> opt = findByName("missing");
String s = opt.get();  // NoSuchElementException.

## Common Causes

```java
Optional<String> opt = findByName("missing");
String s = opt.get();  // NoSuchElementException
```

## Solutions

```java
// Fix: isPresent check
if (opt.isPresent()) { String s = opt.get(); }

// Fix: orElse
String s = opt.orElse("default");

// Fix: orElseThrow
String s = opt.orElseThrow(() -> new ISE("Not found"));

// Fix: ifPresent
opt.ifPresent(s -> process(s));

// Fix: map/filter chain
String s = opt.map(String::toUpperCase).orElse("N/A");
```

## Prevention Checklist

- Never call Optional.get() without isPresent().
- Use orElse(), orElseThrow(), or ifPresent().
- Use map()/filter() chains for transformations.

## Related Errors

NullPointerException, IllegalStateException

---
title: "[Solution] Java IllegalStateException — stream operated on after a terminal operation"
description: "Fix Java IllegalStateException when stream operated on after a terminal operation with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# IllegalStateException — stream operated on after a terminal operation

A `IllegalStateException` occurs when Stream<String> s = list.stream();
long count = s.count();
s.forEach(System.out::println);  // ISE.

## Common Causes

```java
Stream<String> s = list.stream();
long count = s.count();
s.forEach(System.out::println);  // ISE
```

## Solutions

```java
// Fix: store result not stream
List<String> result = list.stream().filter(...).collect(toList());

// Fix: new stream each time
long count = list.stream().filter(...).count();
List<String> r = list.stream().filter(...).collect(toList());

// Fix: Supplier
Supplier<Stream<String>> sup = () -> list.stream().filter(...);
long count = sup.get().count();
List<String> r = sup.get().collect(toList());
```

## Prevention Checklist

- Never assign streams to variables for reuse.
- Use Supplier<Stream<T>> for multiple operations.
- Collect results immediately.

## Related Errors

UnsupportedOperationException, ConcurrentModificationException

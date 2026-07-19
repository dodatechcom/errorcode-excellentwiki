---
title: "[Solution] Java UnsupportedOperationException — calling remove() on iterators from read-only sources"
description: "Fix Java UnsupportedOperationException when calling remove() on iterators from read-only sources with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# UnsupportedOperationException — calling remove() on iterators from read-only sources

A `UnsupportedOperationException` occurs when Iterator<String> it = Collections.emptyIterator();
it.remove();  // UOE.

## Common Causes

```java
Iterator<String> it = Collections.emptyIterator();
it.remove();  // UOE
```

## Solutions

```java
// Fix: try-catch
try { it.remove(); }
catch (UnsupportedOperationException e) { log.warn("Not supported"); }

// Fix: use collection's own remove
list.remove("b");

// Fix: streams
List<String> result = list.stream().filter(s -> !s.equals("b")).collect(toList());
```

## Prevention Checklist

- Never assume Iterator.remove() is supported.
- Use collection-level removeIf().
- Create mutable copies before removal.

## Related Errors

NoSuchElementException, ConcurrentModificationException

---
title: "[Solution] Java UnsupportedOperationException — calling remove() on Iterator from immutable collection"
description: "Fix Java UnsupportedOperationException when calling remove() on iterator from immutable collection with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# UnsupportedOperationException — calling remove() on Iterator from immutable collection

A `UnsupportedOperationException` occurs when Iterator<String> it = List.of("a","b").iterator();
it.next();
it.remove();  // UOE.

## Common Causes

```java
Iterator<String> it = List.of("a","b").iterator();
it.next();
it.remove();  // UOE
```

## Solutions

```java
// Fix: mutable collection iterator
List<String> list = new ArrayList<>(List.of("a","b"));
Iterator<String> it = list.iterator();
it.next(); it.remove();

// Fix: removeIf
list.removeIf(item -> item.equals("b"));

// Fix: collect to remove
List<String> toRemove = new ArrayList<>();
for (String item : list) { if (item.equals("b")) toRemove.add(item); }
list.removeAll(toRemove);
```

## Prevention Checklist

- Check if collection is mutable before Iterator.remove().
- Use removeIf() for safe filtering.
- Create mutable copies before removing.

## Related Errors

ConcurrentModificationException, IllegalStateException

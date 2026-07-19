---
title: "[Solution] Java ConcurrentModificationException — multiple threads read/write same non-synchronized collection"
description: "Fix Java ConcurrentModificationException when multiple threads read/write same non-synchronized collection with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ConcurrentModificationException — multiple threads read/write same non-synchronized collection

A `ConcurrentModificationException` occurs when List<String> shared = new ArrayList<>();
// Thread1: shared.add("a"); Thread2: for (String s : shared) { process(s); } // CME.

## Common Causes

```java
List<String> shared = new ArrayList<>();
// Thread1: shared.add("a"); Thread2: for (String s : shared) { process(s); } // CME
```

## Solutions

```java
// Fix: ConcurrentHashMap
Map<String,Integer> map = new ConcurrentHashMap<>();

// Fix: CopyOnWriteArrayList
List<String> list = new CopyOnWriteArrayList<>();

// Fix: synchronize
synchronized (list) { for (String item : list) { process(item); } }

// Fix: immutable for read-only
List<String> shared = List.of("a","b","c");
```

## Prevention Checklist

- Use ConcurrentHashMap for concurrent map access.
- Use CopyOnWriteArrayList for read-heavy.
- Synchronize all access to non-thread-safe collections.

## Related Errors

NullPointerException, IllegalStateException

---
title: "[Solution] Java ConcurrentModificationException — using Collection.remove() inside enhanced for-each"
description: "Fix Java ConcurrentModificationException when using collection.remove() inside enhanced for-each with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ConcurrentModificationException — using Collection.remove() inside enhanced for-each

A `ConcurrentModificationException` occurs when List<String> list = new ArrayList<>(Arrays.asList("a","b","c"));
for (String item : list) {
    if (item.equals("b")) list.remove(item);  // CME
}.

## Common Causes

```java
List<String> list = new ArrayList<>(Arrays.asList("a","b","c"));
for (String item : list) {
    if (item.equals("b")) list.remove(item);  // CME
}
```

## Solutions

```java
// Fix: Iterator.remove()
Iterator<String> it = list.iterator();
while (it.hasNext()) { if (it.next().equals("b")) it.remove(); }

// Fix: removeIf
list.removeIf(item -> item.equals("b"));

// Fix: streams
List<String> result = list.stream().filter(item -> !item.equals("b")).collect(toList());
```

## Prevention Checklist

- Never use Collection.remove() in for-each.
- Use removeIf() for simple filtering.
- Use stream operations.

## Related Errors

IllegalStateException, UnsupportedOperationException

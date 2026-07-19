---
title: "[Solution] Java IllegalStateException — calling next() after all elements consumed, or remove() without next()"
description: "Fix Java IllegalStateException when calling next() after all elements consumed, or remove() without next() with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# IllegalStateException — calling next() after all elements consumed, or remove() without next()

A `IllegalStateException` occurs when Iterator<String> it = list.iterator();
while (it.hasNext()) { String s = it.next(); }
it.next();  // NoSuchElementException.

## Common Causes

```java
Iterator<String> it = list.iterator();
while (it.hasNext()) { String s = it.next(); }
it.next();  // NoSuchElementException
```

## Solutions

```java
// Fix: hasNext check
while (it.hasNext()) { String s = it.next(); process(s); }

// Fix: enhanced for
for (String s : list) { process(s); }

// Fix: removeIf
list.removeIf(item -> shouldRemove(item));
```

## Prevention Checklist

- Always check hasNext() before next().
- Use enhanced for-loops.
- Use stream API for declarative iteration.

## Related Errors

NoSuchElementException, ConcurrentModificationException

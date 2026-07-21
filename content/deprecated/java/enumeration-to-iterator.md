---
title: "[Solution] Deprecated Function Migration: Enumeration to Iterator"
description: "Migrate from deprecated Enumeration to Iterator for traversing collections in Java."
deprecated_function: "Enumeration"
replacement_function: "Iterator"
languages: ["java"]
deprecated_since: "Java 1.2+"
---

# [Solution] Deprecated Function Migration: Enumeration to Iterator

The `Enumeration` has been deprecated in favor of `Iterator`.

## Migration Guide

Iterator supports remove() and is the standard interface for traversing collections.

## Before (Deprecated)

```java
import java.util.Vector;
import java.util.Enumeration;

Vector<String> list = new Vector<>();
Enumeration<String> e = list.elements();
while (e.hasMoreElements()) {
    String item = e.nextElement();
    System.out.println(item);
}
```

## After (Modern)

```java
import java.util.ArrayList;
import java.util.Iterator;

ArrayList<String> list = new ArrayList<>();
Iterator<String> it = list.iterator();
while (it.hasNext()) {
    String item = it.next();
    System.out.println(item);
}
```

## Key Differences

- Iterator has remove() method
- For-each loop uses Iterator internally
- Enumeration is legacy

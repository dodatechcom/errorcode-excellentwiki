---
title: "[Solution] Deprecated Function Migration: Vector enumeration to ArrayList iteration"
description: "Migrate from deprecated Vector enumeration to ArrayList iteration."
deprecated_function: "Vector + Enumeration"
replacement_function: "ArrayList + for-each"
languages: ["java"]
deprecated_since: "Java 1.2+"
---

# [Solution] Deprecated Function Migration: Vector enumeration to ArrayList iteration

The `Vector + Enumeration` has been deprecated in favor of `ArrayList + for-each`.

## Migration Guide

ArrayList is faster and more modern

Vector is legacy from Java 1.0.

## Before (Deprecated)

```java
Vector<String> vec = new Vector<>();
Enumeration<String> e = vec.elements();
while (e.hasMoreElements()) {
    System.out.println(e.nextElement());
}
```

## After (Modern)

```java
ArrayList<String> list = new ArrayList<>();
for (String s : list) {
    System.out.println(s);
}
list.forEach(System.out::println);
```

## Key Differences

- ArrayList is not synchronized
- for-each is cleaner
- streams for functional style

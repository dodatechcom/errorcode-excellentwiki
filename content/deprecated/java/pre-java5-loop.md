---
title: "[Solution] Deprecated Function Migration: Iterator-based loops to enhanced for loop"
description: "Migrate from deprecated Iterator-based loop to enhanced for-each loop in Java."
deprecated_function: "Iterator-based loops"
replacement_function: "for-each loop"
languages: ["java"]
deprecated_since: "Java 5+"
---

# [Solution] Deprecated Function Migration: Iterator-based loops to enhanced for loop

The `Iterator-based loops` has been deprecated in favor of `for-each loop`.

## Migration Guide

The enhanced for loop (for-each) is cleaner and less error-prone than explicit Iterator usage.

## Before (Deprecated)

```java
List<String> names = getNames();
for (Iterator<String> it = names.iterator(); it.hasNext();) {
    String name = it.next();
    System.out.println(name);
}
```

## After (Modern)

```java
List<String> names = getNames();
for (String name : names) {
    System.out.println(name);
}

// Or with streams
names.forEach(name -> System.out.println(name));
```

## Key Differences

- for-each is more concise
- No Iterator boilerplate
- forEach for functional style
- Use Iterator only when you need remove()

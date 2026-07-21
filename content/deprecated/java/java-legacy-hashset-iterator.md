---
title: "[Solution] Deprecated Function Migration: HashSet iterator to for-each loop"
description: "Migrate from deprecated iterator-based iteration to enhanced for-each loop."
deprecated_function: "Iterator-based loops"
replacement_function: "for-each loop"
languages: ["java"]
deprecated_since: "Java 5+"
---

# [Solution] Deprecated Function Migration: HashSet iterator to for-each loop

The `Iterator-based loops` has been deprecated in favor of `for-each loop`.

## Migration Guide

Enhanced for loop is cleaner and less error-prone

The enhanced for loop is cleaner than explicit Iterator usage.

## Before (Deprecated)

```java
HashSet<String> set = new HashSet<>();
Iterator<String> it = set.iterator();
while (it.hasNext()) {
    String item = it.next();
    System.out.println(item);
}
```

## After (Modern)

```java
HashSet<String> set = new HashSet<>();
for (String item : set) {
    System.out.println(item);
}

// Or with streams
set.forEach(item -> System.out.println(item));
```

## Key Differences

- for-each is more concise
- No Iterator boilerplate
- forEach for functional style
- Use Iterator only when you need remove()

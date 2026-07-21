---
title: "[Solution] Deprecated Function Migration: Vector to ArrayList"
description: "Migrate from deprecated Vector to ArrayList for non-synchronized list operations in Java."
deprecated_function: "java.util.Vector"
replacement_function: "java.util.ArrayList"
languages: ["java"]
deprecated_since: "Java 1.2+"
---

# [Solution] Deprecated Function Migration: Vector to ArrayList

The `java.util.Vector` has been deprecated in favor of `java.util.ArrayList`.

## Migration Guide

Vector synchronizes every method. ArrayList provides the same functionality without synchronization overhead.

## Before (Deprecated)

```java
import java.util.Vector;

Vector<String> names = new Vector<>();
names.add("Alice");
names.add("Bob");

for (String name : names) {
    System.out.println(name);
}
```

## After (Modern)

```java
import java.util.ArrayList;

ArrayList<String> names = new ArrayList<>();
names.add("Alice");
names.add("Bob");

for (String name : names) {
    System.out.println(name);
}

// For concurrent access
import java.util.concurrent.CopyOnWriteArrayList;
CopyOnWriteArrayList<String> threadSafe = new CopyOnWriteArrayList<>();
```

## Key Differences

- ArrayList has no synchronization overhead
- Use CopyOnWriteArrayList for concurrent access
- Both implement List interface

---
title: "[Solution] Deprecated Function Migration: Enum.values() to EnumSet/EnumMap"
description: "Migrate from deprecated manual enum iteration to EnumSet/EnumMap."
deprecated_function: "MyEnum.values()"
replacement_function: "EnumSet.of()"
languages: ["java"]
deprecated_since: "Java 5+"
---

# [Solution] Deprecated Function Migration: Enum.values() to EnumSet/EnumMap

The `MyEnum.values()` has been deprecated in favor of `EnumSet.of()`.

## Migration Guide

EnumSet/EnumMap are more efficient for enum-based collections

values() creates a new array each time. EnumSet/EnumMap are more efficient.

## Before (Deprecated)

```java
for (MyEnum e : MyEnum.values()) {
    System.out.println(e);
}
```

## After (Modern)

```java
EnumSet.allOf(MyEnum.class).forEach(e -> {
    System.out.println(e);
});

// For maps
EnumMap<MyEnum, String> map = new EnumMap<>(MyEnum.class);
map.put(MyEnum.VALUE, "hello");
```

## Key Differences

- EnumSet is a compact bit set
- EnumMap uses enum ordinal as index
- Both are more efficient than HashMap
- values() creates a new array each time

---
title: "[Solution] Deprecated Function Migration: String concatenation with + to StringJoiner"
description: "Migrate from deprecated String concatenation with + to StringJoiner."
deprecated_function: "result += ,  + item"
replacement_function: "StringJoiner"
languages: ["java"]
deprecated_since: "Java 8+"
---

# [Solution] Deprecated Function Migration: String concatenation with + to StringJoiner

The `result += ", " + item` has been deprecated in favor of `StringJoiner`.

## Migration Guide

StringJoiner is more efficient.

## Before (Deprecated)

```java
String result = "";
for (String item : items) {
    result += ", " + item;
}
```

## After (Modern)

```java
StringJoiner joiner = new StringJoiner(", ");
for (String item : items) {
    joiner.add(item);
}
String result = joiner.toString();
```

## Key Differences

- StringJoiner is more efficient

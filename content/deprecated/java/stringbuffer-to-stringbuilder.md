---
title: "[Solution] Deprecated Function Migration: StringBuffer to StringBuilder"
description: "Migrate from deprecated StringBuffer to StringBuilder for single-threaded string building in Java."
deprecated_function: "StringBuffer"
replacement_function: "StringBuilder"
languages: ["java"]
deprecated_since: "Java 1.5+"
---

# [Solution] Deprecated Function Migration: StringBuffer to StringBuilder

The `StringBuffer` has been deprecated in favor of `StringBuilder`.

## Migration Guide

StringBuffer synchronizes every method. StringBuilder is faster in single-threaded contexts.

## Before (Deprecated)

```java
StringBuffer sb = new StringBuffer();
sb.append("Hello");
sb.append(" ");
sb.append("World");
String result = sb.toString();
```

## After (Modern)

```java
StringBuilder sb = new StringBuilder();
sb.append("Hello");
sb.append(" ");
sb.append("World");
String result = sb.toString();

// Or with chaining
String result2 = new StringBuilder()
    .append("Hello")
    .append(" ")
    .append("World")
    .toString();
```

## Key Differences

- StringBuilder is not synchronized -- faster
- Same API as StringBuffer
- Use StringBuffer only for multi-threaded access

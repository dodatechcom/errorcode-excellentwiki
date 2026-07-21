---
title: "[Solution] Deprecated Function Migration: string concatenation in loops to StringBuilder"
description: "Migrate from deprecated string concatenation in loops to StringBuilder."
deprecated_function: "result += str"
replacement_function: "StringBuilder.append()"
languages: ["java"]
deprecated_since: "Java 1.5+"
---

# [Solution] Deprecated Function Migration: string concatenation in loops to StringBuilder

The `result += str` has been deprecated in favor of `StringBuilder.append()`.

## Migration Guide

StringBuilder avoids O(n^2) string copies

String concatenation in loops creates many temporary objects.

## Before (Deprecated)

```java
String result = "";
for (String s : items) {
    result += s;
}
```

## After (Modern)

```java
StringBuilder sb = new StringBuilder();
for (String s : items) {
    sb.append(s);
}
String result = sb.toString();

// Or use String.join
String result = String.join("", items);
```

## Key Differences

- StringBuilder avoids temporary objects
- String.join for joining strings

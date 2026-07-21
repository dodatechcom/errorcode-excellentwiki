---
title: "[Solution] Deprecated Function Migration: new String() to string literals"
description: "Migrate from deprecated new String() constructor to string literals and String.valueOf() in Java."
deprecated_function: "new String(str)"
replacement_function: "String.valueOf(str) or literal"
languages: ["java"]
deprecated_since: "Java 1.0+"
---

# [Solution] Deprecated Function Migration: new String() to string literals

The `new String(str)` has been deprecated in favor of `String.valueOf(str) or literal`.

## Migration Guide

new String(str) creates unnecessary objects. String literals use the string pool for efficiency.

## Before (Deprecated)

```java
String s1 = new String("hello");
String s2 = new String(s1);
String s3 = new String(bytes, "UTF-8");
```

## After (Modern)

```java
String s1 = "hello";  // uses string pool
String s2 = s1;  // same reference
String s3 = new String(bytes, StandardCharsets.UTF_8);
String s4 = String.valueOf(charArray);
```

## Key Differences

- Use string literals -- they use the string pool
- String.valueOf() for conversion without new
- Avoid new String() -- wastes memory

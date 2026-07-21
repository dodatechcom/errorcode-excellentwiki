---
title: "[Solution] Deprecated Function Migration: == to .equals() for string comparison"
description: "Migrate from deprecated == string comparison to .equals() and .equalsIgnoreCase() in Java."
deprecated_function: "str1 == str2"
replacement_function: "str1.equals(str2)"
languages: ["java"]
deprecated_since: "Java 1.0+"
---

# [Solution] Deprecated Function Migration: == to .equals() for string comparison

The `str1 == str2` has been deprecated in favor of `str1.equals(str2)`.

## Migration Guide

== compares references, not string content. Use .equals() for content comparison.

## Before (Deprecated)

```java
String a = new String("hello");
String b = new String("hello");
if (a == b) {  // always false for different objects
    System.out.println("equal");
}
```

## After (Modern)

```java
String a = new String("hello");
String b = new String("hello");
if (a.equals(b)) {  // true -- content comparison
    System.out.println("equal");
}

// Null-safe comparison
Objects.equals(a, b);

// Case-insensitive
a.equalsIgnoreCase(b);
```

## Key Differences

== compares object references
- .equals() compares string content
- Use Objects.equals() for null safety
- .equalsIgnoreCase() for case-insensitive

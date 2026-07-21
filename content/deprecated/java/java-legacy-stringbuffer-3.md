---
title: "[Solution] Deprecated Function Migration: StringBuffer for concatenation to StringBuilder"
description: "Migrate from deprecated StringBuffer concatenation to StringBuilder."
deprecated_function: "new StringBuffer().append()"
replacement_function: "new StringBuilder().append()"
languages: ["java"]
deprecated_since: "Java 1.5+"
---

# [Solution] Deprecated Function Migration: StringBuffer for concatenation to StringBuilder

The `new StringBuffer().append()` has been deprecated in favor of `new StringBuilder().append()`.

## Migration Guide

StringBuilder is faster for string concatenation

StringBuffer has synchronization overhead. StringBuilder is faster.

## Before (Deprecated)

```java
StringBuffer sb = new StringBuffer();
sb.append("Hello");
sb.append(" ");
sb.append(name);
return sb.toString();
```

## After (Modern)

```java
StringBuilder sb = new StringBuilder();
sb.append("Hello");
sb.append(" ");
sb.append(name);
return sb.toString();

// Or use String.join
return String.join(" ", "Hello", name);
```

## Key Differences

- StringBuilder is not synchronized
- String.join for joining strings
- String concatenation with + is optimized by compiler
- StringBuilder for complex string building

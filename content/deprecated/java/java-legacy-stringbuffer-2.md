---
title: "[Solution] Deprecated Function Migration: StringBuffer in single-thread to StringBuilder"
description: "Migrate from deprecated StringBuffer to StringBuilder for single-threaded string operations."
deprecated_function: "new StringBuffer()"
replacement_function: "new StringBuilder()"
languages: ["java"]
deprecated_since: "Java 1.5+"
---

# [Solution] Deprecated Function Migration: StringBuffer in single-thread to StringBuilder

The `new StringBuffer()` has been deprecated in favor of `new StringBuilder()`.

## Migration Guide

StringBuilder is faster without synchronization

StringBuffer has synchronization overhead. StringBuilder is faster for single-threaded use.

## Before (Deprecated)

```java
StringBuffer sb = new StringBuffer();
sb.append("SELECT ");
sb.append("* FROM ");
sb.append(table);
```

## After (Modern)

```java
StringBuilder sb = new StringBuilder();
sb.append("SELECT ");
sb.append("* FROM ");
sb.append(table);
String query = sb.toString();
```

## Key Differences

- StringBuilder is not synchronized
- Same API as StringBuffer
- Use StringBuffer only for thread safety
- StringBuilder is the default choice

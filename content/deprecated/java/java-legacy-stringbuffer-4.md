---
title: "[Solution] Deprecated Function Migration: StringBuffer for string building to StringBuilder"
description: "Migrate from deprecated StringBuffer to StringBuilder."
deprecated_function: "new StringBuffer()"
replacement_function: "new StringBuilder()"
languages: ["java"]
deprecated_since: "Java 1.5+"
---

# [Solution] Deprecated Function Migration: StringBuffer for string building to StringBuilder

The `new StringBuffer()` has been deprecated in favor of `new StringBuilder()`.

## Migration Guide

StringBuilder is faster without synchronization

StringBuffer synchronizes every method.

## Before (Deprecated)

```java
StringBuffer sb = new StringBuffer();
sb.append("Hello");
```

## After (Modern)

```java
StringBuilder sb = new StringBuilder();
sb.append("Hello");
```

## Key Differences

- StringBuilder is not synchronized
- Same API as StringBuffer
- Use StringBuffer only for thread safety

---
title: "[Solution] Deprecated Function Migration: StringBuffer to StringBuilder"
description: "Migrate from deprecated StringBuffer to StringBuilder."
deprecated_function: "StringBuffer"
replacement_function: "StringBuilder"
languages: ["java"]
deprecated_since: "Java 5+"
---

# [Solution] Deprecated Function Migration: StringBuffer to StringBuilder

The `StringBuffer` has been deprecated in favor of `StringBuilder`.

## Migration Guide

StringBuilder is not synchronized.

## Before (Deprecated)

```java
StringBuffer sb = new StringBuffer();
```

## After (Modern)

```java
StringBuilder sb = new StringBuilder();
```

## Key Differences

- StringBuilder is faster

---
title: "[Solution] Deprecated Function Migration: toCharArray to CharBuffer or direct access"
description: "Migrate from deprecated toCharArray for large strings to CharBuffer."
deprecated_function: "str.toCharArray()"
replacement_function: "CharBuffer.wrap(str)"
languages: ["java"]
deprecated_since: "Java NIO"
---

# [Solution] Deprecated Function Migration: toCharArray to CharBuffer or direct access

The `str.toCharArray()` has been deprecated in favor of `CharBuffer.wrap(str)`.

## Migration Guide

CharBuffer avoids copying.

## Before (Deprecated)

```java
char[] chars = str.toCharArray();
```

## After (Modern)

```java
CharBuffer buf = CharBuffer.wrap(str);
```

## Key Differences

- CharBuffer avoids copying

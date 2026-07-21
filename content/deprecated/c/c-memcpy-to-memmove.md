---
title: "[Solution] Deprecated Function Migration: memcpy to memmove for overlapping regions"
description: "Migrate from deprecated memcpy to memmove for overlapping memory regions."
deprecated_function: "memcpy(dest, src, n)"
replacement_function: "memmove(dest, src, n)"
languages: ["c"]
deprecated_since: "C89+"
---

# [Solution] Deprecated Function Migration: memcpy to memmove for overlapping regions

The `memcpy(dest, src, n)` has been deprecated in favor of `memmove(dest, src, n)`.

## Migration Guide

memmove handles overlapping regions safely

memcpy has undefined behavior with overlapping regions. memmove handles them correctly.

## Before (Deprecated)

```c
char buf[20] = "hello world";
memcpy(buf + 6, buf, 5);  // undefined behavior!
```

## After (Modern)

```c
char buf[20] = "hello world";
memmove(buf + 6, buf, 5);  // safe with overlap
// buf is now "hello hello world"
```

## Key Differences

- memmove handles overlapping regions
- memcpy is faster for non-overlapping
- Use memmove when overlap is possible
- Both have the same interface

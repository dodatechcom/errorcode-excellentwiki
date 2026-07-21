---
title: "[Solution] Deprecated Function Migration: memcpy to memmove for overlapping regions"
description: "Migrate from deprecated memcpy to memmove for overlapping regions."
deprecated_function: "memcpy(dest, src, n)"
replacement_function: "memmove(dest, src, n)"
languages: ["c"]
deprecated_since: "C89+"
---

# [Solution] Deprecated Function Migration: memcpy to memmove for overlapping regions

The `memcpy(dest, src, n)` has been deprecated in favor of `memmove(dest, src, n)`.

## Migration Guide

memmove handles overlapping regions

memcpy has undefined behavior with overlap.

## Before (Deprecated)

```c
memcpy(buf + 6, buf, 5);  // UB!
```

## After (Modern)

```c
memmove(buf + 6, buf, 5);  // safe
```

## Key Differences

- memmove handles overlapping regions
- memcpy is faster for non-overlap

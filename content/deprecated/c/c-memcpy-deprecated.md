---
title: "[Solution] Deprecated Function Migration: memcpy to memmove for overlapping regions"
description: "Migrate from deprecated memcpy to memmove for overlapping regions."
deprecated_function: "memcpy(dest, src, n)"
replacement_function: "memmove(dest, src, n)"
languages: ["c"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: memcpy to memmove for overlapping regions

The `memcpy(dest, src, n)` has been deprecated in favor of `memmove(dest, src, n)`.

## Migration Guide

memmove handles overlapping regions.

## Before (Deprecated)

```c
memcpy(dest, src, n);
```

## After (Modern)

```c
memmove(dest, src, n);
```

## Key Differences

- memmove handles overlapping regions

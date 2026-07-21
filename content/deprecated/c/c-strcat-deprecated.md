---
title: "[Solution] Deprecated Function Migration: strcat to strncat"
description: "Migrate from deprecated strcat to strncat."
deprecated_function: "strcat(dest, src)"
replacement_function: "strncat(dest, src, n)"
languages: ["c"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: strcat to strncat

The `strcat(dest, src)` has been deprecated in favor of `strncat(dest, src, n)`.

## Migration Guide

strncat prevents buffer overflow.

## Before (Deprecated)

```c
strcat(dest, src);
```

## After (Modern)

```c
strncat(dest, src, sizeof(dest) - strlen(dest) - 1);
```

## Key Differences

- strncat prevents buffer overflow

---
title: "[Solution] Deprecated Function Migration: strncpy to strlcpy"
description: "Migrate from deprecated strncpy to strlcpy."
deprecated_function: "strncpy(dest, src, n)"
replacement_function: "strlcpy(dest, src, n)"
languages: ["c"]
deprecated_since: "BSD / POSIX"
---

# [Solution] Deprecated Function Migration: strncpy to strlcpy

The `strncpy(dest, src, n)` has been deprecated in favor of `strlcpy(dest, src, n)`.

## Migration Guide

strlcpy always null-terminates

strncpy may not null-terminate.

## Before (Deprecated)

```c
strncpy(dest, "long string", sizeof(dest));
```

## After (Modern)

```c
strlcpy(dest, "long string", sizeof(dest));
```

## Key Differences

- strlcpy always null-terminates
- strncpy may not

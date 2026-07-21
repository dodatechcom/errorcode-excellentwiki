---
title: "[Solution] Deprecated Function Migration: strlen to strnlen for safety"
description: "Migrate from deprecated strlen to strnlen for bounded operations."
deprecated_function: "strlen(str)"
replacement_function: "strnlen(str, max_len)"
languages: ["c"]
deprecated_since: "POSIX"
---

# [Solution] Deprecated Function Migration: strlen to strnlen for safety

The `strlen(str)` has been deprecated in favor of `strnlen(str, max_len)`.

## Migration Guide

strnlen prevents reading past buffer.

## Before (Deprecated)

```c
size_t len = strlen(str);
```

## After (Modern)

```c
size_t len = strnlen(str, MAX_LEN);
```

## Key Differences

- strnlen prevents reading past buffer

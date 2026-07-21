---
title: "[Solution] Deprecated Function Migration: malloc + memset to calloc"
description: "Migrate from deprecated malloc + memset to calloc."
deprecated_function: "malloc(n * size); memset(ptr, 0, n * size)"
replacement_function: "calloc(n, size)"
languages: ["c"]
deprecated_since: "C89"
---

# [Solution] Deprecated Function Migration: malloc + memset to calloc

The `malloc(n * size); memset(ptr, 0, n * size)` has been deprecated in favor of `calloc(n, size)`.

## Migration Guide

calloc initializes memory to zero.

## Before (Deprecated)

```c
int *arr = malloc(10 * sizeof(int));
memset(arr, 0, 10 * sizeof(int));
```

## After (Modern)

```c
int *arr = calloc(10, sizeof(int));
```

## Key Differences

- calloc initializes to zero

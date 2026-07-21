---
title: "[Solution] Deprecated Function Migration: realloc to safe realloc pattern"
description: "Migrate from deprecated unsafe realloc to safe realloc pattern."
deprecated_function: "ptr = realloc(ptr, size)"
replacement_function: "safe_realloc(&ptr, size)"
languages: ["c"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: realloc to safe realloc pattern

The `ptr = realloc(ptr, size)` has been deprecated in favor of `safe_realloc(&ptr, size)`.

## Migration Guide

realloc can lose original pointer on failure.

## Before (Deprecated)

```c
ptr = realloc(ptr, new_size);
```

## After (Modern)

```c
void *tmp = realloc(ptr, new_size);
if (tmp == NULL) { /* handle error */ }
ptr = tmp;
```

## Key Differences

- Always check realloc return

---
title: "[Solution] Deprecated Function Migration: strtok to strtok_r for thread safety"
description: "Migrate from deprecated strtok to strtok_r for thread safety."
deprecated_function: "strtok(str, delim)"
replacement_function: "strtok_r(str, delim, &saveptr)"
languages: ["c"]
deprecated_since: "POSIX"
---

# [Solution] Deprecated Function Migration: strtok to strtok_r for thread safety

The `strtok(str, delim)` has been deprecated in favor of `strtok_r(str, delim, &saveptr)`.

## Migration Guide

strtok is not thread-safe.

## Before (Deprecated)

```c
char *token = strtok(str, ",");
```

## After (Modern)

```c
char *saveptr;
char *token = strtok_r(str, ",", &saveptr);
```

## Key Differences

- strtok_r is thread-safe

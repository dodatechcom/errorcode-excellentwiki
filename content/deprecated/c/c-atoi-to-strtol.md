---
title: "[Solution] Deprecated Function Migration: atoi to strtol"
description: "Migrate from deprecated atoi to strtol."
deprecated_function: "atoi(str)"
replacement_function: "strtol(str, NULL, 10)"
languages: ["c"]
deprecated_since: "C89+"
---

# [Solution] Deprecated Function Migration: atoi to strtol

The `atoi(str)` has been deprecated in favor of `strtol(str, NULL, 10)`.

## Migration Guide

strtol provides error detection

atoi cannot detect errors.

## Before (Deprecated)

```c
int val = atoi("123");
```

## After (Modern)

```c
char *endptr;
long val = strtol("123", &endptr, 10);
```

## Key Differences

- strtol provides error detection
- endptr shows where parsing stopped

---
title: "[Solution] Deprecated Function Migration: mutable pointer to const-correct pointer"
description: "Migrate from deprecated mutable pointer to const-correct pointer."
deprecated_function: "char *str"
replacement_function: "const char *str"
languages: ["c"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: mutable pointer to const-correct pointer

The `char *str` has been deprecated in favor of `const char *str`.

## Migration Guide

const-correctness prevents accidental modification.

## Before (Deprecated)

```c
void process(char *str) {
    // might accidentally modify
}
```

## After (Modern)

```c
void process(const char *str) {
    // cannot modify
}
```

## Key Differences

- const-correctness prevents bugs

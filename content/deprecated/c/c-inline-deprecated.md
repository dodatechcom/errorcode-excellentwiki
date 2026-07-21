---
title: "[Solution] Deprecated Function Migration: inline in header to static inline"
description: "Migrate from deprecated inline to static inline for header functions."
deprecated_function: "inline int add(int a, int b) { return a + b; }"
replacement_function: "static inline int add(int a, int b) { return a + b; }"
languages: ["c"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: inline in header to static inline

The `inline int add(int a, int b) { return a + b; }` has been deprecated in favor of `static inline int add(int a, int b) { return a + b; }`.

## Migration Guide

static inline prevents multiple definition.

## Before (Deprecated)

```c
inline int add(int a, int b) { return a + b; }
```

## After (Modern)

```c
static inline int add(int a, int b) { return a + b; }
```

## Key Differences

- static inline prevents linker errors

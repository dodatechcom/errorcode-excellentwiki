---
title: "[Solution] Deprecated Function Migration: global variables to static for file scope"
description: "Migrate from deprecated global variables to static for file scope."
deprecated_function: "int counter; // global"
replacement_function: "static int counter; // file scope"
languages: ["c"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: global variables to static for file scope

The `int counter; // global` has been deprecated in favor of `static int counter; // file scope`.

## Migration Guide

static limits scope to file.

## Before (Deprecated)

```c
int counter = 0;  // visible everywhere
```

## After (Modern)

```c
static int counter = 0;  // file scope only
```

## Key Differences

- static limits scope to file

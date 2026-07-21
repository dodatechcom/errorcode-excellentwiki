---
title: "[Solution] Deprecated Function Migration: void* to std::any"
description: "Migrate from deprecated void* to std::any."
deprecated_function: "void* ptr"
replacement_function: "std::any"
languages: ["cpp"]
deprecated_since: "C++17"
---

# [Solution] Deprecated Function Migration: void* to std::any

The `void* ptr` has been deprecated in favor of `std::any`.

## Migration Guide

any is type-safe.

## Before (Deprecated)

```cpp
void* data = &value;
```

## After (Modern)

```cpp
std::any data = value;
```

## Key Differences

- any is type-safe

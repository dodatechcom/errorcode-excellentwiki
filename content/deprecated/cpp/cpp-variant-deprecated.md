---
title: "[Solution] Deprecated Function Migration: union to std::variant"
description: "Migrate from deprecated union to std::variant."
deprecated_function: "union Data { int i; float f; }"
replacement_function: "std::variant<int, float>"
languages: ["cpp"]
deprecated_since: "C++17"
---

# [Solution] Deprecated Function Migration: union to std::variant

The `union Data { int i; float f; }` has been deprecated in favor of `std::variant<int, float>`.

## Migration Guide

variant is type-safe.

## Before (Deprecated)

```cpp
union Data {
    int i;
    float f;
};
```

## After (Modern)

```cpp
std::variant<int, float> data;
```

## Key Differences

- variant is type-safe

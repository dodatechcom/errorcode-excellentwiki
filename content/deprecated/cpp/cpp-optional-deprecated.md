---
title: "[Solution] Deprecated Function Migration: pointer parameters to std::optional"
description: "Migrate from deprecated pointer parameters to std::optional."
deprecated_function: "T* ptr (nullable)"
replacement_function: "std::optional<T>"
languages: ["cpp"]
deprecated_since: "C++17"
---

# [Solution] Deprecated Function Migration: pointer parameters to std::optional

The `T* ptr (nullable)` has been deprecated in favor of `std::optional<T>`.

## Migration Guide

optional is more expressive.

## Before (Deprecated)

```cpp
void process(int* value);
```

## After (Modern)

```cpp
void process(std::optional<int> value);
```

## Key Differences

- optional is more expressive

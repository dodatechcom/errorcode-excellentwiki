---
title: "[Solution] Deprecated Function Migration: auto_ptr to unique_ptr"
description: "Migrate from deprecated auto_ptr to unique_ptr."
deprecated_function: "auto_ptr<T>"
replacement_function: "unique_ptr<T>"
languages: ["cpp"]
deprecated_since: "C++11"
---

# [Solution] Deprecated Function Migration: auto_ptr to unique_ptr

The `auto_ptr<T>` has been deprecated in favor of `unique_ptr<T>`.

## Migration Guide

auto_ptr was removed in C++17.

## Before (Deprecated)

```cpp
auto_ptr<int> p(new int(42));
```

## After (Modern)

```cpp
unique_ptr<int> p = make_unique<int>(42);
```

## Key Differences

- unique_ptr is the modern replacement

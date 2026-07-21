---
title: "[Solution] Deprecated Function Migration: index-based for to range-based for"
description: "Migrate from deprecated index-based for to range-based for."
deprecated_function: "for (int i = 0; i < vec.size(); i++)"
replacement_function: "for (const auto& item : vec)"
languages: ["cpp"]
deprecated_since: "C++11"
---

# [Solution] Deprecated Function Migration: index-based for to range-based for

The `for (int i = 0; i < vec.size(); i++)` has been deprecated in favor of `for (const auto& item : vec)`.

## Migration Guide

range-based for is cleaner.

## Before (Deprecated)

```cpp
for (int i = 0; i < vec.size(); i++) {
    process(vec[i]);
}
```

## After (Modern)

```cpp
for (const auto& item : vec) {
    process(item);
}
```

## Key Differences

- range-based for is cleaner

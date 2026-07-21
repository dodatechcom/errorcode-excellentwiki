---
title: "[Solution] Deprecated Function Migration: ptr_fun to function"
description: "Migrate from deprecated ptr_fun to function."
deprecated_function: "ptr_fun(func)"
replacement_function: "function"
languages: ["cpp"]
deprecated_since: "C++11"
---

# [Solution] Deprecated Function Migration: ptr_fun to function

The `ptr_fun(func)` has been deprecated in favor of `function`.

## Migration Guide

ptr_fun was removed in C++17.

## Before (Deprecated)

```cpp
transform(v.begin(), v.end(), out.begin(), ptr_fun(toupper));
```

## After (Modern)

```cpp
transform(v.begin(), v.end(), out.begin(), ::toupper);
```

## Key Differences

- ptr_fun was removed in C++17

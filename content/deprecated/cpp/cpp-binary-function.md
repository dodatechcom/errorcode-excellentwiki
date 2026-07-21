---
title: "[Solution] Deprecated Function Migration: binary_function to custom struct"
description: "Migrate from deprecated binary_function to custom struct."
deprecated_function: "struct Comp : binary_function<T,T,bool> {}"
replacement_function: "struct Comp { bool operator()(T a, T b) const {} }"
languages: ["cpp"]
deprecated_since: "C++11"
---

# [Solution] Deprecated Function Migration: binary_function to custom struct

The `struct Comp : binary_function<T,T,bool> {}` has been deprecated in favor of `struct Comp { bool operator()(T a, T b) const {} }`.

## Migration Guide

binary_function was removed in C++17.

## Before (Deprecated)

```cpp
struct Comp : binary_function<int,int,bool> {
    bool operator()(int a, int b) const { return a < b; }
}
```

## After (Modern)

```cpp
struct Comp {
    bool operator()(int a, int b) const { return a < b; }
};
```

## Key Differences

- binary_function was removed in C++17

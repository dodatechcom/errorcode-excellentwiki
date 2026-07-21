---
title: "[Solution] Deprecated Function Migration: unary_function to custom struct"
description: "Migrate from deprecated unary_function to custom struct."
deprecated_function: "struct Pred : unary_function<T,bool> {}"
replacement_function: "struct Pred { bool operator()(T x) const {} }"
languages: ["cpp"]
deprecated_since: "C++11"
---

# [Solution] Deprecated Function Migration: unary_function to custom struct

The `struct Pred : unary_function<T,bool> {}` has been deprecated in favor of `struct Pred { bool operator()(T x) const {} }`.

## Migration Guide

unary_function was removed in C++17.

## Before (Deprecated)

```cpp
struct Pred : unary_function<int,bool> {
    bool operator()(int x) const { return x > 0; }
}
```

## After (Modern)

```cpp
struct Pred {
    bool operator()(int x) const { return x > 0; }
};
```

## Key Differences

- unary_function was removed in C++17

---
title: "[Solution] Deprecated Function Migration: new/delete to make_unique/make_shared"
description: "Migrate from deprecated new/delete to make_unique/make_shared."
deprecated_function: "new T(args)"
replacement_function: "std::make_unique<T>(args)"
languages: ["cpp"]
deprecated_since: "C++14/C++11"
---

# [Solution] Deprecated Function Migration: new/delete to make_unique/make_shared

The `new T(args)` has been deprecated in favor of `std::make_unique<T>(args)`.

## Migration Guide

Smart pointers prevent memory leaks.

## Before (Deprecated)

```cpp
MyClass* ptr = new MyClass(args);
```

## After (Modern)

```cpp
auto ptr = std::make_unique<MyClass>(args);
```

## Key Differences

- Smart pointers prevent memory leaks

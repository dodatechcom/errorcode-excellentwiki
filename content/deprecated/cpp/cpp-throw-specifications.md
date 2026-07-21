---
title: "[Solution] Deprecated Function Migration: throw() to noexcept"
description: "Migrate from deprecated dynamic exception specifications to noexcept in C++."
deprecated_function: "throw(Type)"
replacement_function: "noexcept"
languages: ["cpp"]
deprecated_since: "C++11 deprecated, C++17 removed"
---

# [Solution] Deprecated Function Migration: throw() to noexcept

The `throw(Type)` has been deprecated in favor of `noexcept`.

## Migration Guide

Dynamic exception specifications were removed in C++17. Use noexcept to indicate a function does not throw.

## Before (Deprecated)

```cpp
void func() throw(std::runtime_error) {
    throw std::runtime_error("error");
}

void nothrow() throw() {
    // never throws
}
```

## After (Modern)

```cpp
void func() noexcept(false) {
    throw std::runtime_error("error");
}

void nothrow() noexcept {
    // promise not to throw
}
```

## Key Differences

- throw() replaced by noexcept
- noexcept(true) is the default for destructors
- noexcept(false) for functions that may throw
- Moved/swap operations should be noexcept

---
title: "[Solution] Deprecated Function Migration: auto_ptr to unique_ptr"
description: "Migrate from deprecated std::auto_ptr to std::unique_ptr for exclusive ownership in C++."
deprecated_function: "std::auto_ptr"
replacement_function: "std::unique_ptr"
languages: ["cpp"]
deprecated_since: "C++11"
---

# [Solution] Deprecated Function Migration: auto_ptr to unique_ptr

The `std::auto_ptr` has been deprecated in favor of `std::unique_ptr`.

## Migration Guide

auto_ptr had confusing ownership transfer semantics. unique_ptr provides clear exclusive ownership with move semantics.

## Before (Deprecated)

```cpp
#include <memory>

auto_ptr<MyClass> ptr1(new MyClass());
auto_ptr<MyClass> ptr2 = ptr1;  // ptr1 is now NULL!
```

## After (Modern)

```cpp
#include <memory>

unique_ptr<MyClass> ptr1 = make_unique<MyClass>();
unique_ptr<MyClass> ptr2 = move(ptr1);  // explicit move

// Shared ownership when needed
shared_ptr<MyClass> shared = make_shared<MyClass>();
```

## Key Differences

- Use unique_ptr for exclusive ownership
- Use shared_ptr for shared ownership
- make_unique/make_shared for safe construction
- Move semantics are explicit with std::move

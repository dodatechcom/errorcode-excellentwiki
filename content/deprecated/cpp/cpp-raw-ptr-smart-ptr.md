---
title: "[Solution] Deprecated Function Migration: raw new/delete to smart pointers"
description: "Migrate from deprecated raw pointer ownership to smart pointers in C++."
deprecated_function: "Raw new/delete"
replacement_function: "unique_ptr / shared_ptr / weak_ptr"
languages: ["cpp"]
deprecated_since: "C++11+"
---

# [Solution] Deprecated Function Migration: raw new/delete to smart pointers

The `Raw new/delete` has been deprecated in favor of `unique_ptr / shared_ptr / weak_ptr`.

## Migration Guide

Smart pointers manage lifetime automatically through RAII, preventing memory leaks.

## Before (Deprecated)

```cpp
MyClass* ptr = new MyClass();
ptr->doSomething();
// Easy to forget delete

MyClass* observer = nullptr;
```

## After (Modern)

```cpp
auto ptr = make_unique<MyClass>();
ptr->doSomething();
// Automatically deleted

auto shared = make_shared<MyClass>();
auto weak = weak_ptr<MyClass>(shared);
```

## Key Differences

- unique_ptr for exclusive ownership
- shared_ptr for shared ownership
- weak_ptr for non-owning references
- make_unique/make_shared for safe construction

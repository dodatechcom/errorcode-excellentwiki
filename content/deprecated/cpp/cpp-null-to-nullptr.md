---
title: "[Solution] Deprecated Function Migration: NULL to nullptr"
description: "Migrate from deprecated NULL macro to nullptr for type-safe null pointers in C++."
deprecated_function: "NULL"
replacement_function: "nullptr"
languages: ["cpp"]
deprecated_since: "C++11"
---

# [Solution] Deprecated Function Migration: NULL to nullptr

The `NULL` has been deprecated in favor of `nullptr`.

## Migration Guide

nullptr is a pointer literal of type std::nullptr_t. NULL is a macro that can cause ambiguities.

## Before (Deprecated)

```cpp
void func(int x);
void func(char* p);

func(NULL);   // Ambiguous -- calls func(int)!
```

## After (Modern)

```cpp
void func(int x);
void func(char* p);

func(nullptr);  // Calls func(char*) -- type-safe
```

## Key Differences

- nullptr is type-safe for pointer contexts
- NULL can cause ambiguous overloads
- nullptr cannot be implicitly converted to int
- Use nullptr for all pointer null values

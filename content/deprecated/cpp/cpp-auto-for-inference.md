---
title: "[Solution] Deprecated Function Migration: verbose type declarations to auto"
description: "Migrate from verbose type declarations to auto for type inference in C++."
deprecated_function: "Explicit type everywhere"
replacement_function: "auto with type inference"
languages: ["cpp"]
deprecated_since: "C++11+"
---

# [Solution] Deprecated Function Migration: verbose type declarations to auto

The `Explicit type everywhere` has been deprecated in favor of `auto with type inference`.

## Migration Guide

auto reduces verbosity where type is obvious from context.

## Before (Deprecated)

```cpp
std::vector<std::string>::iterator it = vec.begin();
std::map<std::string, int>::iterator it2 = map.find("key");
auto x = std::make_shared<MyClass>(new MyClass());
```

## After (Modern)

```cpp
auto it = vec.begin();
auto it2 = map.find("key");
auto x = std::make_shared<MyClass>();

// When type is not obvious, be explicit
int count = calculateCount();
```

## Key Differences

- Use auto when type is obvious
- Be explicit when type is not obvious
- auto makes refactoring easier
- Use with iterators, lambdas, complex types

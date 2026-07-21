---
title: "[Solution] Deprecated Function Migration: const string& to string_view"
description: "Migrate from deprecated const string& to string_view for read-only parameters."
deprecated_function: "const std::string& str"
replacement_function: "std::string_view str"
languages: ["cpp"]
deprecated_since: "C++17"
---

# [Solution] Deprecated Function Migration: const string& to string_view

The `const std::string& str` has been deprecated in favor of `std::string_view str`.

## Migration Guide

string_view avoids allocation.

## Before (Deprecated)

```cpp
void process(const std::string& str);
```

## After (Modern)

```cpp
void process(std::string_view str);
```

## Key Differences

- string_view avoids allocation

---
title: "[Solution] Deprecated Function Migration: gets() to std::getline"
description: "Migrate from removed gets() to std::getline for safe string input in C++."
deprecated_function: "gets()"
replacement_function: "std::getline()"
languages: ["cpp"]
deprecated_since: "C++11 deprecated, C++14 removed"
---

# [Solution] Deprecated Function Migration: gets() to std::getline

The `gets()` has been deprecated in favor of `std::getline()`.

## Migration Guide

gets() was removed from C++14 because it has no buffer overflow protection.

## Before (Deprecated)

```cpp
#include <cstdio>

char buffer[100];
gets(buffer);  // DANGEROUS
```

## After (Modern)

```cpp
#include <iostream>
#include <string>

std::string input;
std::getline(std::cin, input);

// With delimited reading
char buffer[100];
std::cin.getline(buffer, 100);
```

## Key Differences

- gets() is removed from C++14
- std::getline() reads with bounds checking
- Use std::string for dynamic sizing
- Always limit input buffer size

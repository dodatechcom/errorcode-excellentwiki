---
title: "[Solution] Deprecated Function Migration: bind1st/bind2nd to std::bind or lambdas"
description: "Migrate from deprecated bind1st/bind2nd to std::bind or lambdas in C++."
deprecated_function: "std::bind1st / std::bind2nd"
replacement_function: "std::bind / lambdas"
languages: ["cpp"]
deprecated_since: "C++11 (removed C++17)"
---

# [Solution] Deprecated Function Migration: bind1st/bind2nd to std::bind or lambdas

The `std::bind1st / std::bind2nd` has been deprecated in favor of `std::bind / lambdas`.

## Migration Guide

bind1st and bind2nd were removed in C++17. Lambdas are usually more readable.

## Before (Deprecated)

```cpp
#include <functional>
#include <algorithm>

std::count_if(vec.begin(), vec.end(),
    std::bind1st(std::greater<int>(), 10));
```

## After (Modern)

```cpp
#include <functional>
#include <algorithm>

// Using lambdas (preferred)
std::count_if(vec.begin(), vec.end(),
    [](int x) { return x > 10; });

// Using std::bind
std::bind(std::plus<int>(), 10, std::placeholders::_1);
```

## Key Differences

- bind1st/bind2nd removed in C++17
- std::bind is the direct replacement
- Lambdas are more readable for most cases

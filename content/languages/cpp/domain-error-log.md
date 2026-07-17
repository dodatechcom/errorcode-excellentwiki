---
title: "[Solution] C++ std::domain_error - log of zero/negative"
description: "Fix C++ std::domain_error from log of zero or negative. Validate arguments before logarithm."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["domain-error", "log", "logarithm", "zero", "negative"]
weight: 5
---

# std::domain_error - log of zero/negative

`std::domain_error` is thrown when `std::log` or `std::log2` or `std::log10` receives zero or a negative argument.

## Common Causes

```cpp
// Cause 1: log of zero
double result = std::log(0.0); // -infinity, may throw

// Cause 2: log of negative
double result = std::log(-1.0); // domain error

// Cause 3: log2 of zero
double result = std::log2(0.0); // -infinity
```

## How to Fix

### Fix 1: Validate input

```cpp
double safe_log(double x) {
    if (x <= 0) throw std::domain_error("log of non-positive");
    return std::log(x);
}
```

### Fix 2: Check before calling

```cpp
if (x > 0) {
    double result = std::log(x);
}
```

### Fix 3: Use log1p for small values

```cpp
double safe_log1p(double x) {
    if (x <= -1) throw std::domain_error("log1p argument <= -1");
    return std::log1p(x);
}
```

## Related Errors

- [std::domain_error - sqrt]({{< relref "/languages/cpp/domain-error-sqrt" >}}) — sqrt of negative.
- [std::domain_error - acos]({{< relref "/languages/cpp/domain-error-acos" >}}) — acos out of range.
- [std::domain_error - asin]({{< relref "/languages/cpp/domain-error-asin" >}}) — asin out of range.

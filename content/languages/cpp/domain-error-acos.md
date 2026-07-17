---
title: "[Solution] C++ std::domain_error - acos domain error"
description: "Fix C++ std::domain_error from acos with out-of-range argument. Clamp to [-1, 1]."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["domain-error", "acos", "arccosine", "trigonometry", "domain"]
weight: 5
---

# std::domain_error - acos domain error

`std::domain_error` is thrown when `std::acos` receives an argument outside [-1, 1]. Due to floating-point precision, values like 1.0000000001 can appear.

## Common Causes

```cpp
// Cause 1: Argument > 1
double result = std::acos(1.1); // domain error

// Cause 2: Argument < -1
double result = std::acos(-1.1); // domain error

// Cause 3: Floating-point precision
double result = std::acos(std::cos(M_PI)); // may be slightly > 1
```

## How to Fix

### Fix 1: Clamp argument

```cpp
double safe_acos(double x) {
    x = std::max(-1.0, std::min(1.0, x));
    return std::acos(x);
}
```

### Fix 2: Check before calling

```cpp
if (x >= -1.0 && x <= 1.0) {
    double angle = std::acos(x);
}
```

### Fix 3: Use asin for better range

```cpp
double angle = std::asin(std::sqrt(1 - x * x));
```

## Related Errors

- [std::domain_error - asin]({{< relref "/languages/cpp/domain-error-asin" >}}) — asin domain error.
- [std::domain_error - sqrt]({{< relref "/languages/cpp/domain-error-sqrt" >}}) — sqrt of negative.
- [std::domain_error - log]({{< relref "/languages/cpp/domain-error-log" >}}) — log domain error.

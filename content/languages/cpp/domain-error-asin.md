---
title: "[Solution] C++ std::domain_error - asin domain error"
description: "Fix C++ std::domain_error from asin with out-of-range argument. Clamp to [-1, 1]."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["domain-error", "asin", "arcsine", "trigonometry", "domain"]
weight: 5
---

# std::domain_error - asin domain error

`std::domain_error` is thrown when `std::asin` receives an argument outside [-1, 1].

## Common Causes

```cpp
// Cause 1: Argument > 1
double result = std::asin(1.1); // domain error

// Cause 2: Argument < -1
double result = std::asin(-1.1); // domain error

// Cause 3: Precision issue
double x = 1.0000000001;
double result = std::asin(x); // may throw
```

## How to Fix

### Fix 1: Clamp argument

```cpp
double safe_asin(double x) {
    x = std::max(-1.0, std::min(1.0, x));
    return std::asin(x);
}
```

### Fix 2: Use atan2 for robust angle calculation

```cpp
double angle = std::atan2(y, x); // always safe
```

### Fix 3: Check before calling

```cpp
if (std::abs(x) <= 1.0) {
    double angle = std::asin(x);
}
```

## Related Errors

- [std::domain_error - acos]({{< relref "/languages/cpp/domain-error-acos" >}}) — acos domain error.
- [std::domain_error - sqrt]({{< relref "/languages/cpp/domain-error-sqrt" >}}) — sqrt of negative.
- [std::domain_error - log]({{< relref "/languages/cpp/domain-error-log" >}}) — log domain error.

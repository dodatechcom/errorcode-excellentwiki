---
title: "[Solution] C++ std::domain_error - pow function error"
description: "Fix C++ std::domain_error from pow function. Handle invalid pow arguments."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::domain_error - pow function error

`std::domain_error` from `std::pow` occurs when arguments are mathematically invalid, such as negative base with fractional exponent.

## Common Causes

```cpp
// Cause 1: Negative base with fractional exponent
double result = std::pow(-1.0, 0.5); // domain error

// Cause 2: 0^negative
double result = std::pow(0.0, -1.0); // domain error (infinity)

// Cause 3: Complex result
double result = std::pow(-2.0, 1.5); // domain error
```

## How to Fix

### Fix 1: Validate before calling

```cpp
double safe_pow(double base, double exp) {
    if (base < 0 && exp != std::floor(exp)) {
        throw std::domain_error("negative base with fractional exponent");
    }
    return std::pow(base, exp);
}
```

### Fix 2: Use std::abs for negative bases

```cpp
double result = std::pow(std::abs(-1.0), 0.5);
```

### Fix 3: Use complex pow

```cpp
#include <complex>
auto result = std::pow(std::complex<double>(-1, 0), 0.5);
```

## Related Errors

- [std::domain_error - sqrt]({{< relref "/languages/cpp/domain-error-sqrt" >}}) — sqrt of negative.
- [std::domain_error - log]({{< relref "/languages/cpp/domain-error-log" >}}) — log of zero.
- [std::domain_error - acos]({{< relref "/languages/cpp/domain-error-acos" >}}) — acos out of range.

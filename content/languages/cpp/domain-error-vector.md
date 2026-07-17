---
title: "[Solution] C++ std::domain_error - math domain error"
description: "Fix C++ std::domain_error from math domain errors. Validate arguments before math functions."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["domain-error", "math", "domain", "sqrt", "log", "acos"]
weight: 5
---

# std::domain_error - math domain error

`std::domain_error` is thrown when a math function receives an argument outside its valid mathematical domain.

## Common Causes

```cpp
// Cause 1: sqrt of negative
double result = std::sqrt(-1.0); // domain error

// Cause 2: log of zero or negative
double result = std::log(-1.0); // domain error

// Cause 3: acos with value > 1
double result = std::acos(2.0); // domain error
```

## How to Fix

### Fix 1: Validate before math

```cpp
double safe_sqrt(double x) {
    if (x < 0) throw std::domain_error("sqrt of negative");
    return std::sqrt(x);
}
```

### Fix 2: Use complex numbers

```cpp
#include <complex>
std::complex<double> result = std::sqrt(std::complex<double>(-1, 0));
```

### Fix 3: Clamp values

```cpp
double safe_acos(double x) {
    x = std::max(-1.0, std::min(1.0, x));
    return std::acos(x);
}
```

## Related Errors

- [std::domain_error - sqrt]({{< relref "/languages/cpp/domain-error-sqrt" >}}) — sqrt specific.
- [std::domain_error - log]({{< relref "/languages/cpp/domain-error-log" >}}) — log specific.
- [std::domain_error - acos]({{< relref "/languages/cpp/domain-error-acos" >}}) — acos specific.

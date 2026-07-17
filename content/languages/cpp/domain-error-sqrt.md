---
title: "[Solution] C++ std::domain_error - sqrt of negative"
description: "Fix C++ std::domain_error from sqrt of negative number. Use std::abs or complex numbers."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::domain_error - sqrt of negative

`std::domain_error` is thrown when `std::sqrt` receives a negative argument (for real number output).

## Common Causes

```cpp
// Cause 1: Direct negative
double result = std::sqrt(-4.0); // domain error

// Cause 2: Variable becomes negative
double x = get_value(); // may be negative
double root = std::sqrt(x); // throws if x < 0

// Cause 3: Expression producing negative
double result = std::sqrt(a - b); // if a < b
```

## How to Fix

### Fix 1: Check before calling

```cpp
double safe_sqrt(double x) {
    if (x < 0) throw std::domain_error("sqrt of negative");
    return std::sqrt(x);
}
```

### Fix 2: Use std::abs

```cpp
double result = std::sqrt(std::abs(x)); // always positive
```

### Fix 3: Use complex numbers

```cpp
#include <complex>
auto result = std::sqrt(std::complex<double>(x, 0));
```

## Related Errors

- [std::domain_error - pow]({{< relref "/languages/cpp/domain-error-pow" >}}) — pow domain error.
- [std::domain_error - log]({{< relref "/languages/cpp/domain-error-log" >}}) — log domain error.
- [std::domain_error - acos]({{< relref "/languages/cpp/domain-error-acos" >}}) — acos domain error.

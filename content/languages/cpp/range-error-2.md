---
title: "[Solution] C++ std::range_error — Result Out of Range Fix"
description: "Fix C++ std::range_error when mathematically valid computations produce results outside representable range. Handle range violations safely."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["range-error", "math", "computation", "exception"]
weight: 5
---

# [Solution] C++ std::range_error — Result Out of Range Fix

A `std::range_error` is thrown when a mathematically valid computation produces a result that cannot be represented in the destination type. Unlike `std::domain_error` (invalid input), the input is valid but the output is too large or too small. For example, `std::tgamma(171)` overflows for `double`. It inherits from `std::runtime_error`.

## Why std::range_error Occurs

Common causes include computing factorials of large numbers that exceed double range, exponentiating large values (`std::exp(1000)`), computing trigonometric functions with very large arguments, and library functions that use `ERANGE` from `<cerrno>`.

## Wrong: Unchecked Range-Producing Computation

```cpp
// WRONG — result may be infinity
#include <cmath>
#include <iostream>

int main() {
    double result = std::tgamma(180);  // overflow to infinity
    std::cout << "Gamma(180) = " << result << std::endl;
    return 0;
}
```

## Correct: Validate Result After Computation

```cpp
// CORRECT — check result after math operation
#include <cmath>
#include <iostream>
#include <limits>
#include <stdexcept>

double safe_tgamma(double x) {
    double result = std::tgamma(x);
    if (std::isinf(result)) {
        throw std::range_error("tgamma overflow: result is infinity");
    }
    if (std::isnan(result)) {
        throw std::range_error("tgamma produced NaN");
    }
    return result;
}

int main() {
    try {
        std::cout << "Gamma(5) = " << safe_tgamma(5) << std::endl;
        std::cout << "Gamma(180) = " << safe_tgamma(180) << std::endl;
    } catch (const std::range_error& e) {
        std::cerr << "Range error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Safe Exponentiation

```cpp
// CORRECT — check exponentiation result
#include <cmath>
#include <iostream>
#include <limits>
#include <stdexcept>

double safe_exp(double x) {
    if (x > 709.0) {
        throw std::range_error("exp(" + std::to_string(x) + ") would overflow");
    }
    if (x < -745.0) {
        throw std::range_error("exp(" + std::to_string(x) + ") would underflow to zero");
    }
    return std::exp(x);
}

int main() {
    try {
        std::cout << "exp(1) = " << safe_exp(1) << std::endl;
        std::cout << "exp(1000) = " << safe_exp(1000) << std::endl;
    } catch (const std::range_error& e) {
        std::cerr << "Range error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Check for `inf` or `NaN` after computation | When math results may overflow |
| Clamp inputs to safe ranges | When inputs could produce out-of-range results |
| Use log-space computations | When dealing with very large/small values |
| Validate before calling math functions | When inputs come from external sources |

## Related Errors

- [std::overflow_error]({{< relref "/languages/cpp/overflowerror" >}}) — arithmetic overflow.
- [std::underflow_error]({{< relref "/languages/cpp/underflowerror" >}}) — arithmetic underflow.
- [std::domain_error]({{< relref "/languages/cpp/domainerror" >}}) — mathematical domain errors.

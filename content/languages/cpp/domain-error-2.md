---
title: "[Solution] C++ std::domain_error — Mathematical Domain Error Fix"
description: "Fix C++ std::domain_error when mathematical functions receive inputs outside their valid domain. Handle domain violations and invalid inputs."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["domain-error", "math", "domain", "exception"]
weight: 5
---

# [Solution] C++ std::domain_error — Mathematical Domain Error Fix

A `std::domain_error` is thrown when a mathematical function is called with an argument outside its valid domain. For example, taking the square root of a negative number, computing the log of zero, or applying an inverse trigonometric function to a value outside [-1, 1]. It inherits from `std::logic_error`.

## Why std::domain_error Occurs

Common causes include computing `sqrt()` of a negative number, computing `log()` or `log10()` of zero or a negative number, applying `asin()` or `acos()` to values outside [-1, 1], and custom mathematical functions receiving invalid inputs.

## Wrong: Computing sqrt of Negative Number

```cpp
// WRONG — undefined behavior for negative input
#include <cmath>
#include <iostream>

int main() {
    double result = std::sqrt(-1.0);  // NaN — no exception by default
    std::cout << result << std::endl;
    return 0;
}
```

## Correct: Validate Domain Before Computation

```cpp
// CORRECT — validate input before math operations
#include <cmath>
#include <iostream>
#include <stdexcept>

double safe_sqrt(double x) {
    if (x < 0) {
        throw std::domain_error("sqrt: argument must be non-negative (got " +
                                 std::to_string(x) + ")");
    }
    return std::sqrt(x);
}

int main() {
    try {
        double result = safe_sqrt(-1.0);
        std::cout << result << std::endl;
    } catch (const std::domain_error& e) {
        std::cerr << "Domain error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Safe Logarithm Function

```cpp
// CORRECT — validate log domain
#include <cmath>
#include <iostream>
#include <stdexcept>

double safe_log(double x) {
    if (x <= 0) {
        throw std::domain_error("log: argument must be positive (got " +
                                 std::to_string(x) + ")");
    }
    return std::log(x);
}

double safe_asin(double x) {
    if (x < -1.0 || x > 1.0) {
        throw std::domain_error("asin: argument must be in [-1, 1] (got " +
                                 std::to_string(x) + ")");
    }
    return std::asin(x);
}

int main() {
    try {
        std::cout << "log(0): " << safe_log(0) << std::endl;
    } catch (const std::domain_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    try {
        std::cout << "asin(2): " << safe_asin(2.0) << std::endl;
    } catch (const std::domain_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Validate input before math functions | When inputs come from user or external data |
| Throw `std::domain_error` | For mathematical domain violations |
| Use `std::complex` for complex results | When negative square roots are valid |
| Clamp input to valid range | When domain errors are acceptable with clamping |

## Related Errors

- [std::invalid_argument]({{< relref "/languages/cpp/invalid-argument" >}}) — invalid function arguments.
- [std::out_of_range]({{< relref "/languages/cpp/stdout-of-range" >}}) — value outside valid range.
- [std::logic_error]({{< relref "/languages/cpp/logic-error" >}}) — general logic errors.

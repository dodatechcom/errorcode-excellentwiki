---
title: "[Solution] C++ std::domain_error — Mathematical Domain Error Fix"
description: "Fix C++ std::domain_error when calling functions with mathematically invalid arguments. Handle domain errors in mathematical computations."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# [Solution] C++ std::domain_error — Mathematical Domain Error Fix

A `std::domain_error` is thrown when a function receives an argument that is outside its mathematical domain — meaning the operation is not defined for that input. Common examples include taking the square root of a negative number, computing the logarithm of a non-positive number, or using inverse trigonometric functions outside their valid range.

## Why std::domain_error Occurs

Common causes include computing `sqrt()` of a negative number, computing `log()` or `log10()` of zero or negative values, using `asin()` or `acos()` with values outside [-1, 1], and performing mathematical operations where the result would be undefined.

## Wrong: Computing sqrt of Negative Number

```cpp
// WRONG — sqrt of negative number is undefined
#include <cmath>
#include <iostream>

int main() {
    double result = std::sqrt(-1.0);  // NaN in IEEE 754, or domain error
    std::cout << result << std::endl;
    return 0;
}
```

## Correct: Validate Domain Before Mathematical Operations

```cpp
// CORRECT — check domain before computing
#include <cmath>
#include <iostream>
#include <stdexcept>

double safe_sqrt(double x) {
    if (x < 0.0) {
        throw std::domain_error("sqrt: negative argument not in domain");
    }
    return std::sqrt(x);
}

int main() {
    try {
        double result = safe_sqrt(-1.0);
        std::cout << result << std::endl;
    } catch (const std::domain_error& e) {
        std::cerr << "Domain error: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

## Safe Logarithm Function

```cpp
// CORRECT — validate log domain (x > 0)
#include <cmath>
#include <iostream>
#include <stdexcept>

double safe_log(double x) {
    if (x <= 0.0) {
        throw std::domain_error("log: argument must be positive");
    }
    return std::log(x);
}

double safe_log10(double x) {
    if (x <= 0.0) {
        throw std::domain_error("log10: argument must be positive");
    }
    return std::log10(x);
}

int main() {
    try {
        std::cout << "log(1) = " << safe_log(1.0) << std::endl;
        std::cout << "log(-1) = " << safe_log(-1.0) << std::endl;
    } catch (const std::domain_error& e) {
        std::cerr << "Domain error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Inverse Trigonometric Function Validation

```cpp
// CORRECT — validate domain for asin/acos ([-1, 1])
#include <cmath>
#include <iostream>
#include <stdexcept>

double safe_asin(double x) {
    if (x < -1.0 || x > 1.0) {
        throw std::domain_error("asin: argument must be in [-1, 1]");
    }
    return std::asin(x);
}

double safe_acos(double x) {
    if (x < -1.0 || x > 1.0) {
        throw std::domain_error("acos: argument must be in [-1, 1]");
    }
    return std::acos(x);
}

int main() {
    try {
        std::cout << "asin(0.5) = " << safe_asin(0.5) << std::endl;
        std::cout << "asin(2.0) = " << safe_asin(2.0) << std::endl;
    } catch (const std::domain_error& e) {
        std::cerr << "Domain error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Mathematical Domain Reference

| Function | Valid Domain | Invalid Input |
|---|---|---|
| `sqrt(x)` | x ≥ 0 | x < 0 |
| `log(x)` | x > 0 | x ≤ 0 |
| `log10(x)` | x > 0 | x ≤ 0 |
| `asin(x)` | -1 ≤ x ≤ 1 | x < -1 or x > 1 |
| `acos(x)` | -1 ≤ x ≤ 1 | x < -1 or x > 1 |
| `pow(x, y)` | x > 0 or (x = 0, y > 0) | x = 0, y ≤ 0 |

## Summary

| Fix | When to Use |
|---|---|
| Validate arguments before math functions | Always when inputs come from users |
| Use safe wrapper functions | When multiple calls need validation |
| Return NaN or fallback for invalid domains | When exceptions are too expensive |
| Document mathematical constraints | For public math libraries |

## Related Errors

- [std::logic_error]({{< relref "/languages/cpp/logic-error" >}}) — logical precondition violations.
- [std::invalid_argument]({{< relref "/languages/cpp/invalid-argument" >}}) — invalid function arguments.
- [std::overflow_error]({{< relref "/languages/cpp/overflowerror" >}}) — arithmetic overflow.

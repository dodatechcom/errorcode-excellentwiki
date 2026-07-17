---
title: "[Solution] C++ std::underflow_error — Arithmetic Underflow Fix"
description: "Fix C++ std::underflow_error when arithmetic operations produce results too close to zero. Handle floating-point and integer underflow."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::underflow_error — Arithmetic Underflow Fix

A `std::underflow_error` is thrown when an arithmetic computation produces a result that is too close to zero to be represented accurately (floating-point underflow), or when a subtraction produces a result below the minimum representable value. It inherits from `std::runtime_error`.

## Why std::underflow_error Occurs

Common causes include dividing very small floating-point numbers that underflow to zero, integer subtraction that wraps below minimum values, exponentiation with very small bases and large exponents, and chained multiplications of small values.

## Wrong: Unchecked Arithmetic Underflow

```cpp
// WRONG — underflow produces denormalized or zero result
#include <iostream>
#include <limits>

int main() {
    double tiny = std::numeric_limits<double>::min();
    double result = tiny / 1e300;  // underflow to zero (or denormalized)
    std::cout << "Result: " << result << std::endl;
    return 0;
}
```

## Correct: Check for Underflow Before Computation

```cpp
// CORRECT — check before division
#include <iostream>
#include <limits>
#include <cmath>
#include <stdexcept>

double safe_divide(double a, double b) {
    if (std::abs(b) < std::numeric_limits<double>::min()) {
        throw std::underflow_error("Divisor too small — would underflow");
    }
    double result = a / b;
    if (result != 0.0 && std::abs(result) < std::numeric_limits<double>::min()) {
        throw std::underflow_error("Result underflowed to denormalized value");
    }
    return result;
}

int main() {
    try {
        double result = safe_divide(1.0, 1e-310);
        std::cout << "Result: " << result << std::endl;
    } catch (const std::underflow_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Safe Integer Subtraction

```cpp
// CORRECT — check integer subtraction for underflow
#include <iostream>
#include <limits>
#include <stdexcept>

int safe_subtract(int a, int b) {
    if (b > 0 && a < std::numeric_limits<int>::min() + b) {
        throw std::underflow_error("Integer underflow in subtraction");
    }
    if (b < 0 && a > std::numeric_limits<int>::max() + b) {
        throw std::underflow_error("Integer overflow in subtraction");
    }
    return a - b;
}

int main() {
    try {
        int result = safe_subtract(std::numeric_limits<int>::min(), 1);
        std::cout << result << std::endl;
    } catch (const std::underflow_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Check divisor magnitude before division | When dividing floating-point values |
| Use `std::numeric_limits::min()` | For minimum positive normalized value |
| Check intermediate results | When chaining arithmetic operations |
| Use arbitrary-precision libraries | When precision is critical |

## Related Errors

- [std::overflow_error]({{< relref "/languages/cpp/overflowerror" >}}) — arithmetic overflow.
- [std::range_error]({{< relref "/languages/cpp/rangeerror" >}}) — result out of range.
- [std::domain_error]({{< relref "/languages/cpp/domainerror" >}}) — mathematical domain errors.

---
title: "[Solution] C++ std::overflow_error — Arithmetic Overflow Error Example"
description: "Example of std::overflow_error in C++. Handle integer and floating-point overflow safely with bounds checking."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 50
---

# [Solution] C++ std::overflow_error — Arithmetic Overflow Error Example

A `std::overflow_error` is thrown when an arithmetic operation produces a result that exceeds the maximum representable value for the given type. This applies to both integers (where overflow is undefined behavior for signed types) and floating-point (where it produces infinity).

## Common Causes

- Adding or multiplying large integers near `INT_MAX`
- Computing factorials of large numbers
- Accumulating values without checking bounds
- Multiplying floating-point values that produce infinity

## Example: Throwing std::overflow_error

```cpp
#include <iostream>
#include <stdexcept>
#include <limits>

int safe_add(int a, int b) {
    if (b > 0 && a > std::numeric_limits<int>::max() - b) {
        throw std::overflow_error("Integer addition overflow");
    }
    if (b < 0 && a < std::numeric_limits<int>::min() - b) {
        throw std::overflow_error("Integer subtraction overflow");
    }
    return a + b;
}

int main() {
    try {
        int result = safe_add(std::numeric_limits<int>::max(), 1);
        std::cout << result << std::endl;
    } catch (const std::overflow_error& e) {
        std::cerr << "Overflow error: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

## How to Fix: Safe Multiplication

```cpp
#include <iostream>
#include <stdexcept>
#include <limits>

int safe_multiply(int a, int b) {
    if (a == 0 || b == 0) return 0;

    if (a > 0) {
        if (b > 0 && a > std::numeric_limits<int>::max() / b) {
            throw std::overflow_error("Multiplication overflow");
        }
    } else {
        if (b > 0 && a < std::numeric_limits<int>::min() / b) {
            throw std::overflow_error("Multiplication underflow");
        }
    }
    return a * b;
}

int main() {
    try {
        int result = safe_multiply(std::numeric_limits<int>::max() / 2, 3);
        std::cout << result << std::endl;
    } catch (const std::overflow_error& e) {
        std::cerr << "Overflow: " << e.what() << std::endl;
    }
    return 0;
}
```

## Safe Factorial Function

```cpp
#include <iostream>
#include <stdexcept>
#include <cstdint>

uint64_t safe_factorial(int n) {
    if (n < 0) {
        throw std::overflow_error("Factorial of negative number");
    }

    uint64_t result = 1;
    for (int i = 2; i <= n; i++) {
        if (result > UINT64_MAX / i) {
            throw std::overflow_error("Factorial overflow");
        }
        result *= i;
    }
    return result;
}

int main() {
    try {
        std::cout << "10! = " << safe_factorial(10) << std::endl;
        std::cout << "21! = " << safe_factorial(21) << std::endl;  // May overflow
    } catch (const std::overflow_error& e) {
        std::cerr << "Overflow: " << e.what() << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Check bounds before arithmetic | Always with user-provided values |
| Use `__builtin_add_overflow` | When targeting GCC/Clang |
| Use wider types for accumulation | When overflow is likely |
| Validate ranges in loops | When accumulating values iteratively |

## Related Errors

- [std::underflow_error]({{< relref "/languages/cpp/underflowerror" >}}) — arithmetic underflow.
- [std::range_error]({{< relref "/languages/cpp/rangeerror" >}}) — range errors in computations.
- [std::domain_error]({{< relref "/languages/cpp/domainerror" >}}) — mathematically undefined operations.

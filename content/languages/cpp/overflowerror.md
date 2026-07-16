---
title: "[Solution] C++ std::overflow_error — Arithmetic Overflow Fix"
description: "Fix C++ std::overflow_error when arithmetic results exceed maximum representable values. Handle integer and floating-point overflow safely."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["overflow-error", "arithmetic", "integer", "bounds"]
weight: 50
---

# [Solution] C++ std::overflow_error — Arithmetic Overflow Fix

A `std::overflow_error` is thrown when an arithmetic operation produces a result that exceeds the maximum representable value for the given type. This applies to both integers (where overflow is undefined behavior for signed types) and floating-point (where it produces infinity). Unlike unsigned integer overflow (which wraps around), signed integer overflow is undefined behavior in C++.

## Why std::overflow_error Occurs

Common causes include adding or multiplying large integers, computing factorials of large numbers, accumulating values without checking bounds, and multiplying floating-point values that produce infinity.

## Wrong: Integer Overflow Without Checks

```cpp
// WRONG — signed integer overflow is undefined behavior
#include <iostream>
#include <climits>

int main() {
    int a = INT_MAX;
    int b = a + 1;  // Undefined behavior!
    std::cout << b << std::endl;
    return 0;
}
```

## Correct: Detect and Prevent Integer Overflow

```cpp
// CORRECT — check for overflow before operations
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
        int result = safe_add(INT_MAX, 1);
        std::cout << result << std::endl;
    } catch (const std::overflow_error& e) {
        std::cerr << "Overflow error: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

## Safe Multiplication

```cpp
// CORRECT — safe multiplication with overflow detection
#include <iostream>
#include <stdexcept>
#include <limits>

int safe_multiply(int a, int b) {
    if (a == 0 || b == 0) return 0;

    if (a > 0) {
        if (b > 0) {
            if (a > std::numeric_limits<int>::max() / b) {
                throw std::overflow_error("Multiplication overflow");
            }
        } else {
            if (b < std::numeric_limits<int>::min() / a) {
                throw std::overflow_error("Multiplication underflow");
            }
        }
    } else {
        if (b > 0) {
            if (a < std::numeric_limits<int>::min() / b) {
                throw std::overflow_error("Multiplication underflow");
            }
        } else {
            if (a < std::numeric_limits<int>::max() / b) {
                throw std::overflow_error("Multiplication overflow");
            }
        }
    }
    return a * b;
}

int main() {
    try {
        int result = safe_multiply(INT_MAX / 2, 3);
        std::cout << result << std::endl;
    } catch (const std::overflow_error& e) {
        std::cerr << "Overflow: " << e.what() << std::endl;
    }
    return 0;
}
```

## Safe Factorial Function

```cpp
// CORRECT — factorial with overflow checking
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
        std::cout << "20! = " << safe_factorial(20) << std::endl;
        std::cout << "21! = " << safe_factorial(21) << std::endl;  // May overflow
    } catch (const std::overflow_error& e) {
        std::cerr << "Overflow: " << e.what() << std::endl;
    }
    return 0;
}
```

## Using Checked Arithmetic Libraries

```cpp
// CORRECT — use compiler built-ins for overflow detection
#include <iostream>
#include <stdexcept>
#include <climits>

int checked_add(int a, int b) {
    int result;
    if (__builtin_add_overflow(a, b, &result)) {
        throw std::overflow_error("Addition overflow detected by compiler");
    }
    return result;
}

int main() {
    try {
        int result = checked_add(INT_MAX, 1);
        std::cout << result << std::endl;
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

- [std::underflow_error]({{< relref "/languages/cpp/underflowerror" >}}) — arithmetic underflow (result too small).
- [std::range_error]({{< relref "/languages/cpp/rangeerror" >}}) — range errors in computations.
- [std::domain_error]({{< relref "/languages/cpp/domainerror" >}}) — mathematically undefined operations.

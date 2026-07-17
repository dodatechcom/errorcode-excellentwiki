---
title: "[Solution] C++ std::overflow_error — Arithmetic Overflow Fix"
description: "Fix C++ std::overflow_error when arithmetic operations exceed the maximum representable value. Learn safe integer arithmetic patterns."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::overflow_error — Arithmetic Overflow Fix

A `std::overflow_error` is thrown when an arithmetic computation produces a result that exceeds the maximum value representable by the result type. For example, adding two large integers that wrap around, or computing a factorial that exceeds `INT_MAX`. It inherits from `std::runtime_error`.

## Why std::overflow_error Occurs

Common causes include integer arithmetic that exceeds `INT_MAX` or `UINT_MAX`, multiplying large values before division (intermediate overflow), unchecked user input leading to arithmetic overflow, and recursive functions where the result grows too large.

## Wrong: Arithmetic Without Overflow Checking

```cpp
// WRONG — overflow is undefined behavior for signed integers
#include <iostream>
#include <limits>

int main() {
    int a = std::numeric_limits<int>::max();
    int b = 1;
    int result = a + b;  // undefined behavior
    std::cout << result << std::endl;
    return 0;
}
```

## Correct: Check for Overflow Before Computation

```cpp
// CORRECT — check before adding
#include <iostream>
#include <limits>
#include <stdexcept>

int safe_add(int a, int b) {
    if (b > 0 && a > std::numeric_limits<int>::max() - b) {
        throw std::overflow_error("Integer overflow in addition");
    }
    if (b < 0 && a < std::numeric_limits<int>::min() - b) {
        throw std::overflow_error("Integer underflow in addition");
    }
    return a + b;
}

int main() {
    try {
        int result = safe_add(std::numeric_limits<int>::max(), 1);
        std::cout << result << std::endl;
    } catch (const std::overflow_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Use Safe Multiplication

```cpp
// CORRECT — safe multiply with overflow check
#include <iostream>
#include <limits>
#include <stdexcept>

long long safe_multiply(int a, int b) {
    long long result = static_cast<long long>(a) * b;
    if (result > std::numeric_limits<int>::max() || result < std::numeric_limits<int>::min()) {
        throw std::overflow_error("Multiplication result exceeds int range");
    }
    return result;
}

int main() {
    try {
        long long result = safe_multiply(100000, 100000);
        std::cout << "Result: " << result << std::endl;

        safe_multiply(std::numeric_limits<int>::max(), 2);  // throws
    } catch (const std::overflow_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Use std::numeric_limits for Safe Comparisons

```cpp
// CORRECT — use numeric_limits for overflow-safe checks
#include <iostream>
#include <limits>
#include <stdexcept>

int factorial_safe(int n) {
    if (n < 0) throw std::invalid_argument("Negative input");
    if (n > 12) throw std::overflow_error("Factorial too large for int");

    int result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

int main() {
    try {
        std::cout << "5! = " << factorial_safe(5) << std::endl;
        std::cout << "20! = " << factorial_safe(20) << std::endl;
    } catch (const std::overflow_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Check before arithmetic operations | When inputs are unbounded |
| Use larger types for intermediate results | When computing products or sums |
| Use `std::numeric_limits` checks | For portable overflow detection |
| Use safe math libraries | For production-critical arithmetic |

## Related Errors

- [std::underflow_error]({{< relref "/languages/cpp/underflowerror" >}}) — arithmetic underflow.
- [std::range_error]({{< relref "/languages/cpp/rangeerror" >}}) — result out of range.
- [std::bad_array_new_length]({{< relref "/languages/cpp/bad-allocation" >}}) — array size overflow.

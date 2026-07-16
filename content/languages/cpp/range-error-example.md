---
title: "[Solution] C++ std::range_error — Range Error in Computation Example"
description: "Example of std::range_error in C++. Handle results that fall outside valid representable ranges."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["range-error", "numeric", "computation", "exception"]
weight: 50
---

# [Solution] C++ std::range_error — Range Error in Computation Example

A `std::range_error` is thrown when a result of a computation cannot be represented because it falls outside the range of representable values. Unlike `std::overflow_error` (too large) or `std::underflow_error` (too small), `std::range_error` typically indicates an internal range violation in a library function where the result is not mathematically representable.

## Common Causes

- Mathematical functions returning results outside representable bounds
- Internal state errors in numeric libraries
- Combining operations that produce values outside valid ranges
- Rounding or conversion errors in fixed-precision arithmetic

## Example: Throwing std::range_error

```cpp
#include <cmath>
#include <iostream>
#include <stdexcept>
#include <limits>

double safe_pow(double base, double exp) {
    if (base == 0.0 && exp <= 0.0) {
        throw std::range_error("pow: undefined for 0^non-positive");
    }
    double result = std::pow(base, exp);
    if (!std::isfinite(result)) {
        throw std::range_error("pow: result out of representable range");
    }
    return result;
}

int main() {
    try {
        double result = safe_pow(10.0, 400);
        std::cout << result << std::endl;
    } catch (const std::range_error& e) {
        std::cerr << "Range error: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

## How to Fix: Safe Integer Conversion

```cpp
#include <iostream>
#include <stdexcept>
#include <limits>

template <typename Target, typename Source>
Target safe_narrow(Source value) {
    if (value < std::numeric_limits<Target>::min() ||
        value > std::numeric_limits<Target>::max()) {
        throw std::range_error("Value out of target range");
    }
    return static_cast<Target>(value);
}

int main() {
    try {
        long long big = 1000000;
        int small = safe_narrow<int>(big);
        std::cout << "Converted: " << small << std::endl;

        long long too_big = std::numeric_limits<long long>::max();
        int bad = safe_narrow<int>(too_big);  // throws
    } catch (const std::range_error& e) {
        std::cerr << "Range error: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

## Numeric Computation with Range Checks

```cpp
#include <iostream>
#include <stdexcept>
#include <cmath>

class NumericalComputation {
public:
    static double circle_area(double radius) {
        if (radius < 0.0) {
            throw std::range_error("Radius cannot be negative");
        }
        double area = M_PI * radius * radius;
        if (!std::isfinite(area)) {
            throw std::range_error("Circle area out of range");
        }
        return area;
    }

    static double compound_interest(double principal, double rate, int periods) {
        if (principal < 0.0 || rate < -1.0) {
            throw std::range_error("Invalid input parameters");
        }
        double factor = std::pow(1.0 + rate, periods);
        if (!std::isfinite(factor)) {
            throw std::range_error("Compound interest out of range");
        }
        return principal * factor;
    }
};

int main() {
    try {
        std::cout << "Area: " << NumericalComputation::circle_area(10.0) << std::endl;
        std::cout << "Interest: " << NumericalComputation::compound_interest(1000.0, 0.05, 10) << std::endl;
    } catch (const std::range_error& e) {
        std::cerr << "Range error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Check `std::isfinite()` on results | Always after floating-point computations |
| Validate input ranges | When arguments come from external sources |
| Use `std::numeric_limits` for bounds | When checking representable ranges |
| Use safe conversion functions | When narrowing between numeric types |

## Related Errors

- [std::overflow_error]({{< relref "/languages/cpp/overflowerror" >}}) — arithmetic overflow (result too large).
- [std::underflow_error]({{< relref "/languages/cpp/underflowerror" >}}) — arithmetic underflow (result too small).
- [std::domain_error]({{< relref "/languages/cpp/domainerror" >}}) — mathematically undefined operations.

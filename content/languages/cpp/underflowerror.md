---
title: "[Solution] C++ std::underflow_error — Arithmetic Underflow Fix"
description: "Fix C++ std::underflow_error when arithmetic results are too small to represent. Handle floating-point underflow and loss of precision."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# [Solution] C++ std::underflow_error — Arithmetic Underflow Fix

A `std::underflow_error` is thrown when an arithmetic operation produces a result that is too small in magnitude to be represented as a finite floating-point number (denormalized or zero). This typically happens with extremely small floating-point calculations where the result underflows the minimum representable positive value.

## Why std::underflow_error Occurs

Common causes include multiplying very small floating-point numbers together, computing extremely small exponential values, dividing by very large numbers repeatedly, and accumulating rounding errors in floating-point arithmetic.

## Wrong: Not Handling Underflow

```cpp
// WRONG — underflow produces denormalized values or zero
#include <iostream>
#include <cmath>
#include <limits>

int main() {
    double tiny = std::numeric_limits<double>::min();
    double result = tiny * tiny;  // Underflow to denormalized or zero
    std::cout << "Result: " << result << std::endl;
    std::cout << "Is denormalized: " << (result != 0 && result < std::numeric_limits<double>::min()) << std::endl;
    return 0;
}
```

## Correct: Detect and Handle Underflow

```cpp
// CORRECT — check for underflow conditions
#include <iostream>
#include <cmath>
#include <limits>

double safe_multiply(double a, double b) {
    double result = a * b;

    // Check for underflow (result is denormalized)
    if (result != 0.0 && std::abs(result) < std::numeric_limits<double>::min()) {
        throw std::underflow_error("Multiplication underflow detected");
    }

    return result;
}

int main() {
    try {
        double tiny = std::numeric_limits<double>::min();
        double result = safe_multiply(tiny, tiny);
        std::cout << "Result: " << result << std::endl;
    } catch (const std::underflow_error& e) {
        std::cerr << "Underflow error: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

## Safe Exponential Computation

```cpp
// CORRECT — handle underflow in exponential calculations
#include <iostream>
#include <cmath>
#include <limits>

double safe_exp(double x) {
    if (x < std::log(std::numeric_limits<double>::min())) {
        throw std::underflow_error("exp(): result would underflow");
    }
    return std::exp(x);
}

int main() {
    try {
        std::cout << "exp(0) = " << safe_exp(0.0) << std::endl;
        std::cout << "exp(-1000) = " << safe_exp(-1000.0) << std::endl;
    } catch (const std::underflow_error& e) {
        std::cerr << "Underflow: " << e.what() << std::endl;
    }
    return 0;
}
```

## Using Log-Space for Small Values

```cpp
// CORRECT — work in log-space to avoid underflow
#include <iostream>
#include <cmath>

class LogValue {
    double log_value_;
    bool is_zero_;
public:
    LogValue(double value) : is_zero_(value == 0.0) {
        log_value_ = is_zero_ ? 0.0 : std::log(std::abs(value));
    }

    static LogValue from_log(double log_val) {
        LogValue lv(0.0);
        lv.log_value_ = log_val;
        lv.is_zero_ = false;
        return lv;
    }

    double value() const {
        if (is_zero_) return 0.0;
        // May still underflow when converting back
        if (log_value_ < std::log(std::numeric_limits<double>::min())) {
            return 0.0;  // Underflow to zero
        }
        return std::exp(log_value_);
    }

    LogValue multiply(const LogValue& other) const {
        if (is_zero_ || other.is_zero_) return LogValue(0.0);
        return from_log(log_value_ + other.log_value_);
    }
};

int main() {
    LogValue a(std::numeric_limits<double>::min());
    LogValue b(std::numeric_limits<double>::min());

    LogValue result = a.multiply(b);
    std::cout << "Result: " << result.value() << std::endl;
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Check for denormalized results | When precision is critical |
| Use log-space arithmetic | When dealing with very small or large numbers |
| Validate ranges before operations | When inputs come from users |
| Use `std::fpclassify()` | To detect subnormal values |

## Related Errors

- [std::overflow_error]({{< relref "/languages/cpp/overflowerror" >}}) — arithmetic overflow.
- [std::range_error]({{< relref "/languages/cpp/rangeerror" >}}) — range errors in computations.
- [std::domain_error]({{< relref "/languages/cpp/domainerror" >}}) — mathematical domain errors.

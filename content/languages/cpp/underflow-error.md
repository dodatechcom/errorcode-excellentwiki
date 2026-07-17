---
title: "[Solution] C++ std::underflow_error - arithmetic underflow"
description: "Fix C++ std::underflow_error from arithmetic underflow. Prevent loss of precision in calculations."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["underflow-error", "arithmetic", "underflow", "numeric", "stdexcept"]
weight: 5
---

# std::underflow_error - arithmetic underflow

`std::underflow_error` is thrown when a mathematical operation produces a value too close to zero to be represented. This is less common than overflow.

## Common Causes

```cpp
// Cause 1: Very small floating-point result
double result = std::numeric_limits<double>::min() / 2.0;

// Cause 2: Subnormal calculations
double a = 1e-300;
double b = 1e-300;
double product = a * b; // may underflow to zero

// Cause 3: Custom function throwing
double safe_sqrt(double x) {
    if (x < 0) throw std::underflow_error("negative");
    return std::sqrt(x);
}
```

## How to Fix

### Fix 1: Check before operation

```cpp
if (std::abs(x) < std::numeric_limits<double>::min()) {
    throw std::underflow_error("value too small");
}
```

### Fix 2: Use appropriate types

```cpp
long double result = static_cast<long double>(a) * b;
```

### Fix 3: Catch and handle

```cpp
try {
    double result = calculate(a, b);
} catch (const std::underflow_error& e) {
    std::cerr << "Underflow: " << e.what() << std::endl;
}
```

## Related Errors

- [std::overflow_error]({{< relref "/languages/cpp/overflow-error-arithmetic" >}}) — arithmetic overflow.
- [std::domain_error]({{< relref "/languages/cpp/domain-error-vector" >}}) — math domain error.
- [std::range_error]({{< relref "/languages/cpp/range-error-base" >}}) — range error.

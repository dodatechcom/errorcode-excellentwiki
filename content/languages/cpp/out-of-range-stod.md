---
title: "[Solution] C++ std::out_of_range - stod out of range"
description: "Fix C++ std::out_of_range when stod receives value outside double range."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["out-of-range", "stod", "conversion", "double", "floating-point"]
weight: 5
---

# std::out_of_range - stod out of range

`std::out_of_range` is thrown when `std::stod` converts a string whose numeric value exceeds the range of `double` (overflow to infinity).

## Common Causes

```cpp
// Cause 1: Extremely large value
double val = std::stod("1e999"); // out_of_range (overflow to inf)

// Cause 2: Extremely small value
double val = std::stod("1e-999"); // out_of_range (underflow to 0)
```

## How to Fix

### Fix 1: Use try-catch

```cpp
try {
    double val = std::stod(input);
} catch (const std::out_of_range& e) {
    std::cerr << "Value out of double range" << std::endl;
}
```

### Fix 2: Validate exponent

```cpp
// Check if exponent is reasonable
if (input.find("e") != std::string::npos) {
    auto exp_pos = input.find("e") + 1;
    int exp = std::stoi(input.substr(exp_pos));
    if (std::abs(exp) > 308) {
        std::cerr << "Exponent too large" << std::endl;
    }
}
```

### Fix 3: Use long double

```cpp
long double val = std::stold(input); // wider range
```

## Related Errors

- [std::invalid_argument - stod]({{< relref "/languages/cpp/invalid-argument-stod" >}}) — non-numeric.
- [std::out_of_range - stoul]({{< relref "/languages/cpp/out-of-range-stoul" >}}) — stoul out of range.
- [std::overflow_error - stoi]({{< relref "/languages/cpp/overflow-error-stoi" >}}) — stoi overflow.

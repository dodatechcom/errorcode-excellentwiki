---
title: "[Solution] C++ std::invalid_argument - stold conversion error"
description: "Fix C++ std::invalid_argument when stold receives non-numeric string."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["invalid-argument", "stold", "conversion", "long-double", "numeric"]
weight: 5
---

# std::invalid_argument - stold conversion error

`std::invalid_argument` is thrown when `std::stold` receives a string that cannot be converted to a `long double`.

## Common Causes

```cpp
// Cause 1: Non-numeric string
long double val = std::stold("hello"); // throws

// Cause 2: Empty string
long double val = std::stold(""); // throws
```

## How to Fix

### Fix 1: Use try-catch

```cpp
try {
    long double val = std::stold(input);
} catch (const std::invalid_argument& e) {
    std::cerr << "Not a valid number" << std::endl;
}
```

### Fix 2: Validate input

```cpp
if (!input.empty()) {
    try {
        long double val = std::stold(input);
    } catch (...) {
        std::cerr << "Conversion failed" << std::endl;
    }
}
```

### Fix 3: Use strtold

```cpp
char* end;
long double val = std::strtold(input.c_str(), &end);
if (end == input.c_str()) {
    std::cerr << "Invalid conversion" << std::endl;
}
```

## Related Errors

- [std::invalid_argument - stod]({{< relref "/languages/cpp/invalid-argument-stod" >}}) — stod error.
- [std::invalid_argument - stof]({{< relref "/languages/cpp/invalid-argument-stof" >}}) — stof error.
- [std::invalid_argument - stoi]({{< relref "/languages/cpp/invalid-argument-stoi" >}}) — stoi error.

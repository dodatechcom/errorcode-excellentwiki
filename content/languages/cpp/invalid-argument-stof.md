---
title: "[Solution] C++ std::invalid_argument - stof conversion error"
description: "Fix C++ std::invalid_argument when stof receives non-numeric string."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["invalid-argument", "stof", "conversion", "float", "numeric"]
weight: 5
---

# std::invalid_argument - stof conversion error

`std::invalid_argument` is thrown when `std::stof` receives a string that cannot be converted to a float.

## Common Causes

```cpp
// Cause 1: Non-numeric string
float val = std::stof("hello"); // throws

// Cause 2: Empty string
float val = std::stof(""); // throws

// Cause 3: Only whitespace
float val = std::stof("   "); // throws
```

## How to Fix

### Fix 1: Use try-catch

```cpp
try {
    float val = std::stof(input);
} catch (const std::invalid_argument& e) {
    std::cerr << "Not a valid float" << std::endl;
}
```

### Fix 2: Validate input

```cpp
if (!input.empty() && (std::isdigit(input[0]) || input[0] == '-' || input[0] == '+')) {
    float val = std::stof(input);
}
```

### Fix 3: Use strtod

```cpp
char* end;
float val = std::strtof(input.c_str(), &end);
if (end == input.c_str()) {
    std::cerr << "Conversion failed" << std::endl;
}
```

## Related Errors

- [std::invalid_argument - stod]({{< relref "/languages/cpp/invalid-argument-stod" >}}) — stod error.
- [std::invalid_argument - stold]({{< relref "/languages/cpp/invalid-argument-stold" >}}) — stold error.
- [std::overflow_error - stoul]({{< relref "/languages/cpp/overflow-error-stoul" >}}) — overflow error.

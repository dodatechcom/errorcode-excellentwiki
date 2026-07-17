---
title: "[Solution] C++ std::invalid_argument - stod conversion error"
description: "Fix C++ std::invalid_argument when stod receives non-numeric string."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["invalid-argument", "stod", "conversion", "double", "numeric"]
weight: 5
---

# std::invalid_argument - stod conversion error

`std::invalid_argument` is thrown when `std::stod` receives a string that cannot be converted to a double.

## Common Causes

```cpp
// Cause 1: Non-numeric string
double val = std::stod("hello"); // throws

// Cause 2: Empty string
double val = std::stod(""); // throws

// Cause 3: Special characters
double val = std::stod("12.34abc"); // may throw or return 12.34
```

## How to Fix

### Fix 1: Validate before conversion

```cpp
bool is_numeric(const std::string& s) {
    if (s.empty()) return false;
    char* end;
    std::strtod(s.c_str(), &end);
    return end != s.c_str();
}
```

### Fix 2: Use try-catch

```cpp
try {
    double val = std::stod(input);
} catch (const std::invalid_argument& e) {
    std::cerr << "Not a valid number" << std::endl;
}
```

### Fix 3: Use from_chars

```cpp
#include <charconv>
double val;
auto [ptr, ec] = std::from_chars(input.data(), input.data() + input.size(), val);
if (ec == std::errc::invalid_argument) {
    std::cerr << "Invalid number" << std::endl;
}
```

## Related Errors

- [std::invalid_argument - stof]({{< relref "/languages/cpp/invalid-argument-stof" >}}) — stof error.
- [std::invalid_argument - stold]({{< relref "/languages/cpp/invalid-argument-stold" >}}) — stold error.
- [std::invalid_argument - stoi]({{< relref "/languages/cpp/invalid-argument-stoi" >}}) — stoi error.

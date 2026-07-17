---
title: "[Solution] C++ std::invalid_argument - stoi conversion error"
description: "Fix C++ std::invalid_argument when stoi receives a non-numeric string."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::invalid_argument - stoi conversion error

`std::invalid_argument` is thrown when `std::stoi` receives a string that does not contain a valid numeric representation.

## Common Causes

```cpp
// Cause 1: Non-numeric string
int val = std::stoi("hello"); // throws std::invalid_argument

// Cause 2: String with spaces
int val = std::stoi(" 123"); // throws (leading space not allowed)

// Cause 3: Empty string
int val = std::stoi(""); // throws
```

## How to Fix

### Fix 1: Validate before conversion

```cpp
#include <string>
#include <cctype>

bool is_numeric(const std::string& s) {
    if (s.empty()) return false;
    for (char c : s) {
        if (!std::isdigit(c) && c != '-' && c != '+') return false;
    }
    return true;
}

if (is_numeric(input)) {
    int val = std::stoi(input);
}
```

### Fix 2: Use try-catch

```cpp
try {
    int val = std::stoi(input);
} catch (const std::invalid_argument& e) {
    std::cerr << "Not a valid number" << std::endl;
}
```

### Fix 3: Use std::from_chars (C++17)

```cpp
#include <charconv>

int val;
auto [ptr, ec] = std::from_chars(input.data(), input.data() + input.size(), val);
if (ec == std::errc::invalid_argument) {
    std::cerr << "Invalid number" << std::endl;
}
```

## Related Errors

- [std::out_of_range - stoul]({{< relref "/languages/cpp/out-of-range-stoul" >}}) — value too large.
- [std::overflow_error - stoi]({{< relref "/languages/cpp/overflow-error-stoi" >}}) — integer overflow.
- [std::invalid_argument - stod]({{< relref "/languages/cpp/invalid-argument-stod" >}}) — double conversion.

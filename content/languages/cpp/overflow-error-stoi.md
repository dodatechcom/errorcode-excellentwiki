---
title: "[Solution] C++ std::overflow_error - stoi overflow"
description: "Fix C++ std::overflow_error from stoi when value exceeds int range."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["overflow-error", "stoi", "conversion", "integer", "range"]
weight: 5
---

# std::overflow_error - stoi overflow

`std::overflow_error` is thrown when `std::stoi` converts a string whose numeric value exceeds the range of `int`.

## Common Causes

```cpp
// Cause 1: Number too large
int val = std::stoi("99999999999999"); // overflow

// Cause 2: Negative overflow
int val = std::stoi("-99999999999999"); // overflow

// Cause 3: Hex overflow
int val = std::stoi("0xFFFFFFFF", nullptr, 16); // overflow on 32-bit
```

## How to Fix

### Fix 1: Use long long

```cpp
long long val = std::stoll("99999999999999");
```

### Fix 2: Check range before conversion

```cpp
#include <climits>
if (input.length() < 10) { // rough check
    int val = std::stoi(input);
}
```

### Fix 3: Use try-catch

```cpp
try {
    int val = std::stoi(input);
} catch (const std::overflow_error& e) {
    std::cerr << "Value too large for int" << std::endl;
}
```

## Related Errors

- [std::out_of_range - stoul]({{< relref "/languages/cpp/out-of-range-stoul" >}}) — stoul out of range.
- [std::invalid_argument - stoi]({{< relref "/languages/cpp/invalid-argument-stoi" >}}) — non-numeric string.
- [std::overflow_error - stoul]({{< relref "/languages/cpp/overflow-error-stoul" >}}) — stoul overflow.

---
title: "[Solution] C++ std::out_of_range - stoul out of range"
description: "Fix C++ std::out_of_range when stoul receives value outside unsigned long range."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::out_of_range - stoul out of range

`std::out_of_range` is thrown when `std::stoul` converts a string whose numeric value is outside the range of `unsigned long`.

## Common Causes

```cpp
// Cause 1: Value too large
unsigned long val = std::stoul("999999999999999999999"); // out_of_range

// Cause 2: Negative value
unsigned long val = std::stoul("-1"); // out_of_range
```

## How to Fix

### Fix 1: Use wider type

```cpp
unsigned long long val = std::stoull(input);
```

### Fix 2: Validate before conversion

```cpp
try {
    unsigned long val = std::stoul(input);
} catch (const std::out_of_range& e) {
    std::cerr << "Value out of range" << std::endl;
}
```

### Fix 3: Use check range

```cpp
if (input.find('-') != std::string::npos) {
    // Negative value can't be unsigned
    std::cerr << "Invalid unsigned value" << std::endl;
}
```

## Related Errors

- [std::overflow_error - stoul]({{< relref "/languages/cpp/overflow-error-stoul" >}}) — stoul overflow.
- [std::out_of_range - stod]({{< relref "/languages/cpp/out-of-range-stod" >}}) — stod out of range.
- [std::invalid_argument - stoi]({{< relref "/languages/cpp/invalid-argument-stoi" >}}) — non-numeric.

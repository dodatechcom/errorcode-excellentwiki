---
title: "[Solution] C++ std::overflow_error - stoul overflow"
description: "Fix C++ std::overflow_error from stoul when value exceeds unsigned long range."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["overflow-error", "stoul", "conversion", "unsigned-long", "range"]
weight: 5
---

# std::overflow_error - stoul overflow

`std::overflow_error` is thrown when `std::stoul` converts a string whose numeric value exceeds the range of `unsigned long`.

## Common Causes

```cpp
// Cause 1: Too large for unsigned long
unsigned long val = std::stoul("99999999999999999999"); // overflow

// Cause 2: Negative value for unsigned
unsigned long val = std::stoul("-1"); // overflow
```

## How to Fix

### Fix 1: Use unsigned long long

```cpp
unsigned long long val = std::stoull("99999999999999999999");
```

### Fix 2: Use try-catch

```cpp
try {
    unsigned long val = std::stoul(input);
} catch (const std::overflow_error& e) {
    std::cerr << "Value too large" << std::endl;
}
```

### Fix 3: Validate range

```cpp
if (input.length() <= 20) { // rough max digits for unsigned long long
    auto val = std::stoull(input);
}
```

## Related Errors

- [std::overflow_error - stoi]({{< relref "/languages/cpp/overflow-error-stoi" >}}) — stoi overflow.
- [std::overflow_error - stoll]({{< relref "/languages/cpp/overflow-error-stoll" >}}) — stoll overflow.
- [std::out_of_range - stoul]({{< relref "/languages/cpp/out-of-range-stoul" >}}) — stoul out of range.

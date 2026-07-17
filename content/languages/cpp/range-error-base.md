---
title: "[Solution] C++ std::range_error - base error"
description: "Fix C++ std::range_error from range errors. Ensure values are within valid ranges."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["range-error", "range", "stdexcept", "runtime-error", "bounds"]
weight: 5
---

# std::range_error - base error

`std::range_error` is thrown when a result is not representable within the target range. It indicates a calculation result that cannot be represented.

## Common Causes

```cpp
// Cause 1: Wide string conversion
std::wstring ws = L"too long";
std::string s = std::wstring_convert<...>().to_bytes(ws); // range_error

// Cause 2: Numeric conversion
long val = std::stol("99999999999999999999"); // range_error

// Cause 3: Custom range check
int normalize(int x) {
    if (x < 0 || x > 100) throw std::range_error("out of range");
    return x;
}
```

## How to Fix

### Fix 1: Validate before conversion

```cpp
std::string input = "12345";
long val;
try {
    val = std::stol(input);
} catch (const std::out_of_range& e) {
    std::cerr << "Value out of range" << std::endl;
}
```

### Fix 2: Clamp values

```cpp
int clamp(int val, int min, int max) {
    return std::max(min, std::min(max, val));
}
```

### Fix 3: Use appropriate types

```cpp
long long val = std::stoll("99999999999999999999");
```

## Related Errors

- [std::overflow_error]({{< relref "/languages/cpp/overflow-error-arithmetic" >}}) — arithmetic overflow.
- [std::underflow_error]({{< relref "/languages/cpp/underflow-error" >}}) — arithmetic underflow.
- [std::out_of_range - vector.at()]({{< relref "/languages/cpp/out-of-range-vector" >}}) — vector index.

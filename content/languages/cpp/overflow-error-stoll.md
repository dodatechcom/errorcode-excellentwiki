---
title: "[Solution] C++ std::overflow_error - stoll overflow"
description: "Fix C++ std::overflow_error from stoll when value exceeds long long range."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::overflow_error - stoll overflow

`std::overflow_error` is thrown when `std::stoll` converts a string whose numeric value exceeds the range of `long long`.

## Common Causes

```cpp
// Cause 1: Exceeding long long max
long long val = std::stoll("999999999999999999999"); // overflow

// Cause 2: Hex value too large
long long val = std::stoll("FFFFFFFFFFFFFFFFFFFF", nullptr, 16);
```

## How to Fix

### Fix 1: Use __int128 or arbitrary precision

```cpp
#include <boost/multiprecision/cpp_int.hpp>
auto val = boost::multiprecision::cpp_int("999999999999999999999");
```

### Fix 2: Use try-catch

```cpp
try {
    long long val = std::stoll(input);
} catch (const std::overflow_error& e) {
    std::cerr << "Value too large for long long" << std::endl;
}
```

### Fix 3: Validate length

```cpp
if (input.length() <= 19) { // max digits for long long
    long long val = std::stoll(input);
}
```

## Related Errors

- [std::overflow_error - stoi]({{< relref "/languages/cpp/overflow-error-stoi" >}}) — stoi overflow.
- [std::overflow_error - stoul]({{< relref "/languages/cpp/overflow-error-stoul" >}}) — stoul overflow.
- [std::out_of_range - stoul]({{< relref "/languages/cpp/out-of-range-stoul" >}}) — stoul out of range.

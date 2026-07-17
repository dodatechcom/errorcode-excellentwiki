---
title: "[Solution] C++ std::overflow_error - arithmetic overflow"
description: "Fix C++ std::overflow_error from arithmetic overflow. Check bounds before arithmetic operations."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::overflow_error - arithmetic overflow

`std::overflow_error` is thrown when an arithmetic operation produces a value too large for the destination type. Some functions explicitly throw this on overflow.

## Common Causes

```cpp
// Cause 1: bitset overflow
std::bitset<8> bs;
bs.to_ulong(); // may throw if value > ULONG_MAX

// Cause 2: Arithmetic in checked functions
int result = std::numeric_limits<int>::max() + 1; // UB

// Cause 3: Numeric cast overflow
auto val = std::numeric_limits<long long>::max();
int small = static_cast<int>(val); // overflow
```

## How to Fix

### Fix 1: Check before operation

```cpp
#include <limits>

if (a > std::numeric_limits<int>::max() - b) {
    throw std::overflow_error("addition would overflow");
}
int result = a + b;
```

### Fix 2: Use safer types

```cpp
long long result = static_cast<long long>(a) + b;
```

### Fix 3: Catch and handle

```cpp
try {
    auto val = bs.to_ulong();
} catch (const std::overflow_error& e) {
    std::cerr << "Overflow: " << e.what() << std::endl;
}
```

## Related Errors

- [std::underflow_error]({{< relref "/languages/cpp/underflow-error" >}}) — arithmetic underflow.
- [std::range_error]({{< relref "/languages/cpp/range-error-base" >}}) — range error.
- [std::overflow_error - stoi]({{< relref "/languages/cpp/overflow-error-stoi" >}}) — stoi overflow.

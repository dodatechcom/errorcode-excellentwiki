---
title: "[Solution] C++ std::logic_error - domain error"
description: "Fix C++ std::logic_error domain error. Ensure function arguments are within valid domains."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::logic_error - domain error

`std::logic_error` indicates a violation of a function's precondition. The argument is outside the valid domain for the operation.

## Common Causes

```cpp
// Cause 1: Math domain error
double result = std::sqrt(-1.0); // domain error

// Cause 2: Invalid string position
std::string s = "hello";
s.erase(100); // throws std::logic_error

// Cause 3: Invalid iterator range
std::vector<int> v = {1, 2, 3};
std::vector<int> v2(v.end(), v.begin()); // invalid range
```

## How to Fix

### Fix 1: Validate domain

```cpp
double safe_sqrt(double x) {
    if (x < 0) throw std::domain_error("sqrt of negative");
    return std::sqrt(x);
}
```

### Fix 2: Check string positions

```cpp
if (pos <= s.size()) {
    s.erase(pos);
}
```

### Fix 3: Validate iterator range

```cpp
if (first <= last) {
    std::vector<int> v2(first, last);
}
```

## Related Errors

- [std::domain_error - sqrt]({{< relref "/languages/cpp/domain-error-sqrt" >}}) — sqrt of negative.
- [std::domain_error - log]({{< relref "/languages/cpp/domain-error-log" >}}) — log of zero/negative.
- [std::logic_error - length]({{< relref "/languages/cpp/logic-error-length" >}}) — length error.

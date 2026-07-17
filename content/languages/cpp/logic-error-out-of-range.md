---
title: "[Solution] C++ std::logic_error - out of range"
description: "Fix C++ std::logic_error out of range. Access elements within valid bounds."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["logic-error", "out-of-range", "bounds", "stdexcept", "access"]
weight: 5
---

# std::logic_error - out of range

`std::out_of_range` is thrown when an element access is outside the valid range of a container or sequence.

## Common Causes

```cpp
// Cause 1: String position out of range
std::string s = "hello";
s.at(100); // throws std::out_of_range

// Cause 2: Vector index out of range
std::vector<int> v = {1, 2, 3};
v.at(10); // throws

// Cause 3: Map key not found
std::map<int, int> m;
m.at(99); // throws
```

## How to Fix

### Fix 1: Check bounds first

```cpp
if (index < v.size()) {
    int val = v.at(index);
}
```

### Fix 2: Use safe access

```cpp
int get_or_default(const std::vector<int>& v, size_t idx, int def) {
    return (idx < v.size()) ? v[idx] : def;
}
```

### Fix 3: Use find for maps

```cpp
auto it = m.find(key);
if (it != m.end()) {
    int val = it->second;
}
```

## Related Errors

- [std::out_of_range - vector.at()]({{< relref "/languages/cpp/out-of-range-vector" >}}) — vector bounds.
- [std::out_of_range - map.at()]({{< relref "/languages/cpp/out-of-range-map" >}}) — map key.
- [std::out_of_range - string.at()]({{< relref "/languages/cpp/out-of-range-string" >}}) — string bounds.

---
title: "[Solution] C++ std::out_of_range - string out of bounds"
description: "Fix C++ std::out_of_range when accessing string characters out of bounds."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::out_of_range - string.at() out of bounds

`std::out_of_range` is thrown when `string::at()` is called with an index that is >= the string's length.

## Common Causes

```cpp
// Cause 1: Index beyond string length
std::string s = "hello";
char c = s.at(10); // throws std::out_of_range

// Cause 2: Empty string
std::string s;
char c = s.at(0); // throws

// Cause 3: Off-by-one in loop
std::string s = "test";
for (size_t i = 0; i <= s.length(); i++) {
    s.at(i); // throws when i == s.length()
}
```

## How to Fix

### Fix 1: Check length first

```cpp
if (index < s.length()) {
    char c = s.at(index);
}
```

### Fix 2: Use operator[] or []

```cpp
char c = s[index]; // undefined if out of bounds
```

### Fix 3: Use range-based for

```cpp
for (char c : s) {
    std::cout << c << std::endl;
}
```

## Related Errors

- [std::out_of_range - vector.at()]({{< relref "/languages/cpp/out-of-range-vector" >}}) — vector index.
- [std::out_of_range - map.at()]({{< relref "/languages/cpp/out-of-range-map" >}}) — map key.
- [std::out_of_range - deque.at()]({{< relref "/languages/cpp/out-of-range-deque" >}}) — deque index.

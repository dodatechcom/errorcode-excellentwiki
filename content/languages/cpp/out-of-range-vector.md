---
title: "[Solution] C++ std::out_of_range - vector.at() index out of range"
description: "Fix C++ std::out_of_range when vector.at() receives an out-of-bounds index."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["out-of-range", "vector", "at", "index", "bounds-check"]
weight: 5
---

# std::out_of_range - vector.at() index out of range

`std::out_of_range` is thrown when `vector::at()` is called with an index that is >= the vector's size or < 0.

## Common Causes

```cpp
// Cause 1: Index beyond size
std::vector<int> v = {1, 2, 3};
int val = v.at(5); // throws std::out_of_range

// Cause 2: Empty vector
std::vector<int> v;
int val = v.at(0); // throws — vector is empty

// Cause 3: Off-by-one error
for (size_t i = 0; i <= v.size(); i++) { // should be <
    v.at(i); // throws when i == v.size()
}
```

## How to Fix

### Fix 1: Check size before access

```cpp
if (index < v.size()) {
    int val = v.at(index);
}
```

### Fix 2: Use operator[] (no bounds check)

```cpp
int val = v[index]; // undefined if out of bounds
```

### Fix 3: Use iterators

```cpp
for (auto it = v.begin(); it != v.end(); ++it) {
    std::cout << *it << std::endl;
}
```

## Related Errors

- [std::out_of_range - map.at()]({{< relref "/languages/cpp/out-of-range-map" >}}) — map key not found.
- [std::out_of_range - string.at()]({{< relref "/languages/cpp/out-of-range-string" >}}) — string out of bounds.
- [std::out_of_range - deque.at()]({{< relref "/languages/cpp/out-of-range-deque" >}}) — deque out of range.

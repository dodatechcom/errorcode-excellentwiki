---
title: "[Solution] C++ std::out_of_range - deque.at() out of range"
description: "Fix C++ std::out_of_range when deque.at() receives an out-of-bounds index."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::out_of_range - deque.at() out of range

`std::out_of_range` is thrown when `deque::at()` is called with an index that is >= the deque's size.

## Common Causes

```cpp
// Cause 1: Index beyond size
std::deque<int> d = {1, 2, 3};
int val = d.at(5); // throws

// Cause 2: Empty deque
std::deque<int> d;
int val = d.at(0); // throws

// Cause 3: After popping elements
std::deque<int> d = {1, 2, 3};
d.pop_front();
d.pop_front();
d.pop_front();
d.at(0); // throws — deque is empty
```

## How to Fix

### Fix 1: Check size

```cpp
if (!d.empty() && index < d.size()) {
    int val = d.at(index);
}
```

### Fix 2: Use operator[]

```cpp
int val = d[index]; // undefined if out of bounds
```

### Fix 3: Use iterators

```cpp
for (auto it = d.begin(); it != d.end(); ++it) {
    std::cout << *it << std::endl;
}
```

## Related Errors

- [std::out_of_range - vector.at()]({{< relref "/languages/cpp/out-of-range-vector" >}}) — vector index.
- [std::out_of_range - map.at()]({{< relref "/languages/cpp/out-of-range-map" >}}) — map key.
- [std::out_of_range - string.at()]({{< relref "/languages/cpp/out-of-range-string" >}}) — string index.

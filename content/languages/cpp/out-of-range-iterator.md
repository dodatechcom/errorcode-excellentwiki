---
title: "[Solution] Iterator Out of Range Error Fix"
description: "Fix iterator out of range errors in C++. Handle invalid iterator access, end() dereference, and container invalidation."
languages: ["cpp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["iterator", "out_of_range", "container", "vector", "bounds"]
weight: 5
---

# Iterator Out of Range Error

Fix iterator out of range errors in C++. Handle invalid iterator access, end() dereference, and container invalidation.

## What This Error Means

Iterator out of range errors occur when dereferencing an invalid iterator:

```
/usr/include/debug/vector:389: reference out of range
terminate called after throwing an instance of 'std::out_of_range'
  what():  vector::_M_range_check
```

## Common Causes

```cpp
// Cause 1: Dereferencing end() iterator
auto it = vec.end();
*it; // Undefined behavior

// Cause 2: Iterator invalidated by push_back/insert
auto it = vec.begin();
vec.push_back(42);
*it; // Invalidated!

// Cause 3: Using iterator after erase without re-assigning
// Cause 4: Range-based for with modification
```

## How to Fix

### Fix 1: Always check before dereferencing

```cpp
#include <vector>

void process(const std::vector<int>& vec) {
    auto it = std::find(vec.begin(), vec.end(), 42);
    if (it != vec.end()) {
        std::cout << "Found: " << *it << std::endl;
    }
}
```

### Fix 2: Invalidate and re-acquire iterators after modification

```cpp
#include <vector>

void add_and_process(std::vector<int>& vec, int value) {
    vec.push_back(value); // All iterators invalidated

    // Re-acquire iterators after modification
    for (auto it = vec.begin(); it != vec.end(); ++it) {
        std::cout << *it << std::endl;
    }
}
```

### Fix 3: Use indices instead of iterators for indexed access

```cpp
#include <vector>
#include <stdexcept>

int safe_at(const std::vector<int>& vec, size_t index) {
    if (index >= vec.size()) {
        throw std::out_of_range("Index out of range");
    }
    return vec.at(index);
}
```

## Examples

```cpp
#include <vector>
#include <algorithm>
#include <iostream>

void remove_duplicates(std::vector<int>& vec) {
    std::sort(vec.begin(), vec.end());
    auto last = std::unique(vec.begin(), vec.end());
    vec.erase(last, vec.end());
}

int main() {
    std::vector<int> v = {1, 2, 3, 2, 4, 3, 5};

    remove_duplicates(v);

    for (size_t i = 0; i < v.size(); ++i) {
        std::cout << v[i] << " ";
    }
    // Output: 1 2 3 4 5
    std::cout << std::endl;
    return 0;
}
```

## Related Errors

- [Out of Range Vector]({{< relref "/languages/cpp/out-of-range-vector" >}}) — vector out of range
- [Out of Range Deque]({{< relref "/languages/cpp/out-of-range-deque" >}}) — deque out of range
- [Out of Range Iterator]({{< relref "/languages/cpp/out-of-range-iterator" >}}) — iterator out of range

---
title: "[Solution] C++ std::out_of_range — Vector/String At() Boundary Check Fix"
description: "Fix C++ std::out_of_range exceptions from vector::at(), string::at(), and other container bounds-checked access methods."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["out-of-range", "vector", "string", "at", "bounds-check", "stdexcept"]
weight: 5
---

# [Solution] C++ std::out_of_range — Vector/String At() Boundary Check Fix

A `std::out_of_range` exception is thrown when you use the `.at()` method of a standard container (e.g., `std::vector`, `std::string`, `std::map`) with an index or key that is outside the valid range. The `.at()` methods perform bounds checking, unlike `operator[]`, which has no such check.

## Common Causes

- **Index exceeds container size** — passing an index >= `.size()` to `.at()`
- **Off-by-one in iteration** — loop boundary too large by one
- **Empty container access** — calling `.at(0)` on an empty vector or string
- **Mismatched index type** — using a signed int that is negative

## How to Fix

### Fix 1: Check size before accessing

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> nums = {10, 20, 30};

    size_t index = 5;
    if (index < nums.size()) {
        std::cout << nums.at(index) << std::endl;
    } else {
        std::cerr << "Index " << index << " out of range (size: " << nums.size() << ")" << std::endl;
    }

    return 0;
}
```

### Fix 2: Use iterators and bounds-checked loops

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5};

    for (size_t i = 0; i < nums.size(); i++) {
        std::cout << nums[i] << std::endl;
    }

    // Or use range-based for
    for (const auto& n : nums) {
        std::cout << n << std::endl;
    }

    return 0;
}
```

### Fix 3: Catch and handle the exception gracefully

```cpp
#include <iostream>
#include <vector>
#include <stdexcept>

int safe_get(const std::vector<int>& v, size_t idx, int fallback) {
    try {
        return v.at(idx);
    } catch (const std::out_of_range& e) {
        std::cerr << "Access error: " << e.what() << std::endl;
        return fallback;
    }
}

int main() {
    std::vector<int> nums = {10, 20, 30};
    std::cout << safe_get(nums, 1, 0) << std::endl;   // 20
    std::cout << safe_get(nums, 10, -1) << std::endl;  // -1 (fallback)
    return 0;
}
```

## Examples

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>

int main() {
    /* Vector out of range */
    std::vector<int> v = {1, 2, 3};
    try {
        int x = v.at(10);  // throws std::out_of_range
        std::cout << x << std::endl;
    } catch (const std::out_of_range& e) {
        std::cerr << "vector: " << e.what() << std::endl;
    }

    /* String out of range */
    std::string s = "hello";
    try {
        char c = s.at(10);  // throws std::out_of_range
        std::cout << c << std::endl;
    } catch (const std::out_of_range& e) {
        std::cerr << "string: " << e.what() << std::endl;
    }

    /* Empty container */
    std::vector<int> empty;
    try {
        empty.at(0);  // throws — vector is empty
    } catch (const std::out_of_range& e) {
        std::cerr << "empty: " << e.what() << std::endl;
    }

    return 0;
}
```

## Related Errors

- [std::length_error]({{< relref "/languages/cpp/length-error" >}}) — container resize exceeds max size
- [std::invalid_argument]({{< relref "/languages/cpp/invalid-argument" >}}) — invalid function argument
- [std::out_of_range (variant)]({{< relref "/languages/cpp/out-of-range-2" >}}) — variant index out of range

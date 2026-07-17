---
title: "[Solution] C++ std::out_of_range — Vector/String Index Fix"
description: "Fix C++ std::out_of_range exception when accessing vectors and strings. Learn to use .at() for bounds checking and safe element access every time now."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 40
---

# [Solution] C++ std::out_of_range — Vector/String Index Fix

A `std::out_of_range` exception is thrown when you access a `std::vector` or `std::string` using `.at()` with an index that is beyond the container's valid range. Unlike the `[]` operator, `.at()` performs bounds checking and throws this exception instead of causing undefined behavior.

## Why std::out_of_range Occurs

The most common causes are off-by-one errors, using an index equal to `size()` (which is one past the last valid index), and using negative indices or indices from an unrelated container.

## Wrong: Using .at() With an Invalid Index

```cpp
// WRONG — index 10 does not exist
#include <iostream>
#include <vector>

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5};
    try {
        int val = nums.at(10); // throws std::out_of_range
        std::cout << val << std::endl;
    } catch (const std::out_of_range &e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

**Output:** `Error: vector::_M_range_check: __n (10) >= this->size() (5)`

## Correct: Check Size Before Access

```cpp
// CORRECT — validate index before using .at()
#include <iostream>
#include <vector>

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5};
    size_t index = 10;

    if (index < nums.size()) {
        int val = nums.at(index);
        std::cout << val << std::endl;
    } else {
        std::cerr << "Index " << index << " is out of range" << std::endl;
    }
    return 0;
}
```

## Using .at() vs [] for Safe Access

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {10, 20, 30};

    // [] — no bounds check, undefined behavior on bad index
    std::cout << v[0] << std::endl;

    // .at() — throws std::out_of_range on bad index
    try {
        std::cout << v.at(5) << std::endl;
    } catch (const std::out_of_range &e) {
        std::cerr << "Caught: " << e.what() << std::endl;
    }

    return 0;
}
```

## Wrong: Off-By-One Error With Iterators

```cpp
// WRONG — end() points past the last element
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3};
    auto it = v.end();
    *it = 99; // dereferencing end() — undefined behavior
    return 0;
}
```

## Correct: Iterate Safely

```cpp
// CORRECT — range-based for loop
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3};
    for (const auto &val : v) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

Or use index-based iteration with bounds:

```cpp
// CORRECT — index-based safe iteration
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {10, 20, 30};
    for (size_t i = 0; i < v.size(); i++) {
        std::cout << v.at(i) << std::endl;
    }
    return 0;
}
```

## Safe String Access

Strings are also susceptible to out-of-range errors:

```cpp
#include <iostream>
#include <string>

int main() {
    std::string s = "Hello";

    try {
        char c = s.at(10); // throws std::out_of_range
        std::cout << c << std::endl;
    } catch (const std::out_of_range &e) {
        std::cerr << "String index error: " << e.what() << std::endl;
    }

    // Check length before accessing
    size_t pos = 2;
    if (pos < s.length()) {
        std::cout << "Char at " << pos << ": " << s.at(pos) << std::endl;
    }

    return 0;
}
```

## Using std::optional for Safe Access (C++17)

```cpp
#include <iostream>
#include <vector>
#include <optional>

std::optional<int> safe_get(const std::vector<int> &v, size_t idx) {
    if (idx < v.size()) {
        return v.at(idx);
    }
    return std::nullopt;
}

int main() {
    std::vector<int> v = {10, 20, 30};
    auto val = safe_get(v, 5);
    if (val) {
        std::cout << *val << std::endl;
    } else {
        std::cerr << "Index out of range" << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Check `index < container.size()` | Always before using `.at()` |
| Use `.at()` instead of `[]` | In production code where safety matters |
| Use range-based for loops | When you need to visit every element |
| Use `std::optional` (C++17) | When the absence of a value is expected |
| Wrap `.at()` in try/catch | When invalid input comes from external sources |

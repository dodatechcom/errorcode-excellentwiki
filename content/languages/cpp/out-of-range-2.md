---
title: "[Solution] C++ std::out_of_range — Index Out of Range Fix"
description: "Fix C++ std::out_of_range when accessing containers or strings beyond their valid range. Learn bounds-checking and safe access patterns."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["out-of-range", "bounds-check", "container", "exception"]
weight: 5
---

# [Solution] C++ std::out_of_range — Index Out of Range Fix

A `std::out_of_range` is thrown when an argument (typically an index or iterator) is outside the valid range of an operation. For example, calling `std::vector::at()` with an index beyond the vector size, or accessing `std::string::at()` beyond the string length. It inherits from `std::logic_error`.

## Why std::out_of_range Occurs

Common causes include accessing `vector::at()` with an index >= size, calling `string::at()` beyond string length, using invalid iterators with algorithms, and passing invalid position/length arguments to `string::substr()`.

## Wrong: Using at() Without Checking Bounds

```cpp
// WRONG — throws std::out_of_range
#include <vector>
#include <iostream>

int main() {
    std::vector<int> v = {1, 2, 3};
    int val = v.at(10);  // throws
    std::cout << val << std::endl;
    return 0;
}
```

## Correct: Check Size Before Accessing

```cpp
// CORRECT — check bounds before access
#include <vector>
#include <iostream>
#include <stdexcept>

int safe_get(const std::vector<int>& v, size_t index) {
    if (index >= v.size()) {
        throw std::out_of_range("Index " + std::to_string(index) +
                                " out of range (size: " + std::to_string(v.size()) + ")");
    }
    return v[index];
}

int main() {
    std::vector<int> v = {1, 2, 3};
    try {
        int val = safe_get(v, 10);
        std::cout << val << std::endl;
    } catch (const std::out_of_range& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Safe String Substring

```cpp
// CORRECT — validate substring position
#include <string>
#include <iostream>
#include <stdexcept>

std::string safe_substr(const std::string& s, size_t pos, size_t len = std::string::npos) {
    if (pos > s.size()) {
        throw std::out_of_range("Position " + std::to_string(pos) +
                                " out of range (size: " + std::to_string(s.size()) + ")");
    }
    return s.substr(pos, len);
}

int main() {
    std::string s = "hello";
    try {
        std::string sub = safe_substr(s, 10, 3);
    } catch (const std::out_of_range& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Use Range-Based For to Avoid Bounds Issues

```cpp
// CORRECT — iterate safely
#include <vector>
#include <iostream>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};

    for (const auto& val : v) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use `at()` instead of `[]` | When you need automatic bounds checking |
| Check `size()` before indexing | When using `operator[]` |
| Use range-based for loops | When iterating over containers |
| Validate `substr` arguments | When position/length comes from external input |

## Related Errors

- [std::logic_error]({{< relref "/languages/cpp/logic-error" >}}) — general logic errors.
- [std::invalid_argument]({{< relref "/languages/cpp/invalid-argument" >}}) — invalid function arguments.
- [std::length_error]({{< relref "/languages/cpp/length-error" >}}) — size limit exceeded.

---
title: "[Solution] C++ std::out_of_range — Out of Range Exception Example"
description: "Example of std::out_of_range in C++. Handle vector and string index out of bounds errors safely."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["out-of-range", "vector", "string", "at"]
weight: 50
---

# [Solution] C++ std::out_of_range — Out of Range Exception Example

A `std::out_of_range` exception is thrown when you access a `std::vector` or `std::string` using `.at()` with an index that is beyond the container's valid range. Unlike the `[]` operator, `.at()` performs bounds checking and throws this exception instead of causing undefined behavior.

## Common Causes

- Off-by-one errors (using index equal to `size()`)
- Using negative indices or indices from an unrelated container
- Dereferencing `end()` iterator
- Accessing string positions beyond `length()`

## Example: Throwing std::out_of_range

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5};
    try {
        int val = nums.at(10);  // throws std::out_of_range
        std::cout << val << std::endl;
    } catch (const std::out_of_range& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

## How to Fix: Check Size Before Access

```cpp
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

## Safe Access with std::optional

```cpp
#include <iostream>
#include <vector>
#include <optional>

std::optional<int> safe_get(const std::vector<int>& v, size_t idx) {
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

## Use Range-Based For Loops

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3};
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
| Check `index < container.size()` | Always before using `.at()` |
| Use `.at()` instead of `[]` | In production code where safety matters |
| Use range-based for loops | When you need to visit every element |
| Use `std::optional` (C++17) | When the absence of a value is expected |

## Related Errors

- [std::logic_error]({{< relref "/languages/cpp/logic-error" >}}) — base class for logic errors.
- [std::length_error]({{< relref "/languages/cpp/length-error" >}}) — container size limit exceeded.
- [std::invalid_argument]({{< relref "/languages/cpp/invalid-argument" >}}) — invalid function arguments.

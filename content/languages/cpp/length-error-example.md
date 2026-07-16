---
title: "[Solution] C++ std::length_error — Length Error Exception Example"
description: "Example of std::length_error in C++. Handle container size limits and allocation failures gracefully."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["length-error", "exception", "vector", "container"]
weight: 50
---

# [Solution] C++ std::length_error — Length Error Exception Example

A `std::length_error` exception is thrown when a program attempts to create an object or perform an operation that exceeds an implementation-defined size limit. This is a subclass of `std::logic_error`. Common triggers include requesting a `std::vector` or `std::string` to grow beyond its maximum allowed size, or passing an excessively large count to a container constructor.

## Common Causes

- Excessively large vector or string allocation
- Appending beyond container limits
- `reserve()` with a size that exceeds `max_size`
- Insert with count that overflows

## Example: Throwing std::length_error

```cpp
#include <vector>
#include <stdexcept>
#include <string>

void create_buffer(size_t count) {
    if (count > std::vector<int>::max_size()) {
        throw std::length_error("Requested size exceeds maximum: " + std::to_string(count));
    }
    std::vector<int> buffer(count);
}

int main() {
    try {
        std::vector<int> v(1000000000000ULL);
    } catch (const std::length_error& e) {
        std::cerr << "Container too large: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

## How to Fix: Check Size Limits Before Operations

```cpp
#include <vector>
#include <stdexcept>
#include <iostream>
#include <new>

template <typename T>
void safe_grow(std::vector<T>& vec, size_t additional) {
    size_t new_size = vec.size() + additional;
    if (new_size < vec.size()) {
        throw std::length_error("Size overflow: adding " + std::to_string(additional) +
                                " to " + std::to_string(vec.size()));
    }
    if (new_size > vec.max_size()) {
        throw std::length_error("New size exceeds max_size");
    }
    vec.reserve(new_size);
}

int main() {
    std::vector<int> data;
    try {
        safe_grow(data, 1000000);
        std::cout << "Reserved capacity: " << data.capacity() << std::endl;
    } catch (const std::length_error& e) {
        std::cerr << "Length error: " << e.what() << std::endl;
    } catch (const std::bad_alloc& e) {
        std::cerr << "Allocation failed: " << e.what() << std::endl;
    }
    return 0;
}
```

## Use reserve() Before Bulk push_back

```cpp
#include <vector>
#include <iostream>

int main() {
    // Correct — reserve once, then push_back
    std::vector<int> data;
    data.reserve(1000000);  // pre-allocate exactly what we need
    for (int i = 0; i < 1000000; i++) {
        data.push_back(i);  // no reallocation needed
    }
    std::cout << "Size: " << data.size() << std::endl;
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Check size limits before container operations | When size comes from external input |
| Use `reserve()` before bulk `push_back()` | Always when you know the final size |
| Catch and recover from `std::length_error` | When graceful degradation is possible |
| Use chunked processing for large data | When working with potentially huge datasets |

## Related Errors

- [std::logic_error]({{< relref "/languages/cpp/logic-error" >}}) — base class for logic errors.
- [std::invalid_argument]({{< relref "/languages/cpp/invalid-argument" >}}) — invalid parameter passed to function.
- [std::bad_alloc]({{< relref "/languages/cpp/std-bad-alloc" >}}) — memory allocation failure.

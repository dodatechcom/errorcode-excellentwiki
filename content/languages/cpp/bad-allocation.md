---
title: "[Solution] C++ std::bad_array_new_length — Invalid Array Allocation Fix"
description: "Fix C++ std::bad_array_new_length when allocating arrays with invalid sizes. Handle zero or negative array lengths and size overflow."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["bad-allocation", "array-new", "memory", "new"]
weight: 50
---

# [Solution] C++ std::bad_array_new_length — Invalid Array Allocation Fix

A `std::bad_array_new_length` is thrown when you attempt to allocate an array with a negative size, zero elements (for types without a non-throwing default constructor in some implementations), or a size that would cause an internal arithmetic overflow. This exception was introduced in C++11 and is a subclass of `std::bad_alloc`.

## Why std::bad_array_new_length Occurs

Common causes include requesting `new T[negative_number]`, requesting `new T[0]` for non-default-constructible types, and size calculations that overflow before the allocation call.

## Wrong: Allocating Array with Invalid Size

```cpp
// WRONG — throws std::bad_array_new_length
#include <iostream>

int main() {
    int n = -5;
    int* arr = new int[n];  // negative size — undefined behavior or exception
    delete[] arr;
    return 0;
}
```

## Correct: Validate Size Before Allocation

```cpp
// CORRECT — validate size before array allocation
#include <iostream>
#include <stdexcept>
#include <new>

int main() {
    int n = -5;

    if (n <= 0) {
        std::cerr << "Invalid array size: " << n << std::endl;
        return 1;
    }

    try {
        int* arr = new int[n];
        delete[] arr;
    } catch (const std::bad_array_new_length& e) {
        std::cerr << "Array allocation failed: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

## Safe Array Allocation Helper

```cpp
// CORRECT — wrapper that validates before allocating
#include <iostream>
#include <stdexcept>
#include <new>
#include <memory>

template <typename T>
std::unique_ptr<T[]> safe_new_array(size_t count) {
    if (count == 0) {
        throw std::invalid_argument("Array size must be greater than zero");
    }
    return std::make_unique<T[]>(count);
}

int main() {
    try {
        auto arr = safe_new_array<int>(100);
        std::cout << "Allocated 100 ints" << std::endl;

        auto bad = safe_new_array<int>(0);  // throws
    } catch (const std::invalid_argument& e) {
        std::cerr << "Invalid argument: " << e.what() << std::endl;
    } catch (const std::bad_array_new_length& e) {
        std::cerr << "Allocation failed: " << e.what() << std::endl;
    }
    return 0;
}
```

## Check for Size Overflow Before Allocation

```cpp
// CORRECT — detect size overflow before new[]
#include <iostream>
#include <limits>
#include <new>
#include <vector>

int main() {
    size_t count = std::numeric_limits<size_t>::max() / sizeof(int) + 1;

    // Overflow check: count * sizeof(int) would wrap around
    if (count > std::numeric_limits<size_t>::max() / sizeof(int)) {
        std::cerr << "Size overflow detected" << std::endl;
        return 1;
    }

    int* arr = new int[count];
    delete[] arr;
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Validate array size before `new[]` | Always when size comes from external input |
| Check for overflow in size calculations | When multiplying count by element size |
| Use `std::make_unique` | When you need automatic memory management |
| Use `try-catch` around `new[]` | When allocation may fail |

## Related Errors

- [std::bad_alloc]({{< relref "/languages/cpp/std-bad-alloc" >}}) — general memory allocation failure.
- [std::bad_alloc]({{< relref "/languages/cpp/std-bad-alloc" >}}) — memory allocation failure.
- [std::overflow_error]({{< relref "/languages/cpp/overflowerror" >}}) — arithmetic overflow.

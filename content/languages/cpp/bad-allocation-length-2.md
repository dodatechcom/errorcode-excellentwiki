---
title: "[Solution] C++ std::bad_array_new_length — Array Size Validation Fix"
description: "Fix C++ std::bad_array_new_length when allocating arrays with invalid sizes. Handle zero, negative, or overflowing array lengths."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["bad-array-new-length", "array-allocation", "memory", "new"]
weight: 5
---

# [Solution] C++ std::bad_array_new_length — Array Size Validation Fix

A `std::bad_array_new_length` is thrown when you attempt to allocate an array using `new[]` with an invalid size — such as a negative number, zero (for some types), or a size that causes internal arithmetic overflow. This exception inherits from `std::bad_alloc` and was introduced in C++11.

## Why std::bad_array_new_length Occurs

Common causes include passing a negative value (converted to a large unsigned) to `new[]`, requesting `new T[0]` for non-default-constructible types, and size overflow when multiplying element count by element size.

## Wrong: Allocating Array With Unchecked Size

```cpp
// WRONG — throws std::bad_array_new_length
#include <iostream>

int main() {
    int n = -5;
    int* arr = new int[n];  // negative size causes exception
    delete[] arr;
    return 0;
}
```

## Correct: Validate Size Before Array Allocation

```cpp
// CORRECT — validate size before allocation
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

## Safe Array Allocation with std::vector

```cpp
// CORRECT — use std::vector for safe dynamic arrays
#include <iostream>
#include <vector>

int main() {
    int n = 100;

    if (n <= 0) {
        std::cerr << "Invalid size" << std::endl;
        return 1;
    }

    std::vector<int> arr(n);
    std::cout << "Allocated " << arr.size() << " elements" << std::endl;
    return 0;
}
```

## Check for Overflow Before Allocation

```cpp
// CORRECT — detect overflow in size calculation
#include <iostream>
#include <limits>
#include <new>

int main() {
    size_t count = std::numeric_limits<size_t>::max() / sizeof(int) + 1;

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
| Validate size before `new[]` | When size comes from external input |
| Check for overflow in size calculations | When multiplying count by element size |
| Use `std::vector` | When dynamic array lifetime is needed |
| Use `std::make_unique<T[]>` | When you need automatic memory management |

## Related Errors

- [std::bad_alloc]({{< relref "/languages/cpp/std-bad-alloc" >}}) — general memory allocation failure.
- [std::overflow_error]({{< relref "/languages/cpp/overflowerror" >}}) — arithmetic overflow.
- [std::bad_alloc]({{< relref "/languages/cpp/bad-allocation" >}}) — memory allocation failure.

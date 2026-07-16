---
title: "[Solution] C++ std::bad_alloc — Memory Allocation Failure Fix"
description: "Fix C++ std::bad_alloc when operator new fails to allocate memory. Handle out-of-memory conditions and use alternative allocation strategies."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["bad-alloc", "memory", "new", "allocation"]
weight: 5
---

# [Solution] C++ std::bad_alloc — Memory Allocation Failure Fix

A `std::bad_alloc` is thrown when `operator new` fails to allocate the requested memory. This typically happens when the system runs out of memory or the process exceeds its memory limits. All dynamic memory allocations using `new`, `new[]`, and containers like `std::vector` can throw this exception.

## Why std::bad_alloc Occurs

Common causes include requesting more memory than is available, excessive memory fragmentation preventing large contiguous allocations, memory leaks exhausting available memory, and process memory limits being reached.

## Wrong: Not Handling Allocation Failures

```cpp
// WRONG — may throw std::bad_alloc
#include <iostream>

int main() {
    int* arr = new int[1000000000];  // may fail — no error handling
    delete[] arr;
    return 0;
}
```

## Correct: Catch bad_alloc From Allocation

```cpp
// CORRECT — handle allocation failure
#include <iostream>
#include <new>

int main() {
    try {
        int* arr = new int[1000000000];
        delete[] arr;
    } catch (const std::bad_alloc& e) {
        std::cerr << "Allocation failed: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

## Use std::nothrow for Non-Throwing Allocation

```cpp
// CORRECT — nothrow returns nullptr instead of throwing
#include <iostream>
#include <new>

int main() {
    int* arr = new(std::nothrow) int[1000000000];

    if (arr == nullptr) {
        std::cerr << "Allocation failed" << std::endl;
        return 1;
    }

    delete[] arr;
    return 0;
}
```

## Use Smart Pointers for Automatic Memory Management

```cpp
// CORRECT — use unique_ptr for automatic cleanup
#include <iostream>
#include <memory>
#include <new>

int main() {
    try {
        auto arr = std::make_unique<int[]>(1000);
        std::cout << "Allocated 1000 ints" << std::endl;
    } catch (const std::bad_alloc& e) {
        std::cerr << "Allocation failed: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Catch `std::bad_alloc` | When allocating large or unbounded data |
| Use `new(std::nothrow)` | When you prefer nullptr over exceptions |
| Use `std::make_unique`/`std::make_shared` | For automatic memory management |
| Pre-validate allocation size | When size comes from external input |

## Related Errors

- [std::bad_array_new_length]({{< relref "/languages/cpp/bad-allocation" >}}) — invalid array size.
- [std::bad_alloc (operator new)]({{< relref "/languages/cpp/new-failed" >}}) — operator new failure.
- [std::runtime_error]({{< relref "/languages/cpp/runtimeerror" >}}) — general runtime failures.

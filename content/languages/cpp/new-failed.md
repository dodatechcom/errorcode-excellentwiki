---
title: "[Solution] C++ operator new Failed — New Operator Fix"
description: "Fix C++ operator new failure when memory allocation fails. Handle out-of-memory conditions with nothrow, custom allocators, and smart pointers."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["new-failed", "operator-new", "memory", "allocation"]
weight: 5
---

# [Solution] C++ operator new Failed — New Operator Fix

When `operator new` fails to allocate memory, it throws `std::bad_alloc` by default. You can also use `new(std::nothrow)` to get a `nullptr` instead. Custom `operator new` replacements can provide alternative behaviors such as logging, retrying, or calling a user-defined handler.

## Why operator new Fails

Common causes include system running out of memory, process memory limits exceeded, requesting oversized allocations, and memory fragmentation preventing contiguous allocation.

## Wrong: Assuming new Always Succeeds

```cpp
// WRONG — no error handling for allocation
#include <iostream>

struct LargeObject {
    char data[1024 * 1024];  // 1 MB per object
};

int main() {
    LargeObject* arr = new LargeObject[10000];  // 10 GB — likely fails
    delete[] arr;
    return 0;
}
```

## Correct: Handle new Failure With try-catch

```cpp
// CORRECT — catch std::bad_alloc
#include <iostream>
#include <new>

struct LargeObject {
    char data[1024];
};

int main() {
    try {
        LargeObject* arr = new LargeObject[1000000];
        std::cout << "Allocated successfully" << std::endl;
        delete[] arr;
    } catch (const std::bad_alloc& e) {
        std::cerr << "new failed: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

## Use new(std::nothrow) for nullptr on Failure

```cpp
// CORRECT — nothrow variant returns nullptr
#include <iostream>
#include <new>

int main() {
    int* arr = new(std::nothrow) int[1000000000];

    if (!arr) {
        std::cerr << "Allocation returned nullptr" << std::endl;
        return 1;
    }

    std::cout << "Allocated successfully" << std::endl;
    delete[] arr;
    return 0;
}
```

## Custom operator new With Handler

```cpp
// CORRECT — custom new handler for allocation failures
#include <iostream>
#include <new>
#include <cstdlib>

void out_of_memory_handler() {
    std::cerr << "Out of memory — aborting" << std::endl;
    std::abort();
}

int main() {
    std::set_new_handler(out_of_memory_handler);

    try {
        int* arr = new int[1000000000];
        delete[] arr;
    } catch (const std::bad_alloc& e) {
        std::cerr << "Allocation failed: " << e.what() << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use `try-catch` around `new` | When allocation may fail |
| Use `new(std::nothrow)` | When nullptr is preferred over exceptions |
| Use `std::set_new_handler` | When you need a global allocation failure handler |
| Use smart pointers | For automatic memory management |

## Related Errors

- [std::bad_alloc]({{< relref "/languages/cpp/std-bad-alloc" >}}) — general memory allocation failure.
- [std::bad_array_new_length]({{< relref "/languages/cpp/bad-allocation" >}}) — invalid array size.
- [std::runtime_error]({{< relref "/languages/cpp/runtimeerror" >}}) — general runtime failures.

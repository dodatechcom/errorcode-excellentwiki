---
title: "[Solution] C++ std::bad_alloc — Memory Allocation Failed Fix"
description: "Fix C++ std::bad_alloc when new/malloc fails due to insufficient memory. Handle allocation failures gracefully in C++ programs."
languages: ["cpp"]
severities: ["critical"]
error-types: ["runtime-error", "memory-error"]
tags: ["bad-alloc", "bad_alloc", "new", "malloc", "out-of-memory", "oom"]
weight: 5
---

# [Solution] C++ std::bad_alloc — Memory Allocation Failed Fix

A `std::bad_alloc` is thrown when the `new` operator or `malloc()` fails to allocate the requested amount of memory. This typically happens when the system runs out of available memory, the requested size is unreasonably large, or there is a memory leak gradually exhausting available resources. The exception is defined in `<new>`.

## Common Causes

- **Requesting an excessively large allocation** — `new int[10000000000]` exceeds available memory
- **Memory leak accumulation** — repeated allocations without deallocation exhaust memory over time
- **Fragmented heap** — total free memory exists but is not contiguous
- **Too many threads** — each thread's stack consumes memory, reducing heap availability

## How to Fix

### Fix 1: Use std::nothrow to avoid exceptions

```cpp
#include <iostream>
#include <new>

int main() {
    int* arr = new(std::nothrow) int[100000000];
    if (arr == nullptr) {
        std::cerr << "Allocation failed — out of memory" << std::endl;
        return 1;
    }

    /* use arr ... */
    delete[] arr;
    return 0;
}
```

### Fix 2: Catch and handle bad_alloc

```cpp
#include <iostream>
#include <new>
#include <vector>

int main() {
    try {
        std::vector<int> v;
        v.resize(10000000000ULL);  // may throw std::bad_alloc
    } catch (const std::bad_alloc& e) {
        std::cerr << "Memory allocation failed: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

### Fix 3: Validate size before allocating

```cpp
#include <iostream>
#include <new>
#include <limits>

template <typename T>
T* safe_allocate(size_t count) {
    if (count > std::numeric_limits<size_t>::max() / sizeof(T)) {
        std::cerr << "Allocation size would overflow" << std::endl;
        return nullptr;
    }
    return new(std::nothrow) T[count];
}

int main() {
    int* p = safe_allocate<int>(100);
    if (p) {
        std::cout << "Allocated successfully" << std::endl;
        delete[] p;
    }
    return 0;
}
```

### Fix 4: Use memory pools for frequent small allocations

```cpp
#include <iostream>
#include <vector>
#include <memory>

class ObjectPool {
public:
    ObjectPool(size_t pool_size) : pool_(pool_size) {
        for (size_t i = 0; i < pool_size; i++) {
            free_.push_back(i);
        }
    }

    int allocate() {
        if (free_.empty()) return -1;
        int idx = free_.back();
        free_.pop_back();
        return idx;
    }

    void deallocate(int idx) {
        free_.push_back(idx);
    }

private:
    std::vector<int> pool_;
    std::vector<int> free_;
};

int main() {
    ObjectPool pool(1000);
    int obj = pool.allocate();
    std::cout << "Allocated object at index " << obj << std::endl;
    pool.deallocate(obj);
    return 0;
}
```

## Examples

```cpp
#include <iostream>
#include <new>

int main() {
    /* Huge allocation that will likely fail */
    try {
        int* huge = new int[10000000000LL];
        delete[] huge;
    } catch (const std::bad_alloc& e) {
        std::cerr << "Cannot allocate: " << e.what() << std::endl;
    }

    /* Using new(std::nothrow) for safe failure */
    int* p = new(std::nothrow) int[10000000000LL];
    if (!p) {
        std::cerr << "Allocation returned nullptr" << std::endl;
    }

    return 0;
}
```

## Related Errors

- [std::length_error]({{< relref "/languages/cpp/length-error-3" >}}) — container resize exceeds max allowed size
- [std::bad_array_length]({{< relref "/languages/cpp/bad-allocation-length-2" >}}) — invalid array length in new[]
- [Memory Leak: Valgrind Lost Bytes]({{< relref "/languages/c/memory-leak" >}}) — gradual memory exhaustion

---
title: "[Solution] C++ std::bad_alloc — Memory Allocation Failed Fix"
description: "Fix C++ std::bad_alloc exception when memory allocation fails with proven techniques. Handle out-of-memory conditions and optimize memory usage today."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["bad-alloc", "memory", "allocation", "new"]
weight: 50
---

# [Solution] C++ std::bad_alloc — Memory Allocation Failed Fix

A `std::bad_alloc` exception is thrown when the C++ runtime cannot allocate the requested memory using `new`, `new[]`, or `std::vector::resize()`. This typically means the system has exhausted its available memory or the process has hit its resource limits.

## Why std::bad_alloc Occurs

Common causes include allocating very large arrays, requesting more memory than the system has, memory fragmentation on embedded systems, or a combination of small allocations that accumulate over time.

## Wrong: Not Catching bad_alloc

```cpp
// WRONG — program crashes if allocation fails
#include <vector>

int main() {
    // Attempt to allocate 1 billion ints (~4 GB)
    std::vector<int> v(1000000000);
    return 0;
}
```

## Correct: Catch bad_alloc and Handle It

```cpp
// CORRECT — catch the exception
#include <iostream>
#include <vector>
#include <new>

int main() {
    try {
        std::vector<int> v(1000000000);
    } catch (const std::bad_alloc &e) {
        std::cerr << "Memory allocation failed: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

## Safe Allocation With new (nothrow)

Use `new (std::nothrow)` to get `nullptr` instead of throwing:

```cpp
// CORRECT — nothrow new returns nullptr on failure
#include <iostream>
#include <new>

int main() {
    int *arr = new (std::nothrow) int[1000000000];
    if (arr == nullptr) {
        std::cerr << "Allocation returned nullptr" << std::endl;
        return 1;
    }
    // use arr...
    delete[] arr;
    return 0;
}
```

## Using Smart Pointers to Manage Memory

Smart pointers automatically handle deallocation, reducing the risk of leaks when exceptions occur:

```cpp
// CORRECT — unique_ptr manages memory automatically
#include <memory>
#include <iostream>

int main() {
    try {
        auto arr = std::make_unique<int[]>(1000000000);
        // use arr — memory is freed automatically when scope ends
    } catch (const std::bad_alloc &e) {
        std::cerr << "Allocation failed: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

## Allocating in Chunks Instead of All at Once

For large data, allocate memory in smaller increments to reduce the chance of hitting the limit in a single request:

```cpp
// CORRECT — allocate in chunks
#include <vector>
#include <iostream>
#include <new>

int main() {
    const size_t total = 1000000000;
    const size_t chunk = 1000000;
    std::vector<int> data;
    data.reserve(total);

    for (size_t i = 0; i < total; i += chunk) {
        try {
            data.resize(std::min(i + chunk, total));
        } catch (const std::bad_alloc &e) {
            std::cerr << "Failed at " << i << " elements: " << e.what() << std::endl;
            break;
        }
    }

    std::cout << "Allocated " << data.size() << " elements" << std::endl;
    return 0;
}
```

## Checking System Memory (Linux)

```bash
free -m
ulimit -v
cat /proc/meminfo | grep MemAvailable
```

You can also use `setrlimit` in C++ to enforce a memory ceiling:

```cpp
#include <sys/resource.h>
#include <iostream>

int main() {
    struct rlimit rl;
    rl.rlim_cur = 512 * 1024 * 1024; // 512 MB soft limit
    rl.rlim_max = 512 * 1024 * 1024;
    if (setrlimit(RLIMIT_AS, &rl) != 0) {
        std::cerr << "Failed to set memory limit" << std::endl;
        return 1;
    }
    // Allocations beyond 512 MB will fail
    return 0;
}
```

## Custom Allocator for Large Buffers

For applications that allocate very frequently, a custom allocator can reuse memory and reduce fragmentation:

```cpp
#include <vector>
#include <iostream>

// Pools a fixed-size buffer to avoid repeated new/delete
class PoolAllocator {
    std::vector<int> pool;
public:
    PoolAllocator(size_t capacity) : pool(capacity) {}
    int* data() { return pool.data(); }
    size_t capacity() const { return pool.size(); }
};

int main() {
    PoolAllocator pool(1000000);
    std::cout << "Pool capacity: " << pool.capacity() << std::endl;
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Wrap in try/catch for `std::bad_alloc` | Always when using `new` or large containers |
| Use `new (std::nothrow)` | When you prefer null checks over exceptions |
| Use smart pointers | Always — prevents leaks on exception |
| Allocate in chunks | When dealing with very large data sets |
| Check `free -m` / `ulimit` | During debugging allocation failures |
| Custom allocator | When performance-critical code allocates repeatedly |

---
title: "[Solution] std::bad_alloc Vector Reserve Failure Fix"
description: "Fix std::bad_alloc errors from vector reserve failures. Handle memory allocation failures, large allocations, and OOM conditions."
languages: ["cpp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["std", "bad_alloc", "vector", "memory", "allocation"]
weight: 5
---

# std::bad_alloc Vector Reserve Failure

Fix std::bad_alloc errors from vector reserve failures. Handle memory allocation failures, large allocations, and OOM conditions.

## What This Error Means

`std::bad_alloc` is thrown when the memory allocator cannot satisfy a request:

```
terminate called after throwing an instance of 'std::bad_alloc'
  what():  std::bad_alloc
```

This commonly happens when calling `vector::reserve()` with an excessively large size.

## Common Causes

```cpp
// Cause 1: Requesting too much memory
std::vector<int> v;
v.reserve(1'000'000'000'000ULL); // 1TB - will throw

// Cause 2: Fragmented memory (enough total but not contiguous)
// Cause 3: 32-bit process address space exhaustion
// Cause 4: Oversized container multiplied by element size
```

## How to Fix

### Fix 1: Check available memory before reserving

```cpp
#include <vector>
#include <stdexcept>

template<typename T>
void safe_reserve(std::vector<T>& vec, size_t count) {
    size_t bytes_needed = count * sizeof(T);
    // Conservative limit: 1GB
    if (bytes_needed > 1'000'000'000ULL) {
        throw std::runtime_error("Allocation too large");
    }
    vec.reserve(count);
}
```

### Fix 2: Use try-catch with graceful degradation

```cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> data;
    try {
        data.reserve(10'000'000);
    } catch (const std::bad_alloc&) {
        std::cerr << "Cannot allocate full size, reducing" << std::endl;
        data.reserve(1'000'000);
    }
    return 0;
}
```

### Fix 3: Use reserve with incremental growth

```cpp
#include <vector>

template<typename T>
void grow_vector(std::vector<T>& vec, size_t needed) {
    size_t new_capacity = vec.capacity();
    while (new_capacity < needed) {
        new_capacity = new_capacity + new_capacity / 2; // 1.5x growth
    }
    vec.reserve(new_capacity);
}
```

## Examples

```cpp
#include <vector>
#include <stdexcept>
#include <iostream>

class MemoryAwareBuffer {
    std::vector<char> buffer_;
    size_t max_size_;

public:
    explicit MemoryAwareBuffer(size_t max = 100'000'000)
        : max_size_(max) {}

    void resize(size_t new_size) {
        if (new_size > max_size_) {
            throw std::runtime_error("Buffer size exceeds limit");
        }
        try {
            buffer_.resize(new_size);
        } catch (const std::bad_alloc&) {
            throw std::runtime_error("Out of memory");
        }
    }

    size_t size() const { return buffer_.size(); }
};

int main() {
    MemoryAwareBuffer buf(10'000'000);
    try {
        buf.resize(1'000);
        std::cout << "Allocated " << buf.size() << " bytes" << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Related Errors

- [Bad Alloc 3]({{< relref "/languages/cpp/bad-alloc-3" >}}) — bad_alloc error
- [New Failed]({{< relref "/languages/cpp/new-failed" >}}) — new operator failed
- [Length Error Vector]({{< relref "/languages/cpp/length-error-vector" >}}) — vector length error

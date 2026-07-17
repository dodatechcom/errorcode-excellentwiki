---
title: "[Solution] C++ std::bad_alloc - out of memory with new"
description: "Fix C++ std::bad_alloc when new operator fails due to insufficient memory. Handle allocation failures gracefully."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::bad_alloc - out of memory with new

`std::bad_alloc` is thrown when the `new` operator fails to allocate memory. The system has run out of available memory, or the requested allocation exceeds available resources.

## Common Causes

```cpp
// Cause 1: Excessively large allocation
int* arr = new int[10000000000LL]; // may throw std::bad_alloc

// Cause 2: Memory leak accumulation
while (true) {
    new int[1000]; // leaks memory
}

// Cause 3: Fragmented heap
// Total free memory exists but not contiguous
```

## How to Fix

### Fix 1: Use std::nothrow

```cpp
int* arr = new(std::nothrow) int[100000000];
if (arr == nullptr) {
    std::cerr << "Allocation failed" << std::endl;
    return 1;
}
```

### Fix 2: Catch and handle

```cpp
try {
    int* arr = new int[100000000];
    delete[] arr;
} catch (const std::bad_alloc& e) {
    std::cerr << "Memory allocation failed: " << e.what() << std::endl;
    return 1;
}
```

### Fix 3: Use smart pointers

```cpp
auto arr = std::make_unique<int[]>(100000000);
if (!arr) {
    std::cerr << "Allocation failed" << std::endl;
}
```

## Related Errors

- [std::bad_array_new_length]({{< relref "/languages/cpp/bad-array-new-length" >}}) — invalid array size.
- [std::length_error]({{< relref "/languages/cpp/length-error-vector" >}}) — container resize too large.
- [Memory leak: Valgrind]({{< relref "/languages/c/memory-leak-valgrind" >}}) — gradual memory exhaustion.

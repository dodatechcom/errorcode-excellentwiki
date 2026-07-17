---
title: "[Solution] AddressSanitizer Heap-Buffer-Overflow Fix"
description: "Fix AddressSanitizer heap-buffer-overflow errors. Handle heap memory access beyond allocated bounds."
languages: ["cpp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["asan", "sanitizer", "memory", "heap", "overflow"]
weight: 5
---

# AddressSanitizer Heap-Buffer-Overflow

Fix AddressSanitizer heap-buffer-overflow errors. Handle heap memory access beyond allocated bounds.

## What This Error Means

AddressSanitizer detects when your code reads or writes beyond the allocated heap memory:

```
==12345==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x...
READ of size 4 at 0x... thread T0
    #0 0x... in process_data data.cpp:15
```

## Common Causes

```cpp
// Cause 1: Writing past array bounds
int* arr = new int[10];
arr[10] = 42; // Out of bounds - valid indices are 0-9

// Cause 2: Use-after-free
// Cause 3: Buffer underflow (negative index)
// Cause 4: Off-by-one in loop condition
// Cause 5: Using wrong size in memcpy/memmove
```

## How to Fix

### Fix 1: Use bounds checking containers

```cpp
#include <vector>
#include <stdexcept>

void process(int index) {
    std::vector<int> data = {1, 2, 3, 4, 5};
    if (index < 0 || index >= static_cast<int>(data.size())) {
        throw std::out_of_range("Index out of bounds");
    }
    int value = data[index]; // Safe
}
```

### Fix 2: Use std::span for safe views (C++20)

```cpp
#include <span>
#include <vector>

void process(std::span<int> data) {
    for (int val : data) {  // Range-for is safe
        // Process val
    }
}

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};
    process(v); // Safe
}
```

### Fix 3: Use std::array for fixed-size bounds safety

```cpp
#include <array>

std::array<int, 5> process() {
    std::array<int, 5> arr{1, 2, 3, 4, 5};
    // at() throws std::out_of_range for bad index
    int val = arr.at(10); // Throws instead of undefined behavior
    return arr;
}
```

## Examples

```cpp
#include <vector>
#include <cassert>
#include <iostream>

class SafeBuffer {
    std::vector<uint8_t> data_;

public:
    explicit SafeBuffer(size_t size) : data_(size, 0) {}

    uint8_t& operator[](size_t index) {
        if (index >= data_.size()) {
            throw std::out_of_range("Buffer index out of bounds");
        }
        return data_[index];
    }

    const uint8_t& operator[](size_t index) const {
        if (index >= data_.size()) {
            throw std::out_of_range("Buffer index out of bounds");
        }
        return data_[index];
    }

    size_t size() const { return data_.size(); }
};

int main() {
    SafeBuffer buf(10);
    try {
        buf[5] = 42;   // OK
        buf[15] = 100;  // Throws
    } catch (const std::out_of_range& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Related Errors

- [Sanitizers Address]({{< relref "/languages/cpp/sanitizers-address" >}}) — ASan error
- [Sanitizers Undefined]({{< relref "/languages/cpp/sanitizers-undefined-v2" >}}) — UBSan error
- [Sanitizers Memory]({{< relref "/languages/cpp/sanitizers-memory" >}}) — MSan error

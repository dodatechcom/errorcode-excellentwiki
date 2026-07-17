---
title: "[Solution] C++ std::bad_array_new_length - invalid array size"
description: "Fix C++ std::bad_array_new_length when new[] receives invalid array length."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["bad-array-new-length", "new", "array", "length", "allocation"]
weight: 5
---

# std::bad_array_new_length - invalid array size

`std::bad_array_new_length` is thrown when `new[]` receives an array length that is zero or exceeds implementation limits.

## Common Causes

```cpp
// Cause 1: Zero-length array
int* arr = new int[0]; // throws

// Cause 2: Negative length
int* arr = new int[-5]; // throws (converted to huge unsigned)

// Cause 3: Overflow in size calculation
size_t count = SIZE_MAX / sizeof(int) + 1;
int* arr = new int[count]; // overflow
```

## How to Fix

### Fix 1: Check length before allocation

```cpp
size_t n = get_count();
if (n == 0) {
    // handle zero case
}
int* arr = new int[n];
```

### Fix 2: Use std::vector

```cpp
std::vector<int> v(n); // safe — handles size validation
```

### Fix 3: Catch and handle

```cpp
try {
    int* arr = new int[n];
} catch (const std::bad_array_new_length& e) {
    std::cerr << "Invalid array length: " << e.what() << std::endl;
    return 1;
}
```

## Related Errors

- [std::bad_alloc]({{< relref "/languages/cpp/bad-alloc-nostd" >}}) — allocation failure.
- [std::length_error]({{< relref "/languages/cpp/length-error-vector" >}}) — vector resize too large.
- [std::out_of_range]({{< relref "/languages/cpp/out-of-range-vector" >}}) — index out of range.

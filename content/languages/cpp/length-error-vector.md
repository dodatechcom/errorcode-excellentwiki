---
title: "[Solution] C++ std::length_error - vector resize too large"
description: "Fix C++ std::length_error from vector resize exceeding limits. Check size before resize."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["length-error", "vector", "resize", "max-size", "capacity"]
weight: 5
---

# std::length_error - vector resize too large

`std::length_error` is thrown when a `std::vector::resize()` or `reserve()` call exceeds the maximum possible size.

## Common Causes

```cpp
// Cause 1: Resize to max size
std::vector<int> v;
v.resize(std::numeric_limits<size_t>::max()); // throws

// Cause 2: Reserve overflow
std::vector<int> v;
v.reserve(SIZE_MAX); // throws

// Cause 3: Huge allocation request
std::vector<int> v(100000000000LL); // may throw
```

## How to Fix

### Fix 1: Check size limit

```cpp
if (n <= v.max_size()) {
    v.resize(n);
}
```

### Fix 2: Use try-catch

```cpp
try {
    v.resize(n);
} catch (const std::length_error& e) {
    std::cerr << "Too large: " << e.what() << std::endl;
}
```

### Fix 3: Use smaller chunks

```cpp
std::vector<int> v;
for (size_t i = 0; i < n; i += chunk_size) {
    size_t end = std::min(i + chunk_size, n);
    v.resize(end);
}
```

## Related Errors

- [std::bad_alloc]({{< relref "/languages/cpp/bad-alloc-nostd" >}}) — allocation failure.
- [std::length_error - string]({{< relref "/languages/cpp/length-error-string" >}}) — string too long.
- [std::out_of_range]({{< relref "/languages/cpp/out-of-range-vector" >}}) — index out of range.

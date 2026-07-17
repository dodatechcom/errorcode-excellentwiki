---
title: "[Solution] C++ std::length_error - map max size exceeded"
description: "Fix C++ std::length_error when map exceeds maximum size. Monitor map growth."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::length_error - map max size exceeded

`std::length_error` is thrown when inserting into a `std::map` would exceed its maximum allowed size.

## Common Causes

```cpp
// Cause 1: Excessive insertions
std::map<int, int> m;
for (size_t i = 0; i < SIZE_MAX; i++) {
    m[i] = i; // eventually throws
}

// Cause 2: Huge key count
std::map<std::string, int> m;
m.reserve(m.max_size() + 1); // throws
```

## How to Fix

### Fix 1: Monitor size

```cpp
if (m.size() < m.max_size() - 1) {
    m[key] = value;
}
```

### Fix 2: Use try-catch

```cpp
try {
    m[key] = value;
} catch (const std::length_error& e) {
    std::cerr << "Map full: " << e.what() << std::endl;
}
```

### Fix 3: Use unordered_map with max_load_factor

```cpp
std::unordered_map<int, int> m;
m.max_load_factor(0.25); // control growth
```

## Related Errors

- [std::length_error - vector]({{< relref "/languages/cpp/length-error-vector" >}}) — vector too large.
- [std::length_error - string]({{< relref "/languages/cpp/length-error-string" >}}) — string too long.
- [std::bad_alloc]({{< relref "/languages/cpp/bad-alloc-nostd" >}}) — allocation failure.

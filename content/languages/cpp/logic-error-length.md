---
title: "[Solution] C++ std::logic_error - length error"
description: "Fix C++ std::logic_error length error. Prevent objects from exceeding maximum size."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["logic-error", "length", "max-size", "stdexcept", "container"]
weight: 5
---

# std::logic_error - length error

`std::length_error` is thrown when a container or object exceeds its maximum possible size.

## Common Causes

```cpp
// Cause 1: Vector resize too large
std::vector<int> v;
v.resize(std::numeric_limits<size_t>::max()); // throws

// Cause 2: String too long
std::string s(std::string::npos, 'a'); // throws

// Cause 3: Exceeding max_size
std::vector<int> v;
v.reserve(v.max_size() + 1); // throws
```

## How to Fix

### Fix 1: Check size before resize

```cpp
if (new_size <= v.max_size()) {
    v.resize(new_size);
}
```

### Fix 2: Use reasonable sizes

```cpp
std::vector<int> v;
if (count < 1000000) {
    v.resize(count);
}
```

### Fix 3: Catch and handle

```cpp
try {
    v.resize(huge_number);
} catch (const std::length_error& e) {
    std::cerr << "Too large: " << e.what() << std::endl;
}
```

## Related Errors

- [std::length_error - string]({{< relref "/languages/cpp/length-error-string" >}}) — string too long.
- [std::length_error - map]({{< relref "/languages/cpp/length-error-map" >}}) — map max size.
- [std::bad_alloc]({{< relref "/languages/cpp/bad-alloc-nostd" >}}) — allocation failure.

---
title: "[Solution] C++ std::length_error - string too long"
description: "Fix C++ std::length_error from string exceeding maximum length. Prevent string size overflow."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["length-error", "string", "max-size", "too-long", "capacity"]
weight: 5
---

# std::length_error - string too long

`std::length_error` is thrown when a `std::string` operation would create a string longer than `std::string::max_size()`.

## Common Causes

```cpp
// Cause 1: Concatenation overflow
std::string s(10000000000LL, 'a'); // throws

// Cause 2: Reserve too much
std::string s;
s.reserve(SIZE_MAX); // throws

// Cause 3: Append causing overflow
std::string s = "hello";
s.append(std::string::npos, 'x'); // throws
```

## How to Fix

### Fix 1: Check size before operation

```cpp
if (s.size() + add_size <= s.max_size()) {
    s.append(add);
}
```

### Fix 2: Use streaming

```cpp
std::string result;
for (const auto& chunk : chunks) {
    result += chunk; // grows incrementally
}
```

### Fix 3: Catch and handle

```cpp
try {
    std::string s(huge_size, 'a');
} catch (const std::length_error& e) {
    std::cerr << "String too long: " << e.what() << std::endl;
}
```

## Related Errors

- [std::length_error - vector]({{< relref "/languages/cpp/length-error-vector" >}}) — vector too large.
- [std::length_error - map]({{< relref "/languages/cpp/length-error-map" >}}) — map max size.
- [std::bad_alloc]({{< relref "/languages/cpp/bad-alloc-nostd" >}}) — allocation failure.

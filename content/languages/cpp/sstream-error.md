---
title: "[Solution] C++ std::stringstream - string stream error"
description: "Fix C++ std::stringstream string stream errors. Handle stringstream conversion and I/O failures."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::stringstream - string stream error

`std::stringstream` errors occur when string-to-number conversion fails or the stream enters an error state.

## Common Causes

```cpp
// Cause 1: Format mismatch
std::stringstream ss("hello");
int val;
ss >> val; // failbit

// Cause 2: Empty stream
std::stringstream ss("");
int val;
ss >> val; // failbit

// Cause 3: Incomplete read
std::stringstream ss("1 2");
int a, b;
ss >> a;
ss >> b; // may fail
```

## How to Fix

### Fix 1: Check stream state after read

```cpp
std::stringstream ss(input);
int val;
if (ss >> val) {
    // success
} else {
    std::cerr << "Conversion failed" << std::endl;
}
```

### Fix 2: Use.str() to reset

```cpp
std::stringstream ss;
ss.str("42");
int val;
ss >> val; // success
ss.clear();
ss.str("hello");
ss >> val; // fail
ss.clear();
```

### Fix 3: Use std::from_chars for performance

```cpp
#include <charconv>
int val;
auto [ptr, ec] = std::from_chars(input.data(), input.data() + input.size(), val);
if (ec == std::errc{}) {
    // success
}
```

## Related Errors

- [std::ios_base::failbit]({{< relref "/languages/cpp/ios-base-failbit" >}}) — format error.
- [std::invalid_argument - stoi]({{< relref "/languages/cpp/invalid-argument-stoi" >}}) — conversion error.
- [std::ios_base::failure]({{< relref "/languages/cpp/ios-base-failure" >}}) — stream exception.

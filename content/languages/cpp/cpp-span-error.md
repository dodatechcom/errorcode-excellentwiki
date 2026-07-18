---
title: "[Solution] C++ Span Error — How to Fix"
description: "Fix C++ std::span errors including dynamic extent mismatches, dangling span references, and out-of-bounds access violations."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-time", "runtime"]
weight: 5
comments: true
---

# [Solution] C++ Span Error — How to Fix

C++20 `std::span` provides a non-owning view over a contiguous sequence of objects, but incorrect construction, lifetime mismatches, and extent mismatches lead to undefined behavior or compilation errors.

## Why It Happens

Span errors occur when a span outlives the underlying data, when creating a span from a temporary container, when static extent doesn't match the actual data size, or when accessing elements beyond the span's bounds.

## Common Error Messages

1. `error: static extent mismatch in span construction`
2. `error: cannot convert from 'std::vector<T>' to 'std::span<T, 1>'`
3. `runtime error: span out of bounds access`
4. `error: no matching constructor for 'std::span'`

## How to Fix It

### Fix 1: Avoid Dangling Spans

```cpp
#include <span>
#include <vector>

// WRONG — span dangles after vector is destroyed
std::span<int> create_dangling() {
    std::vector<int> v = {1, 2, 3};
    return std::span<int>(v);  // dangling!
}

// CORRECT — ensure data outlives span
void use_span(std::vector<int>& data) {
    std::span<int> s(data);
    // use s while data is alive
}
```

### Fix 2: Match Static Extent

```cpp
#include <span>
#include <array>

// CORRECT — match static extent to actual size
std::array<int, 3> arr = {1, 2, 3};
std::span<int, 3> s3(arr);     // OK — static extent matches
std::span<int> sd(arr);        // OK — dynamic extent

// WRONG — extent mismatch
// std::span<int, 5> s5(arr); // compilation error
```

### Fix 3: Use Subspan for Safe Slicing

```cpp
#include <span>
#include <iostream>

void process(std::span<int> data) {
    // Safe subspan with bounds checking
    if (data.size() >= 3) {
        auto first_three = data.first(3);
        for (int val : first_three) {
            std::cout << val << " ";
        }
    }
}
```

## Common Scenarios

- **Temporary lifetime**: Passing a temporary vector to span-producing function causes dangling.
- **Stack arrays**: Spans over stack arrays are safe as long as the span doesn't escape the scope.
- **Interfacing with C**: Spans can safely wrap C-style arrays without ownership transfer.

## Prevent It

1. Never return a span created from a local variable — the data will be destroyed.
2. Prefer dynamic extent (`std::span<T>`) unless compile-time size guarantees are needed.
3. Always check `span::size()` before accessing elements to prevent out-of-bounds errors.

## Related Errors

- [Dangling reference]({{< relref "/languages/cpp/dangling-reference" >}}) — references to destroyed objects.
- [Out of bounds]({{< relref "/languages/cpp/out-of-bounds" >}}) — array/vector access beyond limits.
- [String view error]({{< relref "/languages/cpp/cpp-string-view-error" >}}) — similar non-owning view issues.

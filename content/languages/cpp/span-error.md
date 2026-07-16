---
title: "[Solution] C++ std::span Error — Span Bounds Fix"
description: "Fix C++ std::span errors including out-of-bounds access, dangling references, and incorrect size assumptions. Learn safe span usage."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["span", "bounds", "view", "c++20"]
weight: 5
---

# [Solution] C++ std::span Error — Span Bounds Fix

A `std::span` error occurs when accessing elements beyond the span's bounds, when the span dangles (references destroyed data), or when a span is constructed with incorrect size information. `std::span::at()` throws `std::out_of_range`, while `operator[]` has undefined behavior.

## Why std::span Errors Occurs

Common causes include accessing indices beyond span size, span outliving the underlying container, constructing a span with a size larger than the actual data, and using `static_extent` that doesn't match the actual data.

## Wrong: Accessing Span Beyond Bounds

```cpp
// WRONG — undefined behavior
#include <span>
#include <iostream>

int main() {
    int arr[] = {1, 2, 3};
    std::span<int> s(arr, 3);

    std::cout << s[10] << std::endl;  // UB — index 10 out of bounds
    return 0;
}
```

## Correct: Check Span Bounds Before Access

```cpp
// CORRECT — use at() or check size
#include <span>
#include <iostream>
#include <stdexcept>

int main() {
    int arr[] = {1, 2, 3};
    std::span<int> s(arr);

    size_t idx = 10;
    if (idx < s.size()) {
        std::cout << s[idx] << std::endl;
    } else {
        std::cerr << "Index " << idx << " out of range" << std::endl;
    }

    try {
        int val = s.at(10);  // throws std::out_of_range
    } catch (const std::out_of_range& e) {
        std::cerr << e.what() << std::endl;
    }
    return 0;
}
```

## Avoid Dangling Spans

```cpp
// CORRECT — ensure span outlives its data
#include <span>
#include <iostream>
#include <vector>

std::span<int> dangerous() {
    std::vector<int> v = {1, 2, 3};
    return std::span<int>(v);  // dangling — v destroyed on return
}

std::vector<int> safe_data() {
    return {1, 2, 3};
}

int main() {
    auto data = safe_data();
    std::span<int> s(data);  // OK — data is alive

    for (int val : s) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

## Use span for Interface Safety

```cpp
// CORRECT — use span as function parameter
#include <span>
#include <iostream>
#include <vector>

double average(std::span<const double> data) {
    if (data.empty()) return 0.0;
    double sum = 0.0;
    for (double val : data) {
        sum += val;
    }
    return sum / data.size();
}

int main() {
    std::vector<double> values = {1.0, 2.0, 3.0, 4.0, 5.0};
    std::cout << "Average: " << average(values) << std::endl;

    double arr[] = {10.0, 20.0};
    std::cout << "Average: " << average(arr) << std::endl;
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use `at()` for bounds-checked access | When index might be invalid |
| Check `size()` before `operator[]` | When using unchecked access |
| Ensure data outlives the span | Always when creating spans |
| Use `std::span` as function parameter | For non-owning views of contiguous data |

## Related Errors

- [std::out_of_range](/languages/cpp/out-of-range-example/) — container index out of range.
- [std::optional error]({{< relref "/languages/cpp/optional-error" >}}) — optional access errors.
- [std::variant error]({{< relref "/languages/cpp/variant-error" >}}) — variant access errors.

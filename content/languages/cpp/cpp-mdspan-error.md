---
title: "[Solution] C++ Mdspan Error — How to Fix"
description: "Fix C++ std::mdspan errors including dimension mismatches, layout policy conflicts, and multidimensional index out-of-bounds."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-time", "runtime"]
weight: 5
comments: true
---

# [Solution] C++ Mdspan Error — How to Fix

C++23 `std::mdspan` provides a multidimensional array view with customizable layout policies. Dimension mismatches, wrong accessor types, and out-of-bounds access are common pitfalls.

## Why It Happens

Mdspan errors occur when the number of extents in the index pack doesn't match the mdspan's rank, when the underlying data size doesn't satisfy the layout's mapping requirements, when static extents conflict with dynamic construction, or when accessor policies reject the element type.

## Common Error Messages

1. `error: rank mismatch in mdspan operator()`
2. `error: static extent mismatch in mdspan construction`
3. `error: mapping total size exceeds storage`
4. `error: no matching function for call to 'std::mdspan::mdspan'`

## How to Fix It

### Fix 1: Match Index Pack to Rank

```cpp
#include <mdspan>
#include <vector>

// CORRECT — 2D mdspan with 2 indices
std::vector<int> data(12);
std::mdspan<int, std::dextents<size_t, 2>> matrix(data.data(), 3, 4);

matrix[1, 2] = 42;        // OK — C++23 multidimensional subscript
// matrix[1];              // WRONG — rank mismatch
// matrix[1, 2, 3];        // WRONG — too many indices
```

### Fix 2: Use Correct Layout Policies

```cpp
#include <mdspan>
#include <vector>
#include <iostream>

std::vector<double> data(16);

// Row-major (default)
std::mdspan<double, std::dextents<size_t, 2>> row_major(data.data(), 4, 4);

// Column-major
std::mdspan<double, std::dextents<size_t, 2>, std::layout_left>
    col_major(data.data(), 4, 4);

// Both access valid elements
row_major[2, 3] = 1.0;
col_major[2, 3] = 2.0;
```

### Fix 3: Handle Static vs Dynamic Extents

```cpp
#include <mdspan>
#include <array>

// CORRECT — match static extents at compile time
std::array<int, 12> arr{};
std::mdspan<int, std::extents<size_t, 3, 4>> static_mdspan(arr.data());

// CORRECT — fully dynamic
std::mdspan<int, std::dextents<size_t, 2>> dynamic_mdspan(arr.data(), 3, 4);
```

## Common Scenarios

- **Stride access**: Non-standard layouts (strided, layout_left) have different cache behavior.
- **Submdspan**: C++26 adds `std::submdspan` for safe multidimensional slicing.
- **Shared data**: Multiple mdspans can alias the same underlying data with different views.

## Prevent It

1. Always provide the correct number of index arguments matching the mdspan's rank.
2. Use `std::dextents` for dynamic extents and `std::extents` for static extents.
3. Verify the total data size matches `layout mapping::required_span_size()` before construction.

## Related Errors

- [Span out of bounds]({{< relref "/languages/cpp/cpp-span-error" >}}) — 1D span access errors.
- [Array out of bounds]({{< relref "/languages/cpp/out-of-bounds" >}}) — index access violations.
- [Bad alloc]({{< relref "/languages/cpp/bad-alloc" >}}) — allocation failure for mdspan data.

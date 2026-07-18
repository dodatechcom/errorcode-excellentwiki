---
title: "[Solution] C++ Flat Map Error — How to Fix"
description: "Fix C++ std::flat_map errors including insertion failures, comparator issues, and duplicate key handling in sorted container."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-time", "runtime"]
weight: 5
comments: true
---

# [Solution] C++ Flat Map Error — How to Fix

C++23 `std::flat_map` is a sorted associative container backed by a flat storage (typically `std::vector`). It maintains sorted order but enforces unique keys, leading to specific error patterns.

## Why It Happens

Flat map errors occur when inserting duplicate keys, when the comparator doesn't match the key's strict weak ordering requirements, when the underlying container is modified directly bypassing the sorted invariant, or when using `std::flat_map` with non-comparable types.

## Common Error Messages

1. `error: no matching function for call to 'std::flat_map::insert'`
2. `error: comparison function must define strict weak ordering`
3. `runtime error: duplicate key in flat_map`
4. `error: 'operator<' not defined for type`

## How to Fix It

### Fix 1: Handle Duplicate Key Insertion

```cpp
#include <flat_map>
#include <string>
#include <iostream>

std::flat_map<std::string, int> scores;

// WRONG — duplicate key ignored or throws depending on overload
// scores.insert({"alice", 90});
// scores.insert({"alice", 95});  // lost!

// CORRECT — check before inserting
auto [iter, inserted] = scores.try_emplace("alice", 90);
if (!inserted) {
    std::cout << "Key already exists\n";
}
```

### Fix 2: Provide Correct Comparator

```cpp
#include <flat_map>
#include <string>

// CORRECT — case-insensitive comparator
struct CaseInsensitive {
    bool operator()(const std::string& a, const std::string& b) const {
        return std::lexicographical_compare(
            a.begin(), a.end(), b.begin(), b.end(),
            [](char ca, char cb) {
                return std::tolower(ca) < std::tolower(cb);
            });
    }
};

std::flat_map<std::string, int, CaseInsensitive> data;
data.insert({"Hello", 1});
data.insert({"hello", 2});  // overwrites previous
```

### Fix 3: Use Merge for Bulk Insertion

```cpp
#include <flat_map>
#include <vector>

std::flat_map<int, std::string> target;
std::vector<std::pair<int, std::string>> source = {
    {1, "one"}, {2, "two"}, {3, "three"}
};

// CORRECT — bulk construction from sorted data
std::flat_map<int, std::string> from_sorted(source.begin(), source.end());
```

## Common Scenarios

- **Lookup performance**: `find` is O(log n) but `contains` is preferred for boolean checks.
- **Vector backend**: The underlying `std::vector` may reallocate, invalidating iterators.
- **Erase stability**: Erasing elements is O(n) due to shifting in the flat storage.

## Prevent It

1. Always use `try_emplace` or check `insert` return value to handle duplicate keys.
2. Provide a valid strict weak ordering comparator if using custom key types.
3. Consider `std::flat_multimap` (C++23) if you need duplicate keys.

## Related Errors

- [Map iterator invalidation]({{< relref "/languages/cpp/map-iterator-invalidation" >}}) — iterator issues after modification.
- [Bad alloc]({{< relref "/languages/cpp/bad-alloc" >}}) — vector reallocation failure.
- [Comparison error]({{< relref "/languages/cpp/comparator-error" >}}) — invalid strict weak ordering.

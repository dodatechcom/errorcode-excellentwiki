---
title: "[Solution] C++ Flat Map Error — How to Fix"
description: "Fix C++ flat_map errors including sorted range violations, insertion failures, and key comparison issues in boost::container::flat_map."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime", "compile-time"]
weight: 5
comments: true
---

# [Solution] C++ Flat Map Error — How to Fix

Flat maps store key-value pairs in a sorted contiguous array instead of a tree, offering better cache performance but requiring strict sorted-range invariants that can be violated during construction or insertion.

## Why It Happens

Flat map errors occur when inserting elements out of order, using invalid comparators that break the sorted invariant, attempting multi-range construction with unsorted inputs, or violating iterator validity assumptions during modification.

## Common Error Messages

1. `error: Assertion 'boost::container::detail::flat_tree_is_ordered' failed`
2. `error: 'flat_map' insertion aborted — duplicate key or unsorted range`
3. `error: invalid comparator supplied to flat_map`
4. `error: out of range in 'flat_map::at'`

## How to Fix It

### Fix 1: Insert Elements in Sorted Order

```cpp
#include <boost/container/flat_map.hpp>
#include <iostream>

int main() {
    boost::container::flat_map<int, std::string> map;

    // CORRECT — insert in sorted key order
    map.insert({1, "one"});
    map.insert({2, "two"});
    map.insert({3, "three"});

    // WRONG — inserting out of order can cause assertion failure
    // map.insert({5, "five"});
    // map.insert({2, "two"});  // 2 < 5 breaks order

    return 0;
}
```

### Fix 2: Use Range Constructor with Sorted Input

```cpp
#include <boost/container/flat_map.hpp>
#include <vector>
#include <algorithm>
#include <iostream>

int main() {
    std::vector<std::pair<int, std::string>> data = {
        {3, "three"}, {1, "one"}, {2, "two"}
    };

    // MUST sort before range construction
    std::sort(data.begin(), data.end());

    boost::container::flat_map<int, std::string> map(data.begin(), data.end());

    for (const auto& [k, v] : map) {
        std::cout << k << ": " << v << "\n";
    }
    return 0;
}
```

### Fix 3: Use the Correct Comparator

```cpp
#include <boost/container/flat_map.hpp>
#include <string>
#include <iostream>

int main() {
    // CORRECT — descending order comparator
    boost::container::flat_map<int, std::string, std::greater<int>> map;
    map.insert({3, "three"});
    map.insert({1, "one"});
    map.insert({2, "two"});

    for (const auto& [k, v] : map) {
        std::cout << k << ": " << v << "\n";
    }
    return 0;
}
```

### Fix 4: Use try_emplace for Safe Insertion

```cpp
#include <boost/container/flat_map.hpp>
#include <iostream>

int main() {
    boost::container::flat_map<int, std::string> map;

    auto [it, inserted] = map.try_emplace(1, "one");
    std::cout << "Inserted: " << std::boolalpha << inserted << "\n";

    // Duplicate key — won't insert, returns iterator to existing
    auto [it2, inserted2] = map.try_emplace(1, "won");
    std::cout << "Inserted: " << inserted2 << "\n";

    return 0;
}
```

## Common Scenarios

- **Bulk construction**: Calling the range constructor with an unsorted container triggers an assertion failure. Always sort first.
- **Parallel insertion**: Inserting from multiple threads without external synchronization causes data races and corrupted sorted order.
- **Mixed comparators**: Changing the comparator after construction invalidates the sorted invariant.

## Prevent It

1. Always ensure data is sorted by the key comparator before using range constructors.
2. Use `try_emplace` or `insert` rather than `operator[]` for first-time insertions to avoid accidental duplicates.
3. Prefer `boost::container::flat_map` over `std::map` when read performance matters and insertions are infrequent.

## Related Errors

- [std::map out of range]({{< relref "/languages/cpp/out-of-range-map" >}}) — map access errors.
- [std::bad_alloc]({{< relref "/languages/cpp/bad-allocation" >}}) — memory allocation failures.
- [Length error]({{< relref "/languages/cpp/length-error" >}}) — container size limit exceeded.

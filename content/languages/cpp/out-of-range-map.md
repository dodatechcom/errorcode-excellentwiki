---
title: "[Solution] C++ std::out_of_range - map.at() key not found"
description: "Fix C++ std::out_of_range when using map.at() with a non-existent key. Use find() or count() first."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["out-of-range", "map", "at", "key-not-found", "stdexcept"]
weight: 5
---

# std::out_of_range - map.at() key not found

`std::out_of_range` is thrown when `map::at()` is called with a key that does not exist in the map.

## Common Causes

```cpp
// Cause 1: Key doesn't exist
std::map<std::string, int> m = {{"a", 1}};
int val = m.at("b"); // throws std::out_of_range

// Cause 2: Typo in key
std::map<std::string, int> config = {{"host", "localhost"}};
config.at("hosst"); // typo — throws

// Cause 3: Key set conditionally
std::map<int, std::string> m;
if (condition) {
    m[1] = "value";
}
m.at(1); // throws if condition was false
```

## How to Fix

### Fix 1: Use find() instead

```cpp
auto it = m.find("key");
if (it != m.end()) {
    int val = it->second;
}
```

### Fix 2: Use count() first

```cpp
if (m.count("key")) {
    int val = m.at("key");
}
```

### Fix 3: Use operator[] (creates default)

```cpp
int val = m["key"]; // returns 0 if not found
```

## Related Errors

- [std::out_of_range - vector.at()]({{< relref "/languages/cpp/out-of-range-vector" >}}) — vector index out of range.
- [std::out_of_range - string.at()]({{< relref "/languages/cpp/out-of-range-string" >}}) — string index out of range.
- [std::out_of_range - deque.at()]({{< relref "/languages/cpp/out-of-range-deque" >}}) — deque index out of range.

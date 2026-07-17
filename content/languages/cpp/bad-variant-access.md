---
title: "[Solution] C++ std::bad_variant_access - alternative not valid"
description: "Fix C++ std::bad_variant_access. Safely access variant alternatives with type checking."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::bad_variant_access - alternative not valid

`std::bad_variant_access` is thrown when accessing a variant with the wrong type or index. This is the same exception as the wrong type variant.

## Common Causes

```cpp
// Cause 1: Index out of range
std::variant<int, float, double> v = 42;
auto& val = std::get<3>(v); // throws — only 3 alternatives (0, 1, 2)

// Cause 2: Wrong type
std::variant<int, std::string> v = "hello";
int i = std::get<int>(v); // throws

// Cause 3: Index-based access with wrong type
std::variant<int, std::string> v = "hello";
int i = std::get<0>(v); // throws — holds index 1
```

## How to Fix

### Fix 1: Check index with index()

```cpp
if (v.index() == 0) {
    int val = std::get<0>(v);
}
```

### Fix 2: Use std::visit

```cpp
std::visit([](auto&& val) {
    std::cout << val << std::endl;
}, v);
```

### Fix 3: Use std::get_if

```cpp
if (auto* p = std::get_if<0>(&v)) {
    std::cout << *p << std::endl;
}
```

## Related Errors

- [std::bad_variant_access (wrong type)]({{< relref "/languages/cpp/variant-bad-access" >}}) — type mismatch.
- [std::bad_optional_access]({{< relref "/languages/cpp/bad-optional-access" >}}) — empty optional.
- [std::bad_any_cast]({{< relref "/languages/cpp/any-cast-error" >}}) — any_cast failure.

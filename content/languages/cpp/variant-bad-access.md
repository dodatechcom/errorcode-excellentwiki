---
title: "[Solution] C++ std::bad_variant_access - wrong variant type"
description: "Fix C++ std::bad_variant_access when using std::get with wrong type. Use std::holds_alternative first."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::bad_variant_access - wrong variant type

`std::bad_variant_access` is thrown when you call `std::get<T>` on a `std::variant` that does not currently hold type `T`.

## Common Causes

```cpp
// Cause 1: Wrong type in get
std::variant<int, std::string> v = 42;
std::string s = std::get<std::string>(v); // throws

// Cause 2: Getting value without checking
std::variant<int, double> v = 3.14;
int i = std::get<int>(v); // throws

// Cause 3: Index out of range
std::variant<int, double> v = 42;
int i = std::get<2>(v); // throws — index 2 doesn't exist
```

## How to Fix

### Fix 1: Check with holds_alternative

```cpp
if (std::holds_alternative<std::string>(v)) {
    std::string s = std::get<std::string>(v);
}
```

### Fix 2: Use std::get_if (returns nullptr)

```cpp
if (auto* p = std::get_if<std::string>(&v)) {
    std::string s = *p;
}
```

### Fix 3: Use std::visit

```cpp
std::visit([](auto&& val) {
    std::cout << val << std::endl;
}, v);
```

## Related Errors

- [std::bad_variant_access (detailed)]({{< relref "/languages/cpp/bad-variant-access" >}}) — detailed analysis.
- [std::bad_optional_access]({{< relref "/languages/cpp/bad-optional-access" >}}) — empty optional.
- [std::bad_any_cast]({{< relref "/languages/cpp/any-cast-error" >}}) — any_cast failure.

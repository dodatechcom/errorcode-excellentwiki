---
title: "[Solution] C++ std::bad_any_cast - any_cast failure"
description: "Fix C++ std::bad_any_cast when casting std::any to wrong type. Use type checking before cast."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["bad-any-cast", "any-cast", "any", "type-cast", "type-safety"]
weight: 5
---

# std::bad_any_cast - any_cast failure

`std::bad_any_cast` is thrown when `std::any_cast<T>` is used to extract a value of a different type than what was stored.

## Common Causes

```cpp
// Cause 1: Wrong type
std::any a = 42;
std::string s = std::any_cast<std::string>(a); // throws

// Cause 2: Empty any
std::any a;
int val = std::any_cast<int>(a); // throws

// Cause 3: Pointer cast on value
std::any a = 42;
int* p = std::any_cast<int>(&a); // returns nullptr, doesn't throw
```

## How to Fix

### Fix 1: Check type first

```cpp
std::any a = get_value();
if (a.type() == typeid(int)) {
    int val = std::any_cast<int>(a);
}
```

### Fix 2: Use pointer cast

```cpp
if (int* p = std::any_cast<int>(&a)) {
    int val = *p;
} else {
    std::cerr << "Wrong type" << std::endl;
}
```

### Fix 3: Use has_value

```cpp
if (a.has_value()) {
    try {
        int val = std::any_cast<int>(a);
    } catch (const std::bad_any_cast&) {
        std::cerr << "Type mismatch" << std::endl;
    }
}
```

## Related Errors

- [std::bad_cast]({{< relref "/languages/cpp/bad-cast-dynamic" >}}) — dynamic_cast failure.
- [std::bad_variant_access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong variant type.
- [std::bad_optional_access]({{< relref "/languages/cpp/bad-optional-access" >}}) — empty optional.

---
title: "[Solution] C++ std::any_cast Error — Any Type Cast Fix"
description: "Fix C++ std::any_cast errors when extracting values from std::any. Handle type mismatches and empty any values safely."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["any-cast", "std-any", "type-erasure", "c++17"]
weight: 5
---

# [Solution] C++ std::any_cast Error — Any Type Cast Fix

A `std::bad_any_cast` is thrown when `std::any_cast<T>()` is called on a `std::any` that stores a different type than `T`. This exception inherits from `std::bad_cast`. The error occurs when the stored type doesn't match the requested type.

## Why std::any_cast Errors Occur

Common causes include casting to the wrong type, calling `any_cast` on an empty `std::any`, type confusion when storing derived types as base pointers, and using `any_cast` with reference types incorrectly.

## Wrong: Casting to Wrong Type

```cpp
// WRONG — throws std::bad_any_cast
#include <any>
#include <iostream>
#include <string>

int main() {
    std::any val = std::string("hello");

    int num = std::any_cast<int>(val);  // throws — stored type is string
    std::cout << num << std::endl;
    return 0;
}
```

## Correct: Use Pointer any_cast for Safe Access

```cpp
// CORRECT — any_cast<T*> returns nullptr on mismatch
#include <any>
#include <iostream>
#include <string>

int main() {
    std::any val = std::string("hello");

    if (auto* p = std::any_cast<std::string>(&val)) {
        std::cout << "String: " << *p << std::endl;
    } else if (auto* p = std::any_cast<int>(&val)) {
        std::cout << "Int: " << *p << std::endl;
    } else {
        std::cerr << "Type not matched" << std::endl;
    }
    return 0;
}
```

## Check Type Before Casting

```cpp
// CORRECT — verify type before casting
#include <any>
#include <iostream>
#include <string>

int main() {
    std::any val = 42;

    if (val.type() == typeid(int)) {
        int num = std::any_cast<int>(val);
        std::cout << "Int: " << num << std::endl;
    } else if (val.type() == typeid(double)) {
        double d = std::any_cast<double>(val);
        std::cout << "Double: " << d << std::endl;
    }
    return 0;
}
```

## Handle Empty Any

```cpp
// CORRECT — check has_value before casting
#include <any>
#include <iostream>

int main() {
    std::any empty;

    if (empty.has_value()) {
        auto val = std::any_cast<int>(empty);
    } else {
        std::cout << "Any is empty" << std::endl;
    }

    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use `any_cast<T*>(&val)` | For non-throwing access |
| Check `val.type()` before casting | When you need to verify stored type |
| Check `val.has_value()` | When any might be empty |
| Consider `std::variant` | When the type set is known at compile time |

## Related Errors

- [std::bad_variant_access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong type on variant.
- [std::bad_cast]({{< relref "/languages/cpp/bad-cast" >}}) — failed dynamic_cast.
- [std::optional error]({{< relref "/languages/cpp/optional-error" >}}) — optional access errors.

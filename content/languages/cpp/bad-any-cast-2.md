---
title: "[Solution] C++ std::bad_any_cast — Invalid Any Type Cast Fix"
description: "Fix C++ std::bad_any_cast when casting std::any to the wrong type. Learn safe type-erased value access patterns."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::bad_any_cast — Invalid Any Type Cast Fix

A `std::bad_any_cast` is thrown when you use `std::any_cast<T>()` to extract a value from a `std::any` object but the stored type does not match `T`. This exception inherits from `std::bad_cast` and was introduced in C++17.

## Why std::bad_any_cast Occurs

Common causes include casting `std::any` to a type different from what was stored, using `std::any_cast` on an empty `std::any`, and type confusion when storing and retrieving polymorphic types.

## Wrong: Casting std::any to Wrong Type

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

## Correct: Check Type Before Casting

```cpp
// CORRECT — use type() to verify before casting
#include <any>
#include <iostream>
#include <string>

int main() {
    std::any val = std::string("hello");

    if (val.type() == typeid(std::string)) {
        std::string s = std::any_cast<std::string>(val);
        std::cout << "String: " << s << std::endl;
    } else if (val.type() == typeid(int)) {
        int n = std::any_cast<int>(val);
        std::cout << "Int: " << n << std::endl;
    }
    return 0;
}
```

## Use any_cast with Pointer for Non-Throwing Access

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

## Use if constexpr With std::any

```cpp
// CORRECT — safe any access pattern
#include <any>
#include <iostream>
#include <string>
#include <vector>

void print_any(const std::any& val) {
    if (auto* p = std::any_cast<int>(&val)) {
        std::cout << "Int: " << *p << std::endl;
    } else if (auto* p = std::any_cast<double>(&val)) {
        std::cout << "Double: " << *p << std::endl;
    } else if (auto* p = std::any_cast<std::string>(&val)) {
        std::cout << "String: " << *p << std::endl;
    } else {
        std::cout << "Unknown type" << std::endl;
    }
}

int main() {
    std::vector<std::any> values = {42, 3.14, std::string("hello")};

    for (const auto& v : values) {
        print_any(v);
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use `std::any_cast<T*>(&val)` | When you want non-throwing access |
| Check `val.type()` before casting | When you need to verify the stored type |
| Use `val.has_value()` | When checking if any contains a value |
| Consider `std::variant` | When the set of types is known at compile time |

## Related Errors

- [std::bad_variant_access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong type on variant.
- [std::bad_cast]({{< relref "/languages/cpp/bad-cast" >}}) — failed `dynamic_cast`.
- [std::bad_function_call]({{< relref "/languages/cpp/badfunctioncall" >}}) — invoking an empty callable.

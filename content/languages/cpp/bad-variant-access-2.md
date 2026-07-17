---
title: "[Solution] C++ std::bad_variant_access — Variant Type Mismatch Fix"
description: "Fix C++ std::bad_variant_access when accessing a std::variant with the wrong type. Learn safe variant access patterns with std::visit and std::get_if."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::bad_variant_access — Variant Type Mismatch Fix

A `std::bad_variant_access` is thrown when `std::get<T>()` is called on a `std::variant` that does not currently hold a value of type `T`. This commonly happens when code assumes a variant holds a specific type without checking first. The exception also occurs when accessing a variant that is valueless by exception.

## Why std::bad_variant_access Occurs

Common causes include calling `std::get<T>` without first checking `std::holds_alternative<T>`, a variant becoming valueless after a throwing assignment, and using `std::get` on a variant returned from a function that may hold any of its alternative types.

## Wrong: Accessing Variant Without Checking Active Type

```cpp
// WRONG — throws std::bad_variant_access
#include <variant>
#include <iostream>
#include <string>

int main() {
    std::variant<int, std::string, double> v = "hello";

    // v holds string, but we ask for int
    int val = std::get<int>(v);
    std::cout << val << std::endl;
    return 0;
}
```

## Correct: Use std::holds_alternative Before Access

```cpp
// CORRECT — check type before accessing
#include <variant>
#include <iostream>
#include <string>

int main() {
    std::variant<int, std::string, double> v = "hello";

    if (std::holds_alternative<std::string>(v)) {
        std::cout << "String: " << std::get<std::string>(v) << std::endl;
    } else if (std::holds_alternative<int>(v)) {
        std::cout << "Int: " << std::get<int>(v) << std::endl;
    }
    return 0;
}
```

## Use std::get_if for Non-Throwing Access

```cpp
// CORRECT — get_if returns nullptr on mismatch
#include <variant>
#include <iostream>
#include <string>

int main() {
    std::variant<int, std::string, double> v = 3.14;

    if (auto* p = std::get_if<double>(&v)) {
        std::cout << "Double: " << *p << std::endl;
    } else if (auto* p = std::get_if<int>(&v)) {
        std::cout << "Int: " << *p << std::endl;
    } else {
        std::cout << "Holds neither double nor int" << std::endl;
    }
    return 0;
}
```

## Use std::visit for Uniform Handling

```cpp
// CORRECT — visit handles all alternatives safely
#include <variant>
#include <iostream>
#include <string>

int main() {
    std::variant<int, double, std::string> v1 = 42;
    std::variant<int, double, std::string> v2 = 3.14;
    std::variant<int, double, std::string> v3 = "world";

    std::visit([](auto&& val) {
        std::cout << "Value: " << val << std::endl;
    }, v1);

    std::visit([](auto&& val) {
        std::cout << "Value: " << val << std::endl;
    }, v2);

    std::visit([](auto&& val) {
        std::cout << "Value: " << val << std::endl;
    }, v3);
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use `std::holds_alternative` | When you need to check type before access |
| Use `std::get_if` | When you want non-throwing access |
| Use `std::visit` | When handling all types uniformly |
| Use `std::variant::index()` | To check which alternative is active |

## Related Errors

- [std::bad_any_cast]({{< relref "/languages/cpp/badany-cast" >}}) — invalid `std::any` type cast.
- [std::bad_cast]({{< relref "/languages/cpp/bad-cast" >}}) — failed `dynamic_cast` on references.
- [std::bad_function_call]({{< relref "/languages/cpp/badfunctioncall" >}}) — invoking an empty callable.

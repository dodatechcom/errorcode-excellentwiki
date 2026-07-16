---
title: "[Solution] C++ std::bad_variant_access — Invalid Variant Access Fix"
description: "Fix C++ std::bad_variant_access when calling std::get on a std::variant with the wrong type. Handle type-safe variant access safely."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["bad-variant-access", "std-variant", "type-safety", "exception"]
weight: 50
---

# [Solution] C++ std::bad_variant_access — Invalid Variant Access Fix

A `std::bad_variant_access` is thrown when you use `std::get<T>()` on a `std::variant` but the variant currently holds a different type than `T`. It is also thrown by `std::get<T>()` if the variant is valueless by exception. `std::get_if<T>()` does not throw — it returns `nullptr` on mismatch.

## Why std::bad_variant_access Occurs

Common causes include requesting the wrong type from a variant with `std::get`, not checking `std::holds_alternative` before accessing, and a variant becoming valueless after a throwing assignment.

## Wrong: Using std::get Without Checking the Active Type

```cpp
// WRONG — throws std::bad_variant_access
#include <variant>
#include <iostream>
#include <string>

int main() {
    std::variant<int, std::string> v = "hello";

    int val = std::get<int>(v);  // throws — variant holds string
    std::cout << val << std::endl;
    return 0;
}
```

## Correct: Check the Active Type Before Accessing

```cpp
// CORRECT — use std::holds_alternative before std::get
#include <variant>
#include <iostream>
#include <string>

int main() {
    std::variant<int, std::string> v = "hello";

    if (std::holds_alternative<int>(v)) {
        std::cout << "Int: " << std::get<int>(v) << std::endl;
    } else if (std::holds_alternative<std::string>(v)) {
        std::cout << "String: " << std::get<std::string>(v) << std::endl;
    }
    return 0;
}
```

## Use std::get_if for Safe Non-Throwing Access

```cpp
// CORRECT — get_if returns nullptr on type mismatch
#include <variant>
#include <iostream>
#include <string>

int main() {
    std::variant<int, std::string> v = "hello";

    if (auto* p = std::get_if<int>(&v)) {
        std::cout << "Int: " << *p << std::endl;
    } else if (auto* p = std::get_if<std::string>(&v)) {
        std::cout << "String: " << *p << std::endl;
    }
    return 0;
}
```

## Handle Variant with std::visit

```cpp
// CORRECT — use std::visit to handle all types uniformly
#include <variant>
#include <iostream>
#include <string>

struct Overloaded {
    void operator()(int val) const { std::cout << "Int: " << val << std::endl; }
    void operator()(double val) const { std::cout << "Double: " << val << std::endl; }
    void operator()(const std::string& val) const { std::cout << "String: " << val << std::endl; }
};

int main() {
    std::variant<int, double, std::string> v1 = 42;
    std::variant<int, double, std::string> v2 = "hello";

    std::visit(Overloaded{}, v1);  // prints Int: 42
    std::visit(Overloaded{}, v2);  // prints String: hello
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use `std::holds_alternative` before `std::get` | When you need to verify type first |
| Use `std::get_if` | When you want non-throwing access |
| Use `std::visit` | When handling all variant types uniformly |
| Use `std::variant::index()` | To check which type is active |

## Related Errors

- [std::bad_any_cast]({{< relref "/languages/cpp/badany-cast" >}}) — invalid `std::any` cast.
- [std::bad_cast]({{< relref "/languages/cpp/bad-cast" >}}) — failed `dynamic_cast`.
- [std::bad_function_call]({{< relref "/languages/cpp/badfunctioncall" >}}) — invoking an empty callable.

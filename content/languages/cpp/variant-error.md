---
title: "[Solution] C++ std::variant Error — Variant Access Fix"
description: "Fix C++ std::variant errors including bad_variant_access, valueless variants, and type mismatch issues. Learn safe variant handling patterns."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::variant Error — Variant Access Fix

A `std::variant` error occurs when accessing a variant with the wrong type using `std::get`, or when the variant is valueless by exception. `std::bad_variant_access` is thrown on mismatched type access. Variants can also become valueless after a throwing assignment.

## Why std::variant Errors Occur

Common causes include calling `std::get<T>` without checking which type is active, variant becoming valueless after a throwing move constructor, using `std::get` on a variant returned from an unknown source, and not handling all alternative types in visitation.

## Wrong: Accessing Wrong Variant Type

```cpp
// WRONG — throws std::bad_variant_access
#include <variant>
#include <iostream>
#include <string>

int main() {
    std::variant<int, std::string> v = "hello";

    int val = std::get<int>(v);  // throws — holds string
    std::cout << val << std::endl;
    return 0;
}
```

## Correct: Use std::holds_alternative or std::get_if

```cpp
// CORRECT — check type before accessing
#include <variant>
#include <iostream>
#include <string>

int main() {
    std::variant<int, std::string> v = "hello";

    if (auto* p = std::get_if<std::string>(&v)) {
        std::cout << "String: " << *p << std::endl;
    } else if (auto* p = std::get_if<int>(&v)) {
        std::cout << "Int: " << *p << std::endl;
    }
    return 0;
}
```

## Use std::visit for Type-Safe Handling

```cpp
// CORRECT — visit handles all types uniformly
#include <variant>
#include <iostream>
#include <string>

int main() {
    std::variant<int, double, std::string> v = 3.14;

    std::visit([](auto&& val) {
        using T = std::decay_t<decltype(val)>;
        if constexpr (std::is_same_v<T, std::string>) {
            std::cout << "String: " << val << std::endl;
        } else {
            std::cout << "Number: " << val << std::endl;
        }
    }, v);
    return 0;
}
```

## Handle Valueless Variants

```cpp
// CORRECT — check for valueless state
#include <variant>
#include <iostream>
#include <string>

struct MayThrow {
    MayThrow(const char*) { /* may throw */ }
    MayThrow() = default;
};

int main() {
    std::variant<MayThrow, int> v = 42;

    try {
        v.emplace<MayThrow>("test");
    } catch (...) {
        // variant may be valueless
    }

    if (v.valueless_by_exception()) {
        std::cout << "Variant is valueless" << std::endl;
    } else {
        std::cout << "Index: " << v.index() << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use `std::get_if` | For non-throwing type access |
| Use `std::visit` | When handling all alternatives uniformly |
| Check `valueless_by_exception()` | After operations that might leave variant empty |
| Use `std::holds_alternative` | When you need to verify type first |

## Related Errors

- [std::bad_variant_access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong type on variant.
- [std::optional error]({{< relref "/languages/cpp/optional-error" >}}) — optional access errors.
- [std::any_cast error]({{< relref "/languages/cpp/any-cast-error" >}}) — any type cast errors.

---
title: "[Solution] C++ std::bad_any_cast — Invalid Any Cast Fix"
description: "Fix C++ std::bad_any_cast when casting std::any to the wrong type. Handle type-safe casts and validate types before extraction."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# [Solution] C++ std::bad_any_cast — Invalid Any Cast Fix

A `std::bad_any_cast` exception is thrown when you use `std::any_cast` to extract a value from a `std::any` with a type that does not match the stored type. `std::any` is a type-safe container for single values, and casting it to the wrong type produces this exception rather than undefined behavior.

## Why std::bad_any_cast Occurs

Common causes include casting a `std::any` to a different type than what was stored, using `std::any_cast` on an empty `std::any`, casting between incompatible types (e.g., `int` to `double`), or casting to a pointer type when a value is stored.

## Wrong: Casting to the Wrong Type

```cpp
// WRONG — throws std::bad_any_cast
#include <any>
#include <iostream>
#include <string>

int main() {
    std::any a = 42;
    // Stored type is int, but we cast to double
    double val = std::any_cast<double>(a);  // throws std::bad_any_cast
    std::cout << val << std::endl;
    return 0;
}
```

## Correct: Use Type Checks and Matched Casts

```cpp
// CORRECT — verify type before casting
#include <any>
#include <iostream>
#include <string>

int main() {
    std::any a = 42;

    if (a.type() == typeid(int)) {
        int val = std::any_cast<int>(a);
        std::cout << "Int value: " << val << std::endl;
    } else {
        std::cerr << "Type mismatch" << std::endl;
    }
    return 0;
}
```

## Using Pointer Cast to Avoid Exceptions

```cpp
// CORRECT — pointer cast returns nullptr on failure instead of throwing
#include <any>
#include <iostream>
#include <string>

int main() {
    std::any a = std::string("hello");

    // Pointer cast — returns nullptr if type doesn't match
    if (auto* val = std::any_cast<std::string>(&a)) {
        std::cout << "String value: " << *val << std::endl;
    } else {
        std::cerr << "Not a string" << std::endl;
    }

    // Same pattern works for empty any
    std::any empty;
    if (auto* val = std::any_cast<int>(&empty)) {
        std::cout << *val << std::endl;
    } else {
        std::cerr << "Empty or wrong type" << std::endl;
    }
    return 0;
}
```

## Safe Extraction Wrapper

```cpp
// CORRECT — wrap extraction in a try-catch helper
#include <any>
#include <iostream>
#include <optional>

template <typename T>
std::optional<T> safe_any_cast(const std::any& a) {
    try {
        return std::any_cast<T>(a);
    } catch (const std::bad_any_cast&) {
        return std::nullopt;
    }
}

int main() {
    std::any a = 3.14;

    auto int_val = safe_any_cast<int>(a);
    if (int_val) {
        std::cout << "Int: " << *int_val << std::endl;
    } else {
        std::cerr << "Not an int" << std::endl;
    }

    auto double_val = safe_any_cast<double>(a);
    if (double_val) {
        std::cout << "Double: " << *double_val << std::endl;
    } else {
        std::cerr << "Not a double" << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use `std::any_cast<T>(&a)` pointer form | When you want safe, non-throwing cast |
| Check `a.type() == typeid(T)` | When you need the type check before extraction |
| Wrap in try-catch | When exceptions are acceptable for control flow |
| Use `std::any::has_value()` | Before any operation to check emptiness |

## Related Errors

- [std::bad_function_call]({{< relref "/languages/cpp/badfunctioncall" >}}) — invoking an empty `std::function`.
- [std::bad_variant_cast]({{< relref "/languages/cpp/std-bad-alloc" >}}) — invalid `std::variant` access.
- [std::bad_alloc]({{< relref "/languages/cpp/std-bad-alloc" >}}) — memory allocation failure.

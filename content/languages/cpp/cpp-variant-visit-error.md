---
title: "[Solution] C++ std::variant Visit Error — How to Fix"
description: "Fix C++ std::visit and std::variant errors including exhaustive visitor failures, bad_variant_access, and visitor return type mismatches."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-time", "runtime"]
weight: 5
comments: true
---

# [Solution] C++ std::variant Visit Error — How to Fix

`std::visit` errors occur when visitors are not exhaustive (don't handle all types), when accessing the wrong alternative via `std::get`, or when visitor return types are inconsistent across overloads.

## Why It Happens

Variant visit errors arise from incomplete visitor overloads that don't cover all alternative types, calling `std::get<T>` when the variant holds a different type, inconsistent return types across visitor overloads, or visiting a valueless variant after an exception.

## Common Error Messages

1. `error: no matching function for call to 'visit' with overloaded lambda`
2. `runtime error: std::get on valueless variant`
3. `error: no viable conversion from return type of visitor`
4. `error: call to non-constexpr function in visitor`

## How to Fix It

### Fix 1: Provide Complete Visitor Overloads

```cpp
#include <variant>
#include <iostream>
#include <string>

int main() {
    std::variant<int, double, std::string> v = 42;

    // CORRECT — overload for all types
    std::visit([](auto&& val) {
        using T = std::decay_t<decltype(val)>;
        if constexpr (std::is_same_v<T, int>)
            std::cout << "int: " << val << "\n";
        else if constexpr (std::is_same_v<T, double>)
            std::cout << "double: " << val << "\n";
        else if constexpr (std::is_same_v<T, std::string>)
            std::cout << "string: " << val << "\n";
    }, v);

    return 0;
}
```

### Fix 2: Check for Valueless Variant Before Access

```cpp
#include <variant>
#include <iostream>
#include <string>
#include <stdexcept>

int main() {
    std::variant<int, std::string> v = "hello";

    try {
        v = std::get<int>(v);  // throws, makes v valueless
    } catch (...) {}

    // CORRECT — check before visiting
    if (!v.valueless_by_exception()) {
        std::visit([](auto&& val) {
            std::cout << "Value: " << val << "\n";
        }, v);
    } else {
        std::cout << "Variant is valueless\n";
    }

    return 0;
}
```

### Fix 3: Use Overloaded Lambda Pattern

```cpp
#include <variant>
#include <iostream>
#include <string>

template<class... Ts> struct overloaded : Ts... { using Ts::operator()...; };

int main() {
    std::variant<int, double, std::string> v = 3.14;

    // CORRECT — overloaded lambda handles all types
    std::visit(overloaded{
        [](int i) { std::cout << "int: " << i << "\n"; },
        [](double d) { std::cout << "double: " << d << "\n"; },
        [](const std::string& s) { std::cout << "string: " << s << "\n"; }
    }, v);

    return 0;
}
```

### Fix 4: Ensure Consistent Visitor Return Types

```cpp
#include <variant>
#include <iostream>
#include <string>

int main() {
    std::variant<int, std::string> v = 42;

    // WRONG — inconsistent return types
    // std::visit([](auto&& val) -> std::string {
    //     if constexpr (std::is_same_v<decltype(val), int>)
    //         return std::to_string(val);  // OK
    //     else
    //         return val;  // OK but both must agree
    // }, v);

    // CORRECT — consistent return type
    std::string result = std::visit([](auto&& val) -> std::string {
        using T = std::decay_t<decltype(val)>;
        if constexpr (std::is_same_v<T, int>)
            return std::to_string(val);
        else
            return val;
    }, v);

    std::cout << result << "\n";
    return 0;
}
```

## Common Scenarios

- **Incomplete visitor**: Using `if constexpr` without covering all types causes a compile error.
- **Valueless variant**: After a failed assignment, the variant becomes valueless and `std::get` throws.
- **Return type mismatch**: Lambda overloads returning different types without a common type fail to compile.

## Prevent It

1. Always provide overloads for every alternative type in the variant.
2. Check `valueless_by_exception()` before visiting or accessing a variant that may have thrown.
3. Use `if constexpr` with a catch-all `else` clause to ensure all paths return the same type.

## Related Errors

- [Bad variant access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong type access.
- [Bad any cast]({{< relref "/languages/cpp/any-cast-error" >}}) — wrong type in std::any.
- [std::bad_optional_access]({{< relref "/languages/cpp/bad-optional-access" >}}) — empty optional access.

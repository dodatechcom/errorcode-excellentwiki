---
title: "[Solution] C++ std::any_cast Error — How to Fix"
description: "Fix C++ std::any_cast errors including bad_any_cast exceptions, type mismatches, and null pointer casts on std::any values."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C++ std::any_cast Error — How to Fix

`std::any_cast` throws `std::bad_any_cast` when attempting to extract a value of a type that doesn't match the stored type, or when casting from an empty `std::any` object.

## Why It Happens

Any cast errors occur when requesting a type different from what was stored, calling `any_cast` on a valueless `std::any`, using pointer-based `any_cast` without checking the return value, or storing types that are not copy-constructible.

## Common Error Messages

1. `std::bad_any_cast: std::any_cast failed`
2. `error: use of deleted function in 'any_cast'`
3. `runtime error: bad any_cast — type mismatch`
4. `error: cannot cast 'std::any' to incomplete type`

## How to Fix It

### Fix 1: Check the Type Before Casting

```cpp
#include <any>
#include <iostream>
#include <string>

int main() {
    std::any a = std::string("hello");

    // CORRECT — check type before casting
    if (a.type() == typeid(std::string)) {
        auto val = std::any_cast<std::string>(a);
        std::cout << "String: " << val << "\n";
    }

    // WRONG — wrong type throws bad_any_cast
    // auto val = std::any_cast<int>(a);

    return 0;
}
```

### Fix 2: Use Pointer-Based any_cast for Safe Access

```cpp
#include <any>
#include <iostream>
#include <string>

int main() {
    std::any a = 42;

    // CORRECT — pointer cast returns nullptr on mismatch
    int* p = std::any_cast<int>(&a);
    if (p) {
        std::cout << "Int: " << *p << "\n";
    }

    double* d = std::any_cast<double>(&a);
    if (!d) {
        std::cout << "Not a double\n";
    }

    return 0;
}
```

### Fix 3: Handle Empty Any Objects

```cpp
#include <any>
#include <iostream>

int main() {
    std::any a;

    // CORRECT — check if any has a value
    if (a.has_value()) {
        auto val = std::any_cast<int>(a);
        std::cout << val << "\n";
    } else {
        std::cout << "any is empty\n";
    }

    return 0;
}
```

### Fix 4: Use make_any for Perfect Forwarding

```cpp
#include <any>
#include <iostream>
#include <string>

int main() {
    // CORRECT — use std::make_any for clean construction
    auto a = std::make_any<std::string>("hello world");
    auto b = std::make_any<int>(42);

    std::cout << std::any_cast<std::string>(a) << "\n";
    std::cout << std::any_cast<int>(b) << "\n";

    // Reassign safely
    a = 3.14;
    std::cout << std::any_cast<double>(a) << "\n";

    return 0;
}
```

## Common Scenarios

- **Type mismatch**: Storing an `int` and casting to `double` throws `bad_any_cast`.
- **Empty any**: Default-constructed `std::any` has no value — any cast fails.
- **Polymorphic types**: `any_cast` works on the exact stored type, not base classes.

## Prevent It

1. Always use the pointer form of `any_cast` (`std::any_cast<T>(&a)`) to avoid exceptions.
2. Check `a.has_value()` before calling value-based `any_cast`.
3. Prefer `std::variant` over `std::any` when the set of possible types is known at compile time.

## Related Errors

- [Bad variant access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong variant type.
- [Bad optional access]({{< relref "/languages/cpp/bad-optional-access" >}}) — empty optional access.
- [Bad cast]({{< relref "/languages/cpp/bad-cast-dynamic" >}}) — failed dynamic_cast.

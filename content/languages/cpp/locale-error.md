---
title: "[Solution] C++ std::runtime_error: Locale — Locale Error Fix"
description: "Fix C++ std::runtime_error from locale operations. Handle invalid locale names, unsupported facets, and locale construction failures."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["locale", "runtime-error", "internationalization", "facet"]
weight: 5
---

# [Solution] C++ std::runtime_error: Locale — Locale Error Fix

A `std::runtime_error` is thrown when locale operations fail — such as constructing a `std::locale` with an invalid name, accessing a facet that is not present in a locale, or locale conversion failures. This can happen with user-provided locale names or platform-specific locale identifiers.

## Why Locale Errors Occur

Common causes include constructing `std::locale` with an unsupported locale name, using `std::use_facet` when the facet is not in the locale, platform-specific locale name differences (e.g., "en_US.UTF-8" vs "English_United States"), and locale name encoding issues.

## Wrong: Constructing Locale With Invalid Name

```cpp
// WRONG — throws runtime_error for invalid locale
#include <locale>
#include <iostream>

int main() {
    std::locale loc("invalid_nonexistent_locale");  // throws
    return 0;
}
```

## Correct: Catch Locale Construction Errors

```cpp
// CORRECT — catch and handle locale errors
#include <locale>
#include <iostream>
#include <stdexcept>

int main() {
    try {
        std::locale loc("en_US.UTF-8");
        std::cout << "Locale: " << loc.name() << std::endl;
    } catch (const std::runtime_error& e) {
        std::cerr << "Locale error: " << e.what() << std::endl;
        std::locale::global(std::locale::classic());
        std::cerr << "Using classic locale" << std::endl;
    }
    return 0;
}
```

## Safe Facet Access

```cpp
// CORRECT — check has_facet before using use_facet
#include <locale>
#include <iostream>

int main() {
    std::locale loc = std::locale::classic();

    if (std::has_facet<std::numpunct<char>>(loc)) {
        const auto& facet = std::use_facet<std::numpunct<char>>(loc);
        std::cout << "Decimal point: " << facet.decimal_point() << std::endl;
    } else {
        std::cerr << "numpunct facet not available" << std::endl;
    }
    return 0;
}
```

## Portable Locale Handling

```cpp
// CORRECT — use classic locale as fallback
#include <locale>
#include <iostream>
#include <string>

std::locale get_system_locale() {
    try {
        return std::locale("");
    } catch (const std::runtime_error&) {
        return std::locale::classic();
    }
}

int main() {
    std::locale loc = get_system_locale();
    std::cout << "Using locale: " << loc.name() << std::endl;
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Catch `std::runtime_error` from locale | When locale names come from config/user |
| Use `std::locale::classic()` as fallback | When system locale is unavailable |
| Check `has_facet` before `use_facet` | When facet availability is uncertain |
| Use empty string `""` for system locale | When you want the default locale |

## Related Errors

- [std::runtime_error]({{< relref "/languages/cpp/runtimeerror" >}}) — general runtime failures.
- [std::codecvt error]({{< relref "/languages/cpp/codecvt-error" >}}) — character conversion errors.
- [std::ios_base::failure]({{< relref "/languages/cpp/ios-failure" >}}) — stream I/O errors.

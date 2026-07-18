---
title: "[Solution] C++ Locale Error — How to Fix"
description: "Fix C++ std::locale errors including facet creation failures, locale name parsing errors, and codecvt conversion issues across character encodings."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime", "compile-time"]
weight: 5
comments: true
---

# [Solution] C++ Locale Error — How to Fix

`std::locale` and its facets handle internationalization and encoding, but invalid locale names, missing facets, and encoding conversion failures produce runtime errors that are difficult to diagnose.

## Why It Happens

Locale errors occur when constructing locales with invalid names that don't exist on the system, when requesting facets that aren't available in a given locale, when codecvt conversions fail due to invalid multibyte sequences, or when locale objects are accessed after their originating locale goes out of scope.

## Common Error Messages

1. `std::runtime_error: locale::facet::_S_create_c_locale`
2. `std::bad_cast: bad dynamic_cast in locale facet`
3. `error: codecvt_base::error in character conversion`
4. `error: invalid locale name`

## How to Fix It

### Fix 1: Handle Invalid Locale Names

```cpp
#include <locale>
#include <iostream>
#include <string>

int main() {
    // WRONG — invalid locale name may throw
    // std::locale bad("nonexistent_locale.UTF-8");

    // CORRECT — catch locale construction errors
    try {
        std::locale loc("en_US.UTF-8");
        std::cout << "Locale: " << loc.name() << "\n";
    } catch (const std::runtime_error& e) {
        std::cout << "Locale error: " << e.what() << "\n";
        std::cout << "Using default locale\n";
        std::locale loc = std::locale::classic();
    }

    return 0;
}
```

### Fix 2: Use Facet Access Safely

```cpp
#include <locale>
#include <iostream>
#include <string>

int main() {
    std::locale loc = std::locale::classic();

    // CORRECT — check if facet exists
    if (std::has_facet<std::ctype<char>>(loc)) {
        const auto& facet = std::use_facet<std::ctype<char>>(loc);
        char upper = facet.toupper('a');
        std::cout << "Upper: " << upper << "\n";
    }

    // WRONG — bad_cast if facet doesn't exist
    // const auto& bad = std::use_facet<std::ctype<wchar_t>>(loc);

    return 0;
}
```

### Fix 3: Handle Codecvt Conversion Errors

```cpp
#include <codecvt>
#include <locale>
#include <iostream>
#include <string>

int main() {
    std::string utf8_text = "Hello, World!";

    // CORRECT — use codecvt for encoding conversion
    try {
        std::wstring_convert<std::codecvt_utf8<wchar_t>> converter;
        std::wstring wide = converter.from_bytes(utf8_text);
        std::string narrow = converter.to_bytes(wide);
        std::cout << "Converted: " << narrow << "\n";
    } catch (const std::range_error& e) {
        std::cout << "Conversion error: " << e.what() << "\n";
    }

    return 0;
}
```

### Fix 4: Use Locale for Number Formatting

```cpp
#include <locale>
#include <iostream>
#include <sstream>

int main() {
    // CORRECT — use locale for locale-aware formatting
    std::locale loc("de_DE.UTF-8");
    std::stringstream ss;
    ss.imbue(loc);

    ss << 1234567.89;
    std::cout << "German format: " << ss.str() << "\n";

    // Fallback if German locale unavailable
    std::locale fallback = std::locale::classic();
    ss.clear();
    ss.str("");
    ss.imbue(fallback);
    ss << 1234567.89;
    std::cout << "Classic format: " << ss.str() << "\n";

    return 0;
}
```

## Common Scenarios

- **Missing locale**: Systems without installed locales (e.g., Docker containers) fail to construct named locales.
- **Facet mismatch**: Requesting a facet that wasn't registered with the locale throws `std::bad_cast`.
- **Encoding errors**: Invalid UTF-8 sequences in input cause `codecvt` to throw `std::range_error`.

## Prevent It

1. Always catch `std::runtime_error` when constructing named locales from external input.
2. Use `std::locale::classic()` as a fallback when system-specific locales are unavailable.
3. Validate multibyte strings before attempting codecvt conversions.

## Related Errors

- [Filesystem error]({{< relref "/languages/cpp/filesystemerror" >}}) — path encoding issues.
- [String view error]({{< relref "/languages/cpp/cpp-string-view-error" >}}) — string encoding issues.
- [System error]({{< relref "/languages/cpp/system-error-system" >}}) — platform failures.

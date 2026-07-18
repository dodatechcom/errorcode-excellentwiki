---
title: "[Solution] C++ char8_t Error — How to Fix"
description: "Fix C++ char8_t errors including UTF-8 encoding failures, type conversion issues, and incompatible string types in C++20 code."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-time"]
weight: 5
comments: true
---

# [Solution] C++ char8_t Error — How to Fix

C++20 introduced `char8_t` as a distinct type for UTF-8 character data, creating type incompatibilities with `char` and `unsigned char` that break existing string handling code.

## Why It Happens

char8_t errors occur when assigning UTF-8 string literals to `char*` instead of `char8_t*`, when mixing `char` and `char8_t` in APIs that expect specific types, when using `std::string` with UTF-8 data that should use `std::u8string`, or when implicit conversions between char8_t and char are needed but forbidden.

## Common Error Messages

1. `error: cannot convert 'const char8_t*' to 'const char*'`
2. `error: cannot initialize a variable of type 'char*' with an rvalue of type 'const char8_t*'`
3. `error: invalid conversion from 'char8_t' to 'char'`
4. `error: no matching function for call to 'std::string(const char8_t*)'`

## How to Fix It

### Fix 1: Use char8_t for UTF-8 Literals

```cpp
#include <iostream>
#include <string>

int main() {
    // WRONG — C++20 makes u8"..." produce char8_t[]
    // const char* s = u8"hello";

    // CORRECT — use char8_t for u8 literals
    const char8_t* s = u8"hello";
    std::cout << reinterpret_cast<const char*>(s) << "\n";

    return 0;
}
```

### Fix 2: Use std::u8string for UTF-8 Data

```cpp
#include <iostream>
#include <string>

int main() {
    // CORRECT — use u8string for UTF-8 in C++20
    std::u8string utf8_str = u8"Hello, World!";

    // Convert for display
    std::string display(
        reinterpret_cast<const char*>(utf8_str.c_str()),
        utf8_str.size()
    );
    std::cout << display << "\n";

    return 0;
}
```

### Fix 3: Create Conversion Helpers

```cpp
#include <iostream>
#include <string>

// Helper to convert char8_t* to const char*
inline const char* to_char(const char8_t* u8str) {
    return reinterpret_cast<const char*>(u8str);
}

// Helper to convert const char* to char8_t*
inline const char8_t* to_char8(const char* str) {
    return reinterpret_cast<const char8_t*>(str);
}

int main() {
    const char8_t* u8 = u8"UTF-8 text";
    std::cout << to_char(u8) << "\n";

    const char* narrow = "narrow text";
    // Can now use to_char8(narrow) when char8_t* is needed

    return 0;
}
```

### Fix 4: Conditional Compilation for Compatibility

```cpp
#include <iostream>
#include <string>

// CORRECT — handle both C++17 and C++20
#if __cplusplus >= 202002L
    using char_t = char8_t;
    #define UTF8_LITERAL u8
#else
    using char_t = char;
    #define UTF8_LITERAL u8
#endif

int main() {
    // Works in both C++17 and C++20
    const char_t* text = UTF8_LITERAL"Hello";
    std::cout << reinterpret_cast<const char*>(text) << "\n";

    return 0;
}
```

## Common Scenarios

- **C++20 migration**: Existing code using `u8"..."` with `char*` fails to compile.
- **API mismatch**: Third-party libraries expecting `const char*` don't accept `char8_t*`.
- **String comparison**: Comparing `std::string` with `std::u8string` requires explicit conversion.

## Prevent It

1. Use `reinterpret_cast<const char*>` when passing `char8_t*` to APIs expecting `char*`.
2. Create helper functions for conversions if your codebase mixes UTF-8 and narrow strings.
3. Enable C++20 mode and fix char8_t warnings immediately — don't suppress them.

## Related Errors

- [String view error]({{< relref "/languages/cpp/cpp-string-view-error" >}}) — string_view lifetime issues.
- [Locale error]({{< relref "/languages/cpp/cpp-locale-error" >}}) — encoding and locale issues.
- [Type erasure error]({{< relref "/languages/cpp/cpp-type-erasure-error" >}}) — type mismatch issues.
